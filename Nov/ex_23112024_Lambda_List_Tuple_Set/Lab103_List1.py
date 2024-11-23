list_ex = [1, 'hello', 22.45]

# Indexing
print("element at the index 0 - ", list_ex[0])
print("element at the index 1 - ", list_ex[1])
print("element at the index 2 - ", list_ex[2])
# print("element at the index 3 - ", list_ex[3])

# append() - # Append object to the end of the list.
list_ex.append(234)
print(list_ex)

# extend() - Append a new list
list_ex.extend(['ok', False, 'bye',5,3,9])
print(list_ex)

# insert()
list_ex.insert(1,'abhishek')
print(list_ex)

for item in list_ex:
    # a <= len(item)
    print('element at the index',item)

print(len(list_ex))

list_ex.insert(0,0)
print(list_ex)

# remove()
list_ex.remove(0)
print(list_ex)

list_ex[1] = 'Ballu'
print(list_ex)

list_ex.insert(1,2)
print(list_ex)
print(len(list_ex))

new_list = list_ex.copy()
print(new_list)
new_list.remove('Ballu')
new_list.remove('hello')
new_list.remove('ok')
new_list.remove(False)
new_list.remove('bye')
print(new_list)
new_list.sort()
print(new_list)
