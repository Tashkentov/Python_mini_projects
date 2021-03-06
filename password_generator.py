import random
DIGITS = "0123456789" # 1 0 +
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz" #l i o + 
UPPERCASE_LETTERS = "ABCDEFGHIJKMNPOQRSTUVWXYZ" # L O +
PUNCTUATION = "!#$%&*+-=?@^_"

def generate_password(length, chars):
    i = 0
    password = ""
    for i in range(length - 1):
        password += chars[random.randint(0, len(chars) - 1)]

    print(password)

chars = " "
print("Number of passwords to generate :")
count_pass = int(input())

print("The length of one password :")
length_pass = int(input()) - 1

print("Do you want to include digits 0123456789 ? (y = yes, n = no)")
if input().lower() == "y":
    chars = chars + DIGITS

print("Do you want to include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y = yes, n = no)")
if input().lower() == "y":
    chars = chars + UPPERCASE_LETTERS

print("Do you want to include lowercase letters abcdefghijklmnopqrstuvwxyz? (y = yes, n = no)")
if input().lower() == "y":
    chars = chars + LOWERCASE_LETTERS

print("Do you want to include the characters! # $% & * + - =? @ ^ _? (y = yes, n = no)")
if input().lower() == "y":
    chars = chars + PUNCTUATION

for i in range(count_pass):
    generate_password(length_pass, chars)
