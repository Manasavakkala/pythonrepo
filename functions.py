def add(arg_1):
    return arg_1
val_1 = add(6)
print(val_1)

def fun_name(arg_2,arg_1="'welcome "):
    return arg_1+arg_2
var_1=fun_name("hcl'")
print(var_1)


def word(name):
    print("welcome",name)
 word("hcl")



def divby_7(val_1):
    if (val_1%7==0):
        print("True")
    else:
        print("False")
    return divby_7
b=divby_7(44)
print(b)

def square(arg_1):
    area_square=arg_1*arg_1
    perimeter_square=2*arg_1
    print(area_square)
    print(perimeter_square)
    return square
val_1=square(2)
print(val_1)


a="python"
print(a[1])


def word(arg_1):
    #print(arg_1[1])
    return arg_1[1]
a=word("python")
print(a)
print(add(a))

def str_count(arg_1="FanTaSY"):
    l=0
    u=0
    for i in arg_1:
        if i.islower():
            l+=1
        else:
            u+=1
    return (l,u)
print(str_count())


m=int(input("enter from"))
n=int(input("ends to"))
b=[]
for i in range(m,n):
    a=i**2
    if a<=n:
        b.append(a)
print(b)


def num(n):














