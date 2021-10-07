#Joseph Powell IV
#CIS 225-01
#16th Oct. 2018
#Letter Grade


def numeric_input():
    score = float(input("What's the numeric grade >> "))
    return score

def processing(score):
    try:
        if score > 90.0:
            print("A")
        elif 80.0 <= score < 90.0:
            print("B")
        elif 70.0 <= score < 80.0:
            print("B")
        elif 60.0 <= score < 70.0:
            print("C")
        elif 0.0 <= score < 60.0:
            print("F")
        return score
    except:
        print("Please enter a number!")

def output(grade):
    print(round(grade))

def main():
    numeric_grade = numeric_input()
    letter_grade = processing(numeric_grade)
    output(letter_grade)

main()





'''def numeric_input():
    return 88

def processing(score):
    return 'B'

def output(grade):
    print(grade)

def main():
    numeric_grade = numeric_input()
    letter_grade = processing(numeric_grade)
    output(letter_grade)

main()'''
    

'''def main():

    #numeric_input
    n = float(input("What's the numeric grade >> "))
    
    #processing
    grade = n


    #output
    if grade > 90.0:
        print("A")
    elif 80.0 <= grade < 90.0:
        print("B")
    elif 70.0 <= grade < 80.0:
        print("B")
    elif 60.0 <= grade < 70.0:
        print("C")
    elif 0.0 <= grade < 60.0:
        print("F")
    
main()'''

'''def main():
	try:
		#input
		number = float(input("Enter a Number: "))
		
		#process
		answer = math.sqrt(number)
	
		#output
		print(answer)
	except valueError:
		print("Please input number!")
	except: 
		print("Something bad happened.")
	
main()'''

'''def main():
    var = numeric_input()
    ans = processing(var)
        output(ans)
main()'''



'''#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: <60

input = arcpy.GetParameterAsText(0)
score = int(input)
if score > 90:
    print "A"
elif 80 =< score < 90:
    print "B"
elif 70 =< score < 80:
    print "B"
elif 60 =< score < 70:
    print "C"
else:
    print "F"'''


'''def grader(testOne, testTwo, testThree, finalExam):
    first = testOne * .20
    second = testTwo * .20
    third = testThree * .20
    fourth = finalExam *.40
    finalGrade = first + second + third + fourth
    return finalGrade

def ?? (??):
    if grade >= 90 and <= 100:
        return("You received an A")

    elif grade >= 80 and < 90:
        return("You received a B")

    elif grade >= 70 and < 80:
        return("You received a C")

    elif grade >= 60 and < 70:
        return("You received a D")

    else grade < 60:
        return("Sorry, you received an F")

print(testOne, testTwo, testThree, finalExam) #will replace with values'''
