student_details1 = {
    "name" : "ballu",
    "age" : 30,
    "work" : "developer",
    "address" : {
        "city" : "mars",
        "pincode" : 111222
    }
}

student_details2 = {
    "name" : "matru",
    "age" : 25,
    "work" : "cricketer",
    "address" : {
        "city" : "mars",
        "pincode" : 111333
    }
}

# print(student_details1, student_details2)
student_list = [student_details1, student_details2]
# print(student_list)
# print(student_list[0])
# print(student_list[1])
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["address"]["city"])