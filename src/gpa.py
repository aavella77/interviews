# GPA calculator. Max is 4. class 3 credits. 6 classes. output = floating point with one decimal precision. Grades A or F. A=4, B=3 C=2 D=1 F=0, input list string "A,B,C, A"

def calculate_gpa(string):


	grades_dict = {
		"A": 4,
		"B": 3,
		"C": 2,
		"D": 1,
		"F": 0
	}
	
	grades = string.replace(" ","")
	grades = grades.split(",")
	if len(grades) != 6:
		print("Missing some grades")
		return
	
	sum = 0
	for grade in grades:
		if grade.isdigit():
			print("Error grade must be a letter")
			return
		sum = grades_dict[grade] + sum
	
	return sum/6
	
print(calculate_gpa("A,B,C,A,D,A"))
print(calculate_gpa("A,A,A,A,A,A"))	
print(calculate_gpa("B,B,B,B,B,B"))		
print(calculate_gpa("0,B,B,B,B,B"))	
print(calculate_gpa("0,B,B"))	
print(calculate_gpa("A,B,C,A,D, A"))	
