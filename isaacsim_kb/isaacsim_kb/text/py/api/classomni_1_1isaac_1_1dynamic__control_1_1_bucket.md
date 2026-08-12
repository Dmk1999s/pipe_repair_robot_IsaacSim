<!-- source: py/api/classomni_1_1isaac_1_1dynamic__control_1_1_bucket.html | title: Bucket — Isaac Sim -->

# Bucket
Fully qualified name: `omni::isaac::dynamic_control::Bucket`
template<classT>
classBucket

A container for managing objects with unique IDs.
Provides a way to store, retrieve, and remove objects using unique IDs. Takes ownership of the objects and manages their lifetime.
Template Parameters:
T – The type of objects stored in the bucket

Public Functions
inlineuint32_tadd(std ::unique_ptr<T >&&obj)

Adds an object to the bucket.
Takes ownership of the object and assigns it a unique ID
Parameters:
obj – [in] The object to add, transferred as an rvalue reference

Returns:
The unique ID assigned to the object

inlineT *get(uint32_tid)const

Gets an object by its ID.
Returns a pointer to the object if found, or nullptr if not found
Parameters:
id – [in] The ID of the object to retrieve

Returns:
Pointer to the object, or nullptr if not found

inlinevoidremove(uint32_tid)

Removes an object by its ID.
If the object is found, it is removed and destroyed
Parameters:
id – [in] The ID of the object to remove

inlinevoidclear()

Clears all objects from the bucket.
Removes and destroys all objects
