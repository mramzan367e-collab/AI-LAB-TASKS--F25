
class rulebased:
    def __init__(self, score, doucment, attendance, marks):
        self.score = score
        self.doucment = doucment
        self.attendance = attendance
        self.marks = marks

    def show(self):
        if (self.score >= 70 and
            self.doucment == "complete" and
            self.attendance >= 75 and
            self.marks >= 60):
            return "Pass"
        else:
            return "Fail"


print("Enter your score:")
score = int(input())

print("Enter your document status (complete/incomplete):")
doucment = input().lower()

print("Enter your attendance:")
attendance = int(input())

print("Enter your marks:")
marks = int(input())

obj = rulebased(score, doucment, attendance, marks)

print("Overall:", obj.show())
