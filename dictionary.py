# dict = {
#   1: 'Python', 
#   2: 'dictionary', 
#   3: 'example'
# }
# print(dict)


# dictnaries={
#     'name':'tushar',
#     'age':22,
#     'address':'faridabad',
#     'contacts':1234267
# }
# print(dictnaries)


# Dict = {}
# print("Empty Dictionary: ")
# print(Dict)

# Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
# print("\nDictionary with the use of dict(): ")
# print(Dict)

# Dict = dict([(1, 'Geeks'), (2, 'For')])
# print("\nDictionary with each item as a pair: ")
# print(Dict)


# Dict = {1: 'Geeks', 2: 'For',
#         3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

# print(Dict)


Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)
