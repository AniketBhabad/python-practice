#STRING

name = "Aniket"
print("hello,"+name)

print('he said,"i want to eat apple".')

#multiline string use (''' ''')

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[0:6]) 

for characters in name:
    print(name)

#string slicing and operation on string

fruit = "Mango"
a = len(fruit)
print("Mango is",a,"letter word")

a = "applepie"
print(a[:5])
print(a[6])

pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-6])     #Slicing using negative index

alphabets = "ABCDE"
for charcters in alphabets:
    print(alphabets) #abcde for in line 5 times

for i in alphabets:
    print(i)     # a,b,c,d,e single 5 line


fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)

print(fruit[:5])
print(fruit[0:2])
print(fruit[-1:len(fruit)-3])

nm = "harry"
print(nm[-3:-1])

#0 1 2 3 4  (positive index) 
#h a r r y
#-5 -4 -3 -2 - 1 ( negative index)

a = "Aniket"
print(a[0:-2])

#A n i k e t
#-6 -5 -4 -3 -2 -1

   # STRING METHOD

a = "ANIket bhABAd" 
print(a.upper())  # all character in upper

b = 'NJANUANnjcej'  
print(b.lower())  # all character in lower

c = " silver    spoon"
print(c.strip())   # remove white spaces

d = "aniket>??:"
print(d.rstrip(">??:")) # remove trailing charcter

e = "silver spoon"
print(e.replace("sp",("mo"))) # replace 

str = "Aniket Bhabad"
print(str.split(" ")) #spereted string 

str2 = "hello"
print(str2.capitalize())  #first character of the string to uppercase and the rest other characters of the string are turned to lowercase.

str3 = "heLlo worLD"
print(str3.capitalize())

s = "Welcome to the park"
print(s.center(130))    # string to the center

f = "nhcnhnahuaabynejnaanjna"
print(f.count("a"))      # use for count 

g  = " Aniket !!!yy"
print(g.endswith("!!!yy")) # chek for string ends

g = "he's name  dan. he is honest man."
print(g.find("is"))   #if string is absence given value-1

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))  # index method returns the position of the occurrnce of the sprcified value

ex = "aniket"
print(ex.index("i"))

s = "Welcometo00AAAaaathe"
print(s.isalnum()) # only need plane string no space or special charc

a = "aniketbhabad"
print(a.isalpha())  # (a-z, A-Z) no numners

b = "aniket"
print(a.islower())  # string in lower case value return true

a = "aniket bhabad"
print(a.isprintable()) # only printable string no ,/n /t 

a = "     "
print(a.isspace()) #only white space

s = str1 = "World Health Organization"  # returns True only if the first letter of each word of the string is capitalized, else it returns False.
print(s.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())   #true when all characters in upper case

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))  # start with 1st value

str1 = "Python is A Interpreted LanGuage"  #swap upper to lower and lower to upeer
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())                     # capitalizes each letter word within string


# IF - ELSE STAEMENT

num = int(input("enter the value:"))   
if num % 3== 0:
    print("divsible by 3")
else:
    print("not divible by 3")

appleprice = int(input("enter the appleprice:"))
budget =int(input("enter the budget:"))    
if (appleprice <= budget):
    print(" 1 kg apple pack")
else:
    print("don't pack")   # this is if - else statment

num = 0
if (num < 0):
    print("number is negative")
elif (num == 0):
    print("number is zero")
else:
    print("number is positive")

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")

# MATCH-CASE STAEMENT

x = int(input("enter value of num:"))
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("something else")   

day = "sunday"
match day:
    case "monday":
        print("start of week")
    case "friday":
        print("weekwend is near")
    case "sunday":
        print("relax day")    
    case _:
        print("weekday")    

# FOR LOOP

name = "aniket"
for name in name:
    print(name, end=",")  #, for comma in charcters

colors = ["red","pink","blue","black"]
for x in colors:
    print(x)      #we can use loops for lists, sets and dictionaries.

for a in range(1,10):
    print(a)

for a in range(12,122,12):
    print(a)      #creat table

#WHILE LOOP
i = 1
while(i<=10):
    print(i)
    i = i+1

i = 2
while(i<=20):
    print(i)
    i = i + 2    

i = 10
while(i>=1):
    print(i)
    i = i - 1

num = int(input("Enter the no:"))
i  = 1
while(i <=10):
    print(num,"x",i,"=",num*i)
    i = i + 1

    #break and continue 

for i in range(10):
    if(i==8):
      continue         #break for stop the loop
                       #continue for skip the loop (iteration)
    print(i)
    
    for i in range(10):
     if(i==8):
       break
    print(i) 

for i in range(1,11):
  if(i==7):
    continue 
  print("5 x",i,"=",5*i)

  #while true (do - while)

while True:
   i = int(input("enter the number:"))
   if i <=0:
        print("loop end")
        break                 #square of no.
   else:
        print("square is",i*i)

while True:
    password = (input("Enter the password:"))
    if (password==('admin123')):
        print("password found")
        break                      #enter right password
    else:
        print("enter the right password")   


while True:
    num = int(input("Enter the right number:"))
    if (num==7):
        print("number found")
        break
    else:
        print("please the the right number")

while True:
     choice = int(input("Enter your choice:"))
     if (choice==1):
          print("hello")
     elif (choice==2):
          print("bye")
     elif (choice==3):
          print("exiting")
          break
     else:
          print("invalid choice")
            
#FUNCTION (USER DEFIEND )

def calcuate(a,b):
    mean=(a*b)
    print(mean)

def isgreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("secound number is greater")
print(isgreater)
a= 10
b= 6
calcuate(a,b)
isgreater(a,b)

#mean = a*b
#print(mean)

c = 35
d = 4
calcuate(c,d)
isgreater(c,d)
#mean2 = c*d
#print(mean2)
# final













  
   
  
  




    
  