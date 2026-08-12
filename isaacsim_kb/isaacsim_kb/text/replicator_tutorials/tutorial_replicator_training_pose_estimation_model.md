<!-- source: replicator_tutorials/tutorial_replicator_training_pose_estimation_model.html | title: Training Pose Estimation Model with Synthetic Data — Isaac Sim Documentation -->

# Training Pose Estimation Model with Synthetic Data
Warning
[DEPRECATED]: This tutorial will no longer be maintained in future releases and API breaking changes may occur.
This tutorial covers the following topics:

- How to generate synthetic data with Isaac Sim on the OVX clusters on NGC. Using these clusters enables you to scale up your synthetic data generation.

- How to train and evaluate a DOPE model on NGC using data that has been uploaded to an S3 bucket. This enables you to scale up your model training by training multiple models concurrently on clusters with multiple GPUs.

50-60 min tutorial

## Prerequisites
This tutorial requires:

- Working knowledge of the Pose Estimation tutorial.

- Basic understanding of how to submit jobs on NGC using Base Command. For instructions, see section 3.3 of NGC Private Registry User Guide .

### Generating Data on NGC
Generating data on NGC using the OVX clusters allows you to significantly increase the amount of data you can generate compared to using your local machine. The OVX clusters are used for data generation because they are optimized for rendering jobs. Training uses the DGX clusters, which are optimized for machine learning. Because the tutorial uses two different clusters for generation and training, it automatically saves our generated data to an S3 bucket, which is then used to load data during training.

## Building Your Own Container for Data Generation
To build a container to run on NGC, use a `Dockerfile`. To do so:

- Copy the contents below into a file called `Dockerfile`.

- Place the `Dockerfile` in `standalone_examples/replicator/pose_generation`.

Dockerfile to create container for NGC
```
# See https://catalog.ngc.nvidia.com/orgs/nvidia/containers/isaac-sim
# for instructions on how to run this container
FROM nvcr.io/nvidia/isaac-sim:5.1.0

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && apt-get install s3cmd -y

# Copies over latest changes to pose generation code when building the container
COPY ./ standalone_examples/replicator/pose_generation
```
Any updates you have made locally to the `pose_generation.py` or other files in the `standalone_examples/replicator/pose_generation` folder are copied over to the container when you build. This enables workflows where you need to modify the existing files inside `pose_generation/`. For example, to generate data for a custom object by modifying the `config/` files.
To build the container, run:

```
cd standalone_examples/replicator/pose_generation
docker build -t NAME_OF_YOUR_CONTAINER:TAG .
```

## Pushing a Docker Container to NGC
To use this new container in NGC, you must push it to NGC. To push a container to NGC, you must authenticate. To authenticate, follow this NGC guide .
When pushing a container to NGC, there is a specific naming format that must be followed. The name of the container must be `nvcr.io/<ORGANIZATION_NAME>/<TEAM_NAME>/<CONTAINER_NAME>:<TAG>`. For more details on pushing containers to NGC, see this guide .

```
docker push NAME_OF_YOUR_CONTAINER:TAG
```

## Adding S3 Credentials to NGC Jobs
If you are planning on using data from an S3 bucket or writing your results to an S3 bucket, you must add your credentials as part of the job definition. Secrets cannot be managed using NGC.
You can upload your credentials by appending the command below to the beginning of your `Run Command` in your job definition. Make sure to fill in your credentials in the places marked.

```
# Credentials for boto3
mkdir ~/.aws
echo "[default]" >> ~/.aws/config
echo "aws_access_key_id = <YOUR_USER_NAME>" >> ~/.aws/config
echo "aws_secret_access_key = <YOUR_SECRET_KEY>" >> ~/.aws/config
# Credentials for s3cmd
echo "[default]" >> ~/.s3cfg
echo "use_https = True" >> ~/.s3cfg
echo "access_key = <YOUR_USER_NAME>" >> ~/.s3cfg
echo "secret_key = <YOUR_SECRET_KEY>" >> ~/.s3cfg
echo "bucket_location = us-east-1" >> ~/.s3cfg
echo "host_base = <YOUR_ENDPOINT>" >> ~/.s3cfg
echo "host_bucket = bucket-name" >> ~/.s3cfg
```
After pushing the container to NGC, select this container when creating a job. You can use the following run command:

```
# ADD YOUR S3 CREDENTIALS HERE
# (see "Adding S3 Credentials to NGC Jobs" section above for more details)

# Run Pose Generation
./python.sh standalone_examples/replicator/pose_generation/pose_generation.py \
--use_s3 --endpoint https://YOUR_ENDPOINT --bucket OUTPUT_BUCKET --num_dome 1000 --num_mesh 1000 --writer DOPE \
--no-window
```
Note
Isaac Sim requires the `--no-window` flag so that it can run in `headless` mode regardless of what other settings you might have.

