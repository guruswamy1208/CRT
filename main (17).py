class student_data:
    def __int__(self,name,roll,age,branch,cgpa):
        self.name=name
        self.roll=roll
        self.age=age
        self.branch=branch
        self.cgpa=cgpa
        self.marks_btech=marks_btech
        self.marks_10th=marks_10th
        self.marks_inter=marks_inter
    def display(name,roll,age,branch,cgpa):
        return f"name : {name} roll_number : {roll} age = {age}"
    
    def grade(cgpa):
        if(cgpa>9.5):
            return "excellent"
        elif(cgpa>7 and cgpa<9):
            return "good"
        elif(cgpa>5 and cgpa<7):
            return "average"
    def check_placement(marks_10th,marks_inter,marks_btech):
        if(marks_10th>60 and marks_btech>60 and marks_inter>60):
            return "you are eligible for placements"
        else:
            return "you are not eligible for placements"
    # creating object
student_1=student_data
student_2=student_data
    
print(student_1.display("bharath",21,22,"ece",9.0))
print(student_1.check_placement(89,78,98))
print(student_2.grade(9.7))
            