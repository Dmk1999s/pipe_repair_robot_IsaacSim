<!-- source: py/api/structisaacsim_1_1robot_1_1schema_1_1custom_1_1hash.html | title: hash — Isaac Sim -->

# hash
Fully qualified name: `isaacsim::robot::schema::custom::hash`
template<typenameE>
structhash

Hash function object for enum types.
Provides a hash function for enum types by casting them to size_t. This allows enums to be used as keys in unordered containers.
Template Parameters:
E – The enum type to provide hashing for

Public Functions
inlinesize_toperator()(constE &e)const

Hash function operator for enum values.
Converts an enum value to its underlying integer representation and casts it to size_t for use as a hash value.
Parameters:
e – [in] The enum value to hash

Returns:
size_t Hash value for the enum