## Submit Jobs on OVX Clusters
To submit a job on the OVX clusters, it must be made pre-preemptable. To do this, select `Resumable` under Preemption Options when creating the job.

### Train, Inference, and Evaluate

## Running Locally
To run the training, inference, and evaluation scripts locally:

- Clone the official DOPE Repo .

- Follow the instructions in the train/README.md file within the repo.

Note
The instructions in the DOPE repository are intended for Linux and were not tested on other operating systems.

## Running on NGC
NGC offers you the ability to scale your training jobs. Because DOPE needs to be trained separately for each class of object, NGC is extremely helpful in enabling multiple models to be trained concurrently. Furthermore, it reduces the time that it would take to train models using multi-GPU jobs.
When creating a job, copy over the command below and use it as your job’s `Run Command` on NGC. You must replace the parameter values with values for your environment.
If you would like to run the entire training, inference, and evaluation pipeline in one go, you can refer to the Running the Entire Pipeline in One Command section below.

```
# ADD YOUR S3 CREDENTIALS HERE
# (see "Adding S3 Credentials to NGC Jobs" section for more details)

# Change values below:
export endpoint="https://YOUR_ENDPOINT"
export num_gpus=1
export train_buckets="BUCKET_1 BUCKET_2"
export batchsize=32
export epochs=60
export object="CLASS_OF_OBJECT"
export output_bucket="OUTPUT_BUCKET"
export inference_data="PATH_TO_INFERENCE_DATA"

# Run Training
python -m torch.distributed.launch --nproc_per_node=$num_gpus \
train.py --use_s3 \
--train_buckets $train_buckets \
--endpoint $endpoint \
--object $object \
--batchsize $batchsize \
--epochs $((epochs / num_gpus))

# Copy Inference Data Locally
mkdir sample_data/inference_data
s3cmd sync s3://$inference_data sample_data/inference_data

# Run Inference
cd inference/
python inference.py \
--weights ../output/weights \
--data ../sample_data/inference_data \
--object $object

# Run Evaluation
cd ../evaluate
python evaluate.py \
--data_prediction ../inference/output \
--data ../sample_data/inference_data \
--outf ../output/ \
--cuboid

# Store Training and Evaluation Results
cd ../
s3cmd mb s3://$output_bucket
s3cmd sync output/ s3://$output_bucket
```

## Running the Entire Pipeline in One Command
To make running the entire pipeline easier on NGC, there is also a script `run_pipeline_on_ngc.py` that can run the entire pipeline with one command. Below is an example of an NGC run command that uses the script to run the entire pipeline:

```
# ADD YOUR S3 CREDENTIALS HERE
# (see "Adding S3 Credentials to NGC Jobs" section for more details)

python run_pipeline_on_ngc.py \
--num_gpus 1 \
--endpoint https://ENDPOINT \
--object YOUR_OBJECT \
--train_buckets YOUR_BUCKET \
--inference_bucket YOUR_INFERENCE_BUCKET \
--output_bucket YOUR_OUTPUT_BUCKET
```

## Building Your Own Training Container with Dockerfile
The easiest way to run this pipeline is with the existing container on NGC that is linked above. Alternatively, there is a `Dockerfile` in the Dope Training Repo . You can use this to build your own Docker image. This `Dockerfile` uses the PyTorch Container from NGC as the base image.
Then, assuming that you are in the directory where the `Dockerfile` is, you can run the command below. For additional information on building Docker images, see the official Docker guide .

```
cd docker
./get_nvidia_libs.sh

docker build -t nvcr.io/your-org/your-team/sample-image-dope-training:1.0 .
```
Here, `nvcr.io/your-org/your-team/sample-image-dope-training` is the name of the image we want to build and `1.0` is the tag. Use this naming convention to upload your image as a container to NGC.
You must manually copy the files over. Because the `visii` module that is used in `evaluate.py` requires drivers that are not in the default PyTorch container, you must run `get_nvidia_libs.sh`.
Then, to push this container to NGC, follow the same steps listed in the Pushing a Docker Container to NGC section above.

### Summary
This tutorial covered the following topics:

- How to generate synthetic data with Isaac Sim on the OVX clusters on NGC. Using these clusters enables you to scale up your synthetic data generation.

- How to train and evaluate a DOPE model on NGC using data that has been uploaded to an S3 bucket. This enables you to scale up your model training by training multiple models concurrently on clusters with multiple GPUs.
