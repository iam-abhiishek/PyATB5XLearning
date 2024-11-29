dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2}

missing_keys = dict1.keys() - dict2.keys()
# missing_values = set(dict1.values() - dict2.values())
print(missing_keys)
# print(missing_values)


# # Sort a dictionary by its values in descending order
# my_dict = {"a": 3, "b": 1, "c": 2}
#
# # {b: 1 , c: 2 , a :3}