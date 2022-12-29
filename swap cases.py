string1="VIKATAKAVI"
string2=string1[::-1]
print(string1==string2)

string1="MOM"
string2=string1[::-1]
print(string1==string2)
print(string2)

a="PyThOn"
print(a.swapcase())

b="dd-mm-yy"
c=b.replace("-","/")
print(c)

a=7
b=10
if (a<b):
    print("statement is true")
else:
    print("statement is false")

a=1
b=3
c=5
is_a_greatest=(a>b) and (a>c)
if is_a_greatest:
    print(a)
else:
    is_b_greatest=(b>c)
if is_b_greatest:
        print(b)
 else:
        print(c)

a=1287
b=a.[::-1]
print(b)







