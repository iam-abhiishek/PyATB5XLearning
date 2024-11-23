num = int(input('enter a num\n'))
# def even_odd(a):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#
# even_odd(num)

check_even_odd = lambda num : 'even' if num % 2 == 0 else 'odd'
print(check_even_odd(num))