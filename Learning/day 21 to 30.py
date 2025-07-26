                #FUNCTIONS - ARGUMENTS
                
#default argument
'''def user(name="guest"):
    print("hello",name)
user("aniket") 

def intro(name,age= 20):
    print(name, age)
intro('aniket')    


#key world argument
def student(name,age):
    print(name,"is",age,"years old")
student(name= "aniket",age= 20)   #name and age key word argument 


def name(**name):
   print(type(name))
   print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")

#Required arguments

def name(fname,mname,lname):
    print("hello",fname,mname,lname)
name ("aniket","bhabad")    #erro missing 1 required positional argument

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")

 

 #LIST 


lst = [1,2,3,"aniket",True,]
print(lst)
print(len(lst))   #single list can contain items of different data types.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]    
print(colors[0])
print(colors[1])
print(len(colors))
#for negative calculation 5-2=3 (yello)
print(colors[-2])

item=[3,4,6,"aniket",489]
if "aniket" in item:
    print("yes")
else:
    print("no")  


#RANGE OF INDEX
#listname[start:end:jumpindex] ex(1:4:7)

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes']
print(animals[-8:3])

#3rd consecutive value
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3]) #star from 1 jump 3 time end with 8

#list compreshension

names=["aniket","suraj","sudhir","kunal","ankit","anaya"]
name1= [ item for item in names if "a" in item]
print(name1)
name2=[item for item in names if(len(item)>4)]
print(name2)

#LIST METHOD
number= [4,5,7,2,8,4,8,9,0,3]
number.sort()
print(number)           #ascending order( 0, 2, 3, 4, 4, 5, 7, 8, 8, 9]

numbers=[1,2,3,4,9,8,7,6]
numbers.sort(reverse=True)
print(numbers)           #descending order(9, 8, 7, 6, 4, 3, 2, 1)


num= [3,4,5,6,43,67,8,7,]
num.reverse()
print(num)               #reverse the list order

colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)          #['green', 'blue', 'indigo', 'voilet']

num=[2,3,56,8,7,5,5,4,7]
print(num.index(4))                   
print(num.index(3))

num1= [43,5,677,77,77,77,77,5,3,45,6,8]
print(num1.count(77))  #4

color= ["pink","black","white","blue"]
new=color.copy()
print(color)
print(new)

num= [3,4,5,6,5,4,]
num1=num.copy()
print(num)
print(num1)

colors = ["voilet", "indigo", "blue"]
colors.append("green")  #add green
print(colors)


color= ["blue","black","white"]
color.insert(0,"pink")
print(color)         #insert pink in 0 index


#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)         #two list in 1 list
#secound method
print(colors+rainbow)


#TUPLES
#Tuples are unchangeable
#() use for tuples
tup= (1,2,3,4,5)
tup2= ("aniket",20,True,"vikas")
print(tup)
print(tup2)

country=("india","italy","spain")
print(country[0])
print(country[1])
print(country[2])

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(len(country))
print(country[-3])
print(country[-1])
print(country[-4])

if "Spain" in country:
    print("ok")
else:
    print("not ok")

#tuples operetor
country = ("Spain", "Italy", "India", "England", "Germany")
a=list(country)
a.append("russia")#add item
a.pop(2) #remove item
a[0]="finland" #change item
country=tuple(a)
print(country)

tup=(2,3,4,5,66,5,5,3,4,5,5,5,)
res = tup.count(3)
print(res)

tuple = (1,2,3,6,5,8,6,9,5,4)
res = tuple.index(0)
print(res)'''


#f-string
name= "aniket"
age=20
print(f"my name is {name} and i am {age} years old.")

print(f"{3*5}")

letter = "Hey my name is {1} and i am from {0} "

country = "india"
name= "aniket"
print(letter.format(country,name,))
print(f"Hey my name is {name} and i am from {country} ")

price = 39.00344
apple =print(f"1 kg apple price is{price:.2f}")

name="aniket" 
city = "mumbai"
print(f"hello,my name is {name} and i am live in {city} ")

math = 80
science = 75
english = 75

print(f"total marks obtained:{math+science+english}")

price = 49.09000
print(f"the price is:{price:.2f}")

#DOC - STRING
def greet(name):
    '''yeh function kisi person ko greet krta hai'''
    return(f"hello{name}")
print(greet("aniket"))
print(greet.__doc__)

def square(n):
    '''takes in a number n, return the square of n'''
    print(n**2)
square(5)    

#RECURSTION

def countdown(n):
    if (n==0):
        return
    print(n)
    countdown(n-1)
countdown(5)  

def factorial(num):
    if (num==1 or num==0):
        return 1
    else:
        return(num*factorial(num-5))
print(factorial(5))

print(5*4*3*2*1)


