class Student:

    def __init__(self, name, father_name, nationality, city, obtained_marks, total_marks):
        self.name = name
        self.father_name = father_name
        self.city = city
        self.nationality = nationality
        self.obtained_marks = obtained_marks
        self.total_marks = total_marks

    def personal_detail(self):
        print("INFORMATION FOR SHERAZ")
        print("NAME        : ", self.name)
        print("FATHER NAME : ", self.father_name)
        print("CITY        : ", self.city)
        print("NATIONALITY : ", self.nationality)
        print("MARKS       : ", self.obtained_marks)
        print("TOTAL       : ", self.total_marks)
        print("GRADE       : ", self.calculate_grade())
        print()

    def calculate_grade(self):
        if 50 <= self.obtained_marks < 75:
            return "C"
        elif 75 <= self.obtained_marks < 90:
            return "B"
        elif 90 <= self.obtained_marks < 100:
            return "A"
        return "F"
