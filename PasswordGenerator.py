import random

upcase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowcase_letters = upcase_letters.lower()
dgt="0123456789"
symbs="!@#$%^&*()_-+=[]:;<,>.?/\|"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += upcase_letters
if lower:
    all += lowcase_letters
if nums:
    all += dgt
if syms:
    all += symbs

len_str= input("Enter the length:")
length= int(len_str)
amnt_str= input("Enter how many you want:")
amount = int(amnt_str)

for x in range(amount):
    password = "".join(random.sample(all,length))
    print(password)
