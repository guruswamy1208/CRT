#single inheritance:
class father:
    def father_method():
        return "this is father method"
class mother:
    def mother_method():
        return "this is mother method"
class child(father,mother):
    def child_method():
        return "i have properties of mother and father"
father_object=father
mother_object=mother
child_object=child
print(father_object.father_method())
print(mother_object.mother_method())
print(child_object.child_method())
print(child_object.father_method())
print(child_object.mother_method())