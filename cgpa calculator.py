#Program to calculate CGPA
print("WELCOME TO THE UNIVERSITY OF IBADAN, THIS PROGRAM CALCULATES CGPA FOR 1ST SEMESTER")
name= input("enter name(Begin with Surname): ")
n= name.upper()
print (n)
Department= input("Enter University of Ibadan Distance Learning Centre Department: ")

if Department=='Computer' and Department=='Computer Science' and Department=='computer' and Department=='computer science':
	print("fill in the grade of the courses below: ")
	csc102= int(input("enter CSC102 grade: "))
	print("CSC102 is a 4 unit course")
	if csc102>=69 and csc102<=101:
		A= 4
		A1= 4 * 4
		print("Your grade is A, and your grade point is 16")
	elif csc102>=59 and csc102<=70:
		B= 3
		B1= 3 * 4
		print("Your grade is B, and your grade point is 12")
	elif csc102>=49 and csc102<=60:
		C= 2
		C1= 2 * 4
		print("Your grade is C, and your grade point is 10")
	elif csc102>=44 and csc102<=50:
		D= 1
		D1= 1 * 4
		print("Your grade is D, and your grade point is 4")
	elif csc102>=-1 and csc102<=45:
		E= 0
		E1= 0 * 4
		print("Your grade is D and your grade point is 0")
	else: print("\033[1;31;40m, Enter valid score")
	mat111= int(input("enter MAT111 grade: "))
	if mat111>=69 and mat111<=101:
		A2= 4
		A3= 4 * 4
		print("Your grade is A, and your grade point is 16")
	elif mat111>=59 and mat111<=70:
		B2= 3
		B3= 3 * 4
		print("Your grade is B, and your grade point is 12")
	elif mat111>=49 and mat111<=60:
		C2= 2
		C3= 2 * 4
		print("Your grade is C, and your grade point is 10")
	elif mat111>=44 and mat111<=50:
		D2= 1
		D3= 1 * 4
		print("Your grade is D, and your grade point is 4")
	elif mat111>=-1 and mat111<=45:
		E2= 0
		E3= 0 * 4
		print("Your grade is D and your grade point is 0")
	else: print("\033[1;31;40m, Enter valid score")
	mat121= int(input("enter MAT121 grade: "))
	if mat121>=69 and mat121<=101:
		A4= 4
		A5= 4 * 4
		print("Your grade is A, and your grade point is 16")
	elif mat121>=59 and mat121<=70:
		B4= 3
		B5= 3 * 4
		print("Your grade is B, and your grade point is 12")
	elif mat121>=49 and mat121<=60:
		C4= 2
		C5= 2 * 4
		print("Your grade is C, and your grade point is 10")
	elif mat121>=44 and mat121<=50:
		D4= 1
		D5= 1 * 4
		print("Your grade is D, and your grade point is 4")
	elif mat121>=-1 and mat121<=45:
		E4= 0
		E5= 0 * 4
		print("Your grade is D and your grade point is 0")
	else: print("\033[1;31;40m, Enter valid score")
	sta115= int(input("enter STA115 grade: "))
else:
	print("\033[1;31;40m, Invalid Department")
