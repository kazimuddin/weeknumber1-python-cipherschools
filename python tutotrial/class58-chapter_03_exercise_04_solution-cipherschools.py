# n  = input()
# s = int(n[0]) + int(n[1]) +int(n[2]) + int(n[3])
# print(s)
n = input("Enter a number:-") #length = 4 last index =3
total = 0 
i = 0 # int(n[0]) we are starting from 0 index na..
while i<len(n):
    total += int(n[i])
    i +=1
print(total)



