
'''x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)'''

# FOR LOOPS
#irating over list

'''colours = ["red","yello","green","pink"]
for colour in colours:
    print(colour)

    for i in colour:
        print(i)'''

#for a in range(1+20001):
 #   print(a+1)

'''for k in range(1,12,3):
    print(k)'''



#WHILE LOOP
'''count = 5
while(count>0):
    print(count)
    count = count-1'''

#else with while loop
x = 5
while(x > 0):
    print(x)
    x = x - 1
else:
    print('the count is 0')



# break and continue

for i in range(1,101,1):
    print(i,end=" ")
    if(i==50):
        break
    else:
        print("mijeijeij")

for i in range(12):
    if (i==10):
        print("5X",i+1,("=")5*(i + 1))

for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

for i in range(3):
    print(i)
