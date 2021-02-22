temp="Hello <<UserName>>, How are you?"
name=input("Enter username\n")
temp=temp.replace("<<UserName>>",name)
print(temp)
