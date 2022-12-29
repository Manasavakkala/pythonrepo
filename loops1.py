a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end= " ")
    print()

a=int(input())
for i in range(a):
    for j in range(a):
        print("*",end=" ")
    print()

a=int(input())
b=int(input())
for i in range(1,a+1):
    for j in range(1,b+1):
             print("*",end=" ")
     print()


#square

a=3
b=3
for i in range(a):
    for j in range(b):
        print("*",end=" ")
    print()

#right angle triangle

a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


#sum of given numbers
a=[1,2,3,4,]
b=0
for i in a:
    b=b+i
print(b)

#sum of n numbers

a=int(input())
sum=0
for i in range(a):
     sum=sum+i
print(sum)

a=[1,2,3,4]
b=1
for i in range(a):
    b=b*i
print(b)
#diagonal
a=int(input())
b=int(input())
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print( )

#hollow square

s1=int(input())
a=2*s1-2
for i in range(0,s1):
    for j in range(0,a):
        print("*",end=" ")
    print()

a=int(input())
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end=" ")
    print()


n=int(input())
for i in range(n):
    for j in range (n-i+1):
        print(" ",end=" ")
        for m in range(i):
            print("*",end=" ")
        print()


n=3
for i in range(0,3):
    for j in range(3,0):
    print("*",end=" ")
print()

n1=6
n2=5
for i in range(0,2,2):
    for j in range(n2):
        print("*",end=" ")
    print()


#inverted triangle
m=int(input())
n=int(input())
for i in range(0,m+1):
    for j in range(0,n+1):
        if (j-i>=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()



