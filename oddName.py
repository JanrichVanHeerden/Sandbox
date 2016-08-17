"""Janrich van Heerden"""
name = input("Enter your name")
while name == "":
        name = input("Enter a NAME")
char_list = name
count = 1
for each in list(char_list):
    if count % 2 != 0:
        print(each)
        count+=1
    else:
        count+=1
