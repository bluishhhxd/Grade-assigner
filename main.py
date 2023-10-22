def data():
    while True:
        try:
            num_students = int(input("Number of students= "))
        except ValueError:
            print("Number of students can only be a numerical value, please try again.")
            continue
        for student in range(num_students):
            print(f"Student {student}:")
            while True:
                first_name = input("First name= ").capitalize().replace(" ",'')
                if not first_name:
                    print("First name can't be empty")
                else:
                    break
            last_name = input("Last name= ").capitalize().replace(" ", '')
            print("Input the marks of the student in the following subjects:")
            while True:
                try:
                    Maths=float(input("Maths (out of 80) = "))
                    if 0<=Maths<=80:
                        break
                    else:
                        print("Marks should be in range of 0 to 80.")
                except ValueError:
                    print("Please enter a numerical value.")
            while True:
                try:
                    English = float(input("English (out of 80) = "))
                    if 0 <= English <= 80:
                        break
                    else:
                        print("Marks should be in range of 0 to 80.")
                except ValueError:
                    print("Please enter a numerical value.")
            while True:
                try:
                    Physics = float(input("Physics (out of 70) = "))
                    if 0 <= Physics <= 70:
                        break
                    else:
                        print("Marks should be in range of 0 to 70.")
                except ValueError:
                    print("Please enter a numerical value.")
            while True:
                try:
                    Chemistry = float(input("Chemistry (out of 70) = "))
                    if 0 <= Chemistry <= 70:
                        break
                    else:
                        print("Marks should be in range of 0 to 70.")
                except ValueError:
                    print("Please enter a numerical value.")
            while True:
                try:
                    Comp_sci=float(input("Computer Science (out of 50) = "))
                    if 0<=Comp_sci<=50:
                        break
                    else:
                        print("Marks should be in range of 0 to 50.")
                except ValueError:
                    print("Please enter a numerical value.")
            Total = Maths + English + Physics + Chemistry + Comp_sci
            Percent = (Total/350)*100
            if Percent >=90:
                grade=("A+")
            elif 90>Percent>=80:
                grade=("A")
            elif 80>Percent>=70:
                grade=("B+")
            elif 70>Percent>=60:
                grade=("B")
            elif 60>Percent>=50:
                grade=("C")
            elif 50>Percent>=33:
                grade("D")
            else:
                grade=("F")

            if grade=="A+":
                Result = ("EXCELLENT!!, You have been promoted to next class.")
            elif grade=="A":
                Result = ("Very good work, You have been promoted to next class.")
            elif grade=="B+":
                Result = ("Good work, You have been promoted to next class.")
            elif grade=="B":
                Result = ("You have been promoted to next class.")
            elif grade=="C":
                Result = ("You have been promoted to next class.")
            elif grade=="D":
                Result = ("You have been promoted to next class.")
            else:
                Result = ("Work Hard next time, You have failed.")
            print("This is how the report card will look.")

            print(f"""Name: {first_name} {last_name}
            Marks in subjects:
            Maths= {Maths}/80
            English= {English}/80
            Physics= {Physics}/80
            Comp_Sci= {Comp_sci}/80
            Total= {Total}/350
            Percentage= {Percent}%
            Grade= {grade}
            Result= {Result}""")
            

while True:
    data()
    break
