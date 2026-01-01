from collections import defaultdict



class School:
    roll_number=190000
    biodata=defaultdict(list)


class Student():
    @classmethod
    def register_student(cls,name,age,marks):
        School.roll_number+=1
        School.biodata[School.roll_number]={'name':name,'age':age,'marks':marks}
        print(f"Student registered! New Rno: {School.roll_number}")

    @classmethod
    def get_details(cls,rno):
        if rno in School.biodata:
            result=School.biodata[rno]
            print(f"Rollnumber {rno}\nName:{result['name']}\nAge:{result['age']}\nMarks:{result['marks']}\n")
        else:
            print("Student records not found")

    @classmethod
    def get_all_student_details(cls):
        result=School.biodata
        for i,res in enumerate(result,start=1):
            print(f"Student #{i}")
            print("Name ",result[res]['name'])
            print("Rno ",res)
            print("Age ",result[res]['age'])
            print("Marks ",result[res]['marks'])


    @classmethod
    def calc_class_avg(cls):
        result=Student.biodata
        tot_avg=0
        avg_each_student={}
        for res in result:
            marks = result[res]['marks'][1:-1]
            marks = marks.split(",")
            marks = [int(i) for i in marks]
            avg_one_student=sum(marks) / len(marks)
            avg_each_student[result[res]['name']]=avg_one_student
            tot_avg+=avg_one_student

        return ["{:.2f}".format(tot_avg/len(Student.biodata)),avg_each_student]

    @classmethod
    def find_class_topper(cls):
        result=Student.calc_class_avg()[1]
        max_holder = ""
        max_marks=float('-inf')
        for d in result:
            if result[d] > max_marks:
                max_marks = result[d]
                max_holder = d
        return max_holder



while True:
    print("1.New Admission\n2.Get Details\n3.Get all student details\n4.Find average\n5.Find class topper\n6.Exit")
    option=int(input())
    if option==1:
        print("Enter details with space seperated name,age,marks")
        name,age,marks=input().split()
        Student.register_student(name,age,marks)
    if option==2:
        print("Enter roll_number: ")
        rno=int(input())
        Student.get_details(rno)
    if option==3:
        Student.get_all_student_details()
    if option==4:
        print("Class Average ",Student.calc_class_avg()[0])
    if option==5:
        print("Class Topper: ",Student.find_class_topper())
    if option==6:
        break


