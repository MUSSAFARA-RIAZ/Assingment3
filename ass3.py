# Q1. Write a Python program to print the following string in a specific format (see the Output)
print("Twinkle, twinkle, little star ")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star ")
print("\tHow I wonder what you are!")
# Q3 Write a python program to display the current date and time
import datetime
a=datetime.datetime.now()
print("Current date and time : ")
print(a.strftime("%Y-%m-%d %H:%M:%S"))

# Q3 Write a python program to get the python version using 
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# Q4 Write a python program whicha cc[pet the radius of the circle from the user and compute its area
r=int(input("Enter the radius of the circle  "))
pie=3.142
Area=pie*r**2
print("the area of the circle is  ",Area)
#Q5Write a python program which accept the user first and last name and print them in reverse order with
##a space between
firstname=input("Enter your first name  ")
lastname=input("Enter your lastname  ")
print(lastname +"\t"+ firstname )
#Q6 Write a python program which takes two input from the user and print them addition
a=int(input("Enter your first number  "))
b=int(input("Enter your second number  "))
sum=a+b
print("The sum of two number is ",sum)
#Q7 Write a python program which takes five input from the user for different subject marks total it 
# and generate thier marksheet
calculus=int(input("Enter the marks of calculus  "))
DSA=int(input("Enter the marks of Dsa  "))
chinese=int(input("enter the marks of chinese  "))
Sre=int(input("enter the marks of software requirement  "))
accounting=int(input("enter the marks of accounting  "))
Total_marks=500
obtained_marks=calculus+DSA+Sre+chinese+accounting
percentage=(obtained_marks*100/Total_marks)
if(percentage>=80 and percentage<=100):
    print("Your grade is A+")
elif (percentage>=70 and percentage<80):
    print("your grade is A")
elif (percentage>=60 and percentage<70):
    print("your grade is B")
elif (percentage>=50 and percentage<59):
    print("your grade is C")
elif (percentage>=40 and percentage<49):
    print("your grade is D")
elif(percentage>=33 and percentage<39):
    print("your grade is E")
elif(percentage>100 and percentage<0):
    print("Invalid input")
else:
    print("your grade is F")    
# Q8 Write a python program which takes input from the user and identify that the number is even or odd
number=int(input("Enter the number  "))
if(number%2==0):
    print(number ," This number is even")
else:
    print(number," This number is odd ")
# Q9 Write a python program to print the length of the list
list=[12,78,45,98,100]
print(len(list))
# Q10 Write a python program to sum alll the numeric items in thelist
list=[10,20,30,40,50]
sum=0
for i in list:
    sum+=i
print(sum)
# Q11 Write a python program to get the largest number from a numeric list
list=[10,20,30,40,50]
print(max(list))
# Q12 Take a list a=[1,1,2,3,5,8,13,21,34,55,89] write a program that print alll the elements of the list which are 
# less than 5 

a=[1,1,2,3,5,8,13,21,34,55,89]
b=[]
for i in a:
    if(i<5):
        b.append(i)
print(b)

        


