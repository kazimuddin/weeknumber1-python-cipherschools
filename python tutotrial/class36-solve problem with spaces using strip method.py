# name = "     kazim     "
# dots = "...................."
# print(name+dots)
# print(name.lstrip())
# print(name.lstrip()+dots)
# print(name.rstrip()+dots)
# print(name.strip()+dots)
# name = "Kaz     im"
# print(name.replace(" ",""))
# print(name.replace(" ","")+dots)
name,ch = input("Enter your name and letter:-").split(",")
print(f"enter your name{len(name)}")
print(f"charecter count {name.strip().lower().count(ch.strip().lower())}")




