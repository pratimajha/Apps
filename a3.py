# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
 
# s = "Geeksforgeeks"
 
# print("The original string is : ", end="")
# print(s)
 
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))



# Function to reverse a string
# def reverse(string):
#     x = len(string)
#     string = [string[i] for i in range(len(string)-1, -1, -1)]
#     return "".join(string)
 
# s = "Geeksforgeeks"
 
# print("The original string  is : ", s)
 
# print("The reversed string(using reversed) is : ", reverse(s))

#Queue concept in class

# class queue:
#     def __init__(self):
#         self.values = []
#     def enqueue(self, x):
#         self.values.append(x)
#     def dequeue(self):
#         front = self.values.pop(0)
#         # self.values = self.values[1:]
#         return front

# q1 = queue()
# q1.enqueue(10)
# q1.enqueue(20)
# q1.enqueue(40)
# q1.enqueue(64)
# print(q1.values)
# print(q1.dequeue())
# print(q1.values)

#Stack concept in class

# class stack:
#     def __init__(self):
#         self.values = []
#     def enqueue(self,x):
#         self.values = [x] + self.values
#     def dequeue(self):
#         front = self.values.pop(0)
#         return front

# q1 = stack()
# q1.enqueue(10)
# q1.enqueue(12)
# q1.enqueue(18)
# q1.enqueue(60)

    

# print(q1.values)
# print(q1.dequeue())
# print(q1.values)

