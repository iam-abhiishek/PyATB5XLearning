# Tuple
# Collection of Items
# ()
# Immutable

my_tuple = (1, 2, 4, 9, 3)
print(my_tuple)

# my_tuple[1] = 10 TypeError: 'tuple' object does not support item assignment

shopping_list_wife = ["bread", "butter", "paneer"]
shopping_list_wife[2] = "milk"
print(shopping_list_wife)

# Real example of Tuples
my_tuple = ("tta.com", "sdet.live")
my_api_list = list(my_tuple)
print(my_api_list)
# my_tuple[0] = "abc.com" # TypeError: 'tuple' object does not support item assignment

# Real case, where we Tuples
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])
