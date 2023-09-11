
"""""
Q. Write a program to find biggest of given 3 numbers from the commad prompt?
n1=(input("enter the number 1 : "))
n2=(input("enter the  number2 : "))
n3=(input("enter the number 3 : "))

if n1 >n2 and n1 >n3:
    largest=n1
elif n2>n1 and n2 >n3:
    largest=n2
else:
    largest=n3

print("largest among {} {} and {} is {}".format(n1,n2,n3,largest))

Eg 3: To print Hello 30 times
a="hello"
for a in range(30):
    print("hello")
#Eg 4: To display numbers from 0 to 10
a=10
for a in range(0,11):
    print(a)#Eg 5: To display odd numbers from 0 to 20
li=(22,32,12,43,6)
for i in li:
    if i%2!=0:
       print(i)

Eg 6: To display numbers from 10 to 1 in descending order
l=()
for i in range(1,11):
    print(i)
    l.append(i)
print(l)
print(l[::-1])

Eg 7: To print sum of numbers presenst inside list
list=(10,20,22,13)
sum=0
for i in list:
    sum=sum+i
print("sum of list is:",sum)

#Eg: To print numbers from 1 to 10 by using while loop

li=(1,2,3,4,5,6,7,8,9,10)
i=1
while i<=10:
    print(i)
    i=i+1

Eg: To display the sum of first n number?

def findSum(n):
	sum = 0
	x = 1
	while x <= n:
		sum = sum + x
		x = x + 1
	return sum

n = 5
print (findSum(n))

#Eg: write a program to prompt user to enter some name until entering Sumayya
def sumayya():
    name=str(input("enter the name : "))
    print("sumayya " + str(name))
    return
sumayya()

#Q. Write a program to access each character of string in forward and backward direction
  # by using while loop and for loop?"""
"""
str="hello word"
str1=str.split()
print(str)
"""
#Q.Counting substring in the given String ?
"""
import re

s = 'abcde'

res= len(re.findall('(?=(aba))', s))

print("Number of substrings", res)

#Q.Replacing a string with another string:
string = "Good Morning"
new_string = string.replace("Good", "Great")

print(new_string)

s = "Learning Python is very difficult"
#o / p: Learning
#Python is very
#easy


s = "Learning Python is very difficult"
for x in s:
    if x ==" ":
        print()
    else:
        print(x,end="")
 """
#Q.Replacing a string with another string:
"""""
s1='abcabcabcabcadda' #count a,ab,
S2='abc','sumayya'
s2_s1=s1_s2.replace(s1,s2)
print(s1_s2)
"""


#Q.Joining of Strings ?
#t=('sunny','bunny','chinny')
#o/p:sunny-bunny-chinny

t=('sunny','bunny','chinny')
x="-".join(t)
print(x)

#l=['hyderabad','singapore','london','dubai']
l=('hyderabad','singapore','london','dubai')
str1=':'.join(l)
print(l)
print(str1)

s='learning Python is very Easy'
#o/p: LEARNING PYTHON IS VERY EASY
#o/p:learning python is very easy
#o/p:LEARNING pYTHON IS VERY eASY
#o/p:Learning Python Is Very Easy
#o/p:Learning python is very easy

str="learning Python is very Easy"
u=s.upper()
print(u)

n=s.lower()
print(n)

b=s.title()
print(b)
