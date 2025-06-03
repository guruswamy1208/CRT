#hybrid inheritance
class grandfather:
    def grandfather_method():
        return "this is grand father method"
class father:
    def father_method():
        return "this is father method"
class mother:
    def mother_method():
        return "this is mother method"
class child(grandfather,father ,mother):
    def child_method():
        return "i have properties of grandfather,father and mother"
grandfather_object=grandfather
father_object=father
mother_object=mother
child_object=child
print(grandfather_object.grandfather_method())
print(father_object.father_method())
print(mother_object.mother_method())
print(child_object.child_method())
print(child_object.grandfather_method())
print(child_object.father_method())
print(child_object.mother_method())