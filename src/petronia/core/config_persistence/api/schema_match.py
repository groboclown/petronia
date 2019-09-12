

#
#
#
# def find_mismatch(schema: PersistTypeSchema, data: PersistType) -> Sequence[Sequence[Union[str, int]]]:
#     return _find_mismatch(schema, data)
#
#
# def _find_mismatch(
#         prefix: Sequence[Union[str, int]], schema: _GenericPersistSchema, data: _GenericPersistType
# ) -> Sequence[Sequence[Union[str, int]]]:
#     ret: List[Sequence[Union[str, int]]] = []
#     if isinstance(schema, PersistTypeSchemaItem):
#         if (
#                 (schema.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__STR and not isinstance(data, str) and data is not None) or
#                 (schema.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__BOOL and not isinstance(data, bool) and data is not None) or
#                 (schema.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT and not isinstance(data, float) and data is not None) or
#                 (schema.type_name == PERSISTENT_TYPE_SCHEMA_TYPE__INT and not isinstance(data, int) and data is not None)
#         ):
#             path = list(prefix)
#             path.append(schema.type_name)
#             ret.append(path)
#         return ret
#     if isinstance(schema, dict):
#         if not isinstance(data, dict):
#             path = list(prefix)
#             path.append('dict')
#             return [path]
#         # hmm...  should be a matcher...
#         for key, val in schema.items():
#
#             path = list(prefix)
#             path.append(key)
#             ret.extend(_find_mismatch(path, val, data.get(key, None)))
#         return ret
#     if isinstance(schema, Sequence):
#         # Interesting one.
#         if isinstance(data, str) or isinstance(data, dict) or not isinstance(data, Iterable):
#             path = list(prefix)
#             path.append('list')
#             return [path]
#         idx = 0
#         for idx in range(len(data)):
#             path = list(prefix)
#             path.append(idx)
#             ret.extend(_find_mismatch(path, schema[idx], ))
