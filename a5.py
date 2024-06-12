# import sys

# def my_gen(num):
#     value = 0
#     while value<num:
#         if value%2==0:
#             yield value
#         value+= 1

# x = my_gen(50)
# print(list(x))

# user_input = "Hello"

# str = user_input.strip()

# count = 0
# duplicate = []

# for i in str:
#     count = 0
#     if i in str:
#         count = count +1
#         duplicate.extend([i,count])

# print(duplicate)

user_input = input("Enter your string: ")
str = user_input.strip()
count = 0
duplicate = []
index = 0

for i in str:
    count = 0
    if i not in duplicate:
        count = count+1
        duplicate.extend([i,count])
        index+=1
    else:
        if i in duplicate:
            count = count+1
            duplicate[index+1] = count
            

print(duplicate)

