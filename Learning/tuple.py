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
res = tuple.index(3)
print(res)

