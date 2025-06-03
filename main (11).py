      #multilevel inheritance
class grandfather:
    def grandfather_method():
        return "this is grand father method"
class father:
    def father_method():
        return "this is father method"
class child(grandfather,father):
    def child_method():
        return "i have properties of grandfather and father"
grandfather_object=grandfather
father_object=father
child_object=child
print(grandfather_object.grandfather_method())
print(father_object.father_method())
print(child_object.child_method())
print(child_object.grandfather_method())
print(child_object.father_method())