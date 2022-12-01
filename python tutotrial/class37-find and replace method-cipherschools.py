string = "kazim is dancer and he is a very good boy"
print(string.replace(" ","_"))
print(string.replace("is","was",1))
print(string.replace("is","was",4))
print(string.find("is"))
print(string.find("kazim"))
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1+1)
print(is_pos2)
