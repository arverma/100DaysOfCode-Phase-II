class Student:
    full_marks = 300

    def __init__(self, m1, m2, m3):
        self.mark_sub1 = m1
        self.mark_sub2 = m2
        self.mark_sub3 = m3

    @classmethod
    def get_full_marks(cls):
        return cls.full_marks

    def sum_all_marks(self):
        return self.mark_sub1 + self.mark_sub2 + self.mark_sub3

    def get_grade(self):
        full_marks = self.get_full_marks()
        total_marks_secured = self.sum_all_marks()
        percentage = self.calculate_percentage(total_marks_secured, full_marks)
        return "A" if percentage > 80 else "F"

    @staticmethod
    def calculate_percentage(marks_secured, full_marks):
        return marks_secured*full_marks/full_marks*100


aman = Student(90, 60, 99)
print(aman.get_grade())
# Instance method can not be called through class
# print(Student.get_grade())

# Class method
print(aman.get_full_marks())
print(Student.get_full_marks())

# Static method can not be called through obj or class
# print(Student.calculate_percentage())
# print(aman.calculate_percentage())
