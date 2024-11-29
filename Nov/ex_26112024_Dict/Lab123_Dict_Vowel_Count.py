input_string = input("enter ur string\n")

vowel = "aeiou"

vowel_count = 0

for char in input_string:
    if char in vowel:
        vowel_count = vowel_count + 1

print(vowel_count)

