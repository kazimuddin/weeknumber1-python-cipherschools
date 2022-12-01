n = input("Enter your name :")
# kazim
# name.count("k") ,name.count(name[0])=1
# name.count("a") ,name.count(name[1])=2
# name.count("z") ,name.count(name[2])=1
# name.count("i") ,name.count(name[3])=1
# name.count("m") ,name.count(name[4])=1

# output
# k : 1
# a : 1
# z : 1
# i : 1
# m : 1
# i = 0
# while i<len(n):
#     print(f"{n[i]}  : {n.count(n[i])}")
#     i +=1
temp_var =""
i = 0
while i <len(n):
    if n[i] not in temp_var:
        temp_var += n[i]
        print(f"{n[i]}  : {n.count(n[i])}")
    i +=1





