# Enter your code here
class calci:
    def __int__(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b

obj_1=calci
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
ch=int(input("enter your choice"))
if(ch==1):
    print(obj_1.add(a,b))
elif(ch==2):
    print(obj_1.sub(a,b))
elif(ch==3):
    print(obj_1.mul(a,b))
else:
    print(obj_1.div(a,b))
