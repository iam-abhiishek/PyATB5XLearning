my_dict = {
    "name" : "Abhishek",
    "age" : 34,
    "role" : "SDET",
    "experience" : 1
}

print(my_dict["age"])

my_dict["age"] = 43
print(my_dict)

del my_dict["age"]
print(my_dict)
print(type(my_dict))

for key,value in my_dict.items():
    print(key,"->",value)

print("age" in my_dict)
print("experience" in my_dict)