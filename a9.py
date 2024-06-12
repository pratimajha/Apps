str = "Hello World"

x = str.split()

# print(x)

rstr = list(reversed(x))
print(rstr)

total = ""

for i in rstr:
    total = total + " " +i

print(total)


    
