# Program - if age > 18 - allowed to vote
# else -> not allowed too

user_age = int(input("enter your age\n"))

if(user_age>18):
    print("yes you can vote")
else:
    print("no you can't vote")

print("yes u can vote" if user_age > 18 else "no u can't vote")