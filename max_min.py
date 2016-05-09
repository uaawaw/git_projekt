a1 = int(input())
a2 = int(input())
a3 = int(input())
print (a1,a2,a3)
print (a1*a2*a3)
print (a1+a2-a3)

if (a1>=a2 and a1>=a3) and (a2>=a3):
    print ('\n',a1,'\n',a3,'\n',a2)
elif (a1>=a2 and a1>=a3) and (a3>=a2):
    print ('\n',a1,'\n',a2,'\n',a3)
elif (a2>=a1 and a2>=a3) and (a1>=a3):
    print ('\n',a2,'\n',a3,'\n',a1)
elif (a2>=a1 and a2>=a3) and (a3>=a1):
    print ('\n',a2,'\n',a1,'\n',a3)
elif (a3>=a1 and a3>=a2) and (a2>=a1):
    print ('\n',a3,'\n',a1,'\n',a2)
elif (a3>=a1 and a3>=a2) and (a1>=a2):
    print ('\n',a3,'\n',a2,'\n',a1)
