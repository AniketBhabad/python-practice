#sets

#unordered collection of data item ,{} use for set

'''set1 = {"aniket",20,True,49.50}
print(set1)

set2=set()
print(type(set2))

set1 = {"aniket",20,True,49.50,}
for item in set1:
    print(item)

# sets method

a={1,2,3,"aniket"}
a.add("bhabad")     #add a single item in set
print(a)   

a={1,2,3,"aniket"}
a.remove(2)
print(a)     #remove a item form set

a={1,2,3,"aniket"}
a.discard(5)
print(a)   #no error if item not in set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi",20}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid",30}
cities3 =cities.union(cities2)
print(cities3)

a = {1,2,3}
b = {3,4,5}
c = a.union(b)
print(c)

a.update(b)
print(a)

c={"a","b","c"}
d={"c","d","e"}
e=c.union(d)   #creates a new set form c,d
print(e)
c.update(d)  #add all elemets form c,d modifies a it self
print(c)

a= {1,2,3,4,}
b= {2,3,5,6}
c = a.intersection(b)  #only commomn value return with new set
print(c)

a.intersection_update(b)
print(a)             #only common elemnts in set a modifie (a)


a= {1,2,3,4}
b={5,6,7,3}
c=a.symmetric_difference(b)   # 3 remove form output no same value return
print(c)                      # output is 1,2,4,5,6,7  with new set

a.symmetric_difference_update(b)
print(a)                      #remove common elements from a and modifies (a)

a= {10,20,30,40,100}
b= {20,50,40,60}
c=a.difference(b)     #returnnew set with elements in a but not in b
print(c)              #output 10,30,100

a.difference_update(b)
print(a)              # return element from a that are present in b modifies 
                      #output(10,30,100)
                      
a = {1,2,3,4}
b = {1,8,7,9}
print(a.isdisjoint(b))  #if common item present output is (false)

a = {1,2,3,4}
b = {0,8,7,9}
print(a.isdisjoint(b))  #if no common item output(true)

a = {1,2}
b= {1,2,3,4}
print(a.issubset(b))  #true because all item a in b

a = {1,2,3,4}
b = {1,2}
print(a.issuperset(b))   #true, a has everthing in b

a = {100,200,300,"aniket"} #random item remove
a.pop()
print(a)

b = {100,200,300,"aniket"}
del b
#print(b)        #delete ful set

c = {3,4,5}
c.clear()
print(c)

info = {"aniket", 19, False, 5.9}
if "aniket" in info:
    print("aniket is present.")
else:
    print("not present")

print(19 in info)


#dict

a = {"name":"aniket","age":20,"course":"bscit"}
print(a)
print(a["name"])
#print(a.get['course'])
print(a.values())
print(a.keys())
print(a.items())

a = {"name":"aniket","age":20,"course":"bscit"}
a.update({"DOB":2005})
print(a)
a.pop("DOB") 
print(a)
a.popitem() #remove last key-value
print(a)
a = {"name":"aniket","age":20,"course":"bscit"}
del a["name"] #remove dic item
print(a)

# FOR LOOPS WITH ELSE

for item in range(5):
    print(item)

else:
    print(" Loop complete")  #this use of else in loop

numbers = [1,2,3,4]
for num in numbers:
    if num == 3:
     break 
    print(num)
else:
    print("loop complete")  # no else print becasue of break 

# Prime no chek with loop and else
num = 7
for i in range(2,num):
    if num % i == 0:
      print("not prime number")
      break
else:

      print("prime number")

i = 0
while i<7:
    print(i)
    i = i+1
    if i==4:
        break
else:                  # no else print (break)
    print("sorry no i")    

#exception handling  

try:
    num = int(input("enter an integer:"))
except:
    print("number entered is not an integer") #error nahi dega ye print hoga



a = input("Enter the number:")
try:
 for i in range(1,11):
    print(f'{int(a)}x{i}={int(a)*i}')
except:     #run if error in code
    print("invaild input")
finally:           #always run if error or not
    print("some imp lines of code")
    print("end of program")

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else: # if no error else also run
    print("Integer Accepted.")
finally:          #always run
    print("This block is always executed.")'''

# Raising custom erros

#a = int(input("enter the value between 5 and 9"))

#if(a<5 or a>9):
   # raise ValueError("value should be between 5 and 9")

num= int(input("Enter the number:"))
if num<0:
    raise ValueError("negative number not allowed!")
else:
    print("valid number")