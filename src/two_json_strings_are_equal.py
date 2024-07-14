# Given 2 json srtings, write a function to compare them.
#
# The function should return True if the dictionaries are equal, False otherwise.

# Plan:
# 1. Parse the JSON strings into dictionaries using the json module.
# 2. Compare the dictionaries for equality.
# 3. Return the result of the comparison.


import json

def are_json_equal(json1, json2):
	dict_1 = json.loads(json1)
	dict_2 = json.loads(json2)
	return dict_1 == dict_2

print(are_json_equal('{"1": 2, "2": 3, "3": 4}',
                     '{"1": 2, "2": 3, "3": 5}'))
print(are_json_equal('{"1": 2, "2": 3, "3": 4}',
                     '{"1": 2, "2": 3, "3": 4}'))
print(are_json_equal('{"1": 2, "2": 3, "3": 4}',
                     '{"1": 2, "2": 3, "2": 4}'))
print(are_json_equal('{"speeds": [10,12,13], "1": 2, "2": 3, "3": 4}',
                     '{"speeds": [10,12,13], "1": 2, "2": 3, "3": 4}'))
print(are_json_equal('{"speeds": [10,12,13], "1": 2, "2": 3, "3": 4}',
                     '{"speeds": [11,12,13], "1": 2, "2": 3, "3": 4}'))
print(are_json_equal('{"speeds": [10,12,14], \
"name": "Alejandro", \
"Age": 52, \
"1": 2, "2": 3, "3": 4}', \
                     '{"speeds": [10,12,13], "name": "Alejandro", "Age": 52,  "1": 2, "2": 3, "3": 4}'))
