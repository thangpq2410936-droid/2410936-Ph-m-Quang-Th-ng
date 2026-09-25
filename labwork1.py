import math
print("ex1")
r=float(input('Enter r:'))
a=math.pi*r**2
print("area of circle:",f"{a:.2f}")
print("ex2")
C=float(input("enter the C:"))
F=(1.8*C)+32
print("the temperature into F:",f"{F:.2f}")
print("ex3")
n=int(input("Enter the number need to check :"))
if n < 2:
    print("Not Prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("It's Prime")        
print("ex4")
n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("Pefect Number")
else:     
    print("Not Perfect Number")           
print("ex5")  
choice=input("Enter your favorite color:")
color=["yellow","blue","red","black"]
if choice in color:
    print("index",color.index(choice)+1)
else:
    print("Sorry, I could not find your color")
print("ex6")
range1=range(0,7,1)
range2=range(1,11,3)
range3=range(5,0,-1)
range4=range(6,-3,-2)
print(list(range1))
print(list(range2))
print(list(range3))
print(list(range4))
print("ex7")
def remove_dollar_sign(s):
    return s.replace("$", "")
n=input("enter the string have $:")
print("the string after change:",remove_dollar_sign(n))
print("ex8")
def extract_even(l):
    result = []

    for i in l:
        if i % 2 == 0:
            result.append(i)

    return result

print(extract_even([1, 4, 5, -1, 10]))
print("ex9")
n=int(input("ENTER HE NUMBER TO FIND FACTORIAL:"))
factorial=1
if n<2:
    print("PLS THE NUMBER HAVE TO MORE THAN 1!")
else:
    for i in range(1,n+1,1):
        factorial=factorial*i
    print("THE FACTORIAL OF",n,"=",factorial)
print("ex10")
n=int(input("enter the number:"))
print("division of number of ",n,"are:",end=" ")
for i in range(1,n+1,1):
    if n%i==0:
        print(i,end=" ")
print("ex11")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("Distance =", d)
print("ex12")
def rectangle(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

m = int(input("m = "))
n = int(input("n = "))

rectangle(m, n)



