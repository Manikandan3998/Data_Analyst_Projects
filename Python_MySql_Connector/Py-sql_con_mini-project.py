import mysql.connector
from tabulate import tabulate

cnx = mysql.connector.connect(
    host="localhost", user="root", password="Scorpio5000@", port=3306, database="sms"
)


def insert():
    while True:
        try:
            st_id = int(input("Enter student id :  "))
            break
        except ValueError:
            print("Student ID must be only in numbers")

    student_name = input("Enter the name of the student :  ")

    Gender = input("Enter male/female :  ")
    while True:
        try:
            class_ = int(input("Enter the class of the student :  "))
            break
        except ValueError:
            print("The class should be a numeric value")

    Department = input("Enter the Department of the student :  ")

    while True:
        try:
            rank = int(input("Enter the Rank of the student :  "))
            break
        except ValueError:
            print("The rank should be in numbers")
    while True:
        try:
            attendance_percentage = int(input("Enter the attendance percentage :  "))
            break
        except ValueError:
            print("The attendance Percentage should be in numbers only")

    first_language = input("Enter the first language of the student :  ")

    res = cnx.cursor()
    sql = "insert into student_info (st_id,student_name,Gender,class_,Department,rank_,attendance_percentage,first_language) values(%s,%s,%s,%s,%s,%s,%s,%s)"

    try:
        res.execute(
            sql,
            (
                st_id,
                student_name,
                Gender,
                class_,
                Department,
                rank,
                attendance_percentage,
                first_language,
            ),
        )
    except:
        print("Please check the student ID for the duplicate values and retry")
        insert()
    cnx.commit()
    print()
    print("record added successfully")
    select()


def select():
    res = cnx.cursor()
    sql = "select * from student_info"
    res.execute(sql)
    result = res.fetchall()
    print()
    print(
        tabulate(
            result,
            headers=[
                "ID",
                "NAME",
                "GENDER",
                "CLASS",
                "DEPARTMENT",
                "RANK",
                "ATTENDANCE %",
                "FIRST LANGUAGE",
            ],
        )
    )


def update():
    print("which field you want to update?")
    print("1)Name")
    print("2)Gender")
    print("3)Class")
    print("4)Department")
    print("5)Rank")
    print("6)Attendance %")
    print("7)First language")
    upd = int(input("Enter the number of the requred field to be updated :  "))
    if upd == 1:
        res = cnx.cursor()
        sql = "update student_info set student_name = %s where st_id = %s"
        while True:
            try:
                st_id = input(
                    "Enter the id of the student, whose name you want to change :  "
                )
                break
            except ValueError:
                print("The student ID has numeric values only")
        new_student_name = input("Enter the new name of the student :  ")
        res.execute(sql, (new_student_name, st_id))
        cnx.commit()
        select()
        print("Name has been updated successfully")

    if upd == 2:
        res = cnx.cursor()
        sql = "update student_info set gender = %s where where st_id =%s"
        while True:
            try:
                st_id = input(
                    "Enter the id of the student, whose gender you want to change :  "
                )
                break
            except ValueError:
                print("The student ID has numeric values only")

        gender = input("Enter the Gender :  ")
        res.execute(sql, (gender, st_id))
        cnx.commit()
        select()
        print("Gender has been updated succesfully")
    if upd == 3:
        res = cnx.cursor()
        sql = "update student_info set class_= %s where st_id =%s"
        while True:
            try:
                st_id = input(
                    "Enter the id of the student, whose class you want to change :  "
                )
                break
            except ValueError:
                print("The student ID has numeric values only")
        while True:
            try:
                cls = int(input("Enter the Class :  "))
                break
            except ValueError:
                print("The student class has numeric values only")

        res.execute(sql, (cls, st_id))
        cnx.commit()
        select()
        print("class has been updated successfully")

    if upd == 4:
        res = cnx.cursor()
        sql = "update student_info set Department = %s where where st_id =%s"
        while True:
            try:
                st_id = input(
                    "Enter the id of the student, whose Department you want to change :  "
                )
                break
            except ValueError:
                print("The student ID has numeric values only")
        dept = input("Enter the Department :  ")
        res.execute(sql, (dept, st_id))
        cnx.commit()
        select()
        print("The Department name has been updated successfully")

    if upd == 5:
        res = cnx.cursor()
        sql = "update student_info set rank_ = %s where where st_id =%s"
        while True:
            try:
                st_id = input(
                    "Enter the id of the student, whose rank you want to change :  "
                )
                break
            except ValueError:
                print("The student ID has numeric values only")

        while True:
            try:
                rank_ = int(input("Enter the rank :  "))
                break
            except ValueError:
                print("The student rank has numeric values only")
        res.execute(sql, (rank_, st_id))
        cnx.commit()
        select()
        print("The Rank has been updated successfully")

    if upd == 6:
        res = cnx.cursor()
        sql = "update student_info set attendance_percentage = %s where where st_id =%s"
        while True:
            try:
                st_id = input(
                    "Enter the id of the student, whose attendance percentage you want to change :  "
                )
                break
            except ValueError:
                print("The student ID has  numeric values only")
        while True:
            try:
                ap = int(input("Enter the attendance percentage :  "))
                break
            except ValueError:
                print("The student attendance percentage has numeric values only")

        res.execute(sql, (ap, st_id))
        cnx.commit()
        select()
        print("The Attendance percentage has been updated successfully")

    if upd == 7:
        res = cnx.cursor()
        sql = "update student_info first_language = %s where where st_id =%s"
        while True:
            try:
                st_id = input(
                    "Enter the id of the student, whose First language you want to change :  "
                )
                break
            except ValueError:
                print("The student ID has numeric values only")
        fl = input("Enter the First language :  ")
        res.execute(sql, (fl, st_id))
        cnx.commit()
        select()
        print("The first language has been updated successfully")


def delete():
    while True:
        try:
            st_id = input("Enter the id of the student to be deleted :  ")
            break
        except ValueError:
            print("The student ID has only numeric values only")
    res = cnx.cursor()
    sql = "delete from student_info where st_id = %s"
    res.execute(sql, (st_id,))
    cnx.commit()
    print()
    select()
    print("Record has been deleted successfully")


while True:
    print()
    print("Type the number corresponding to the functions you want to perform")
    print("1.Insert Record")
    print("2.Update Record")
    print("3.Delete Record")
    print("4.Select Record")
    print("5.Exit")
    print()
    choise = int(input("Enter your choise:  "))
    if choise == 1:
        insert()
    elif choise == 4:
        select()
    elif choise == 2:
        update()
    elif choise == 3:
        delete()
    else:
        print("Invalid option.....!!!")
