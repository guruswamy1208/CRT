# Enter your code here
class student:
    def __init__(self,marks):  #default constructor
        self.marks=marks
        self.__marks=marks     # private
    def getter(self):
        return self.__marks
    def setter(self,marks):
        self.__marks=marks

s1=student(78)
# set the data:
s1.setter(78)
# get the data
ans=s1.getter()
print(ans)
        