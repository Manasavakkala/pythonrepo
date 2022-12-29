var=None
print(var)
print(type(var))

def increment(a):
    a +=1
a=55
result=increment(a)
print(result)






a=2
tuple_a=(5,"six",a,8.2)
print(tuple_a)
tuple_b=("hiee",5,1.22,"hola")
print(tuple_b)
print(tuple_a+tuple_b)

#string to tuple

list_a=[1,2,3]
tuple_a=tuple(list_a)
print(tuple_a)

#sequence to tuple

tuple_a=tuple(range(4))
print(tuple_a)

#in and not in

tuple_a=(1,2,3,6)
b=8 in tuple_a
print(b)

tuple_a=(1,2,3,4)
b=11 not in tuple_a
print(b)

print(tuple_a[2])

colour="blue"
tuple_a=colour
print(tuple_a)

word="carry"
is_part='rr' in word
print(is_part)

tuple_a=('c','a','r')
(s_1,s_2,s_3)=tuple_a
print(s_1)
print(s_2)
print(s_3)


a=1,2,3
print(type(a))
print(a)

a=1
print(type(a))
print(a)


a=2
set_a={5,"six",a,8.2}
print(type(set_a))
print(set_a)

set_a={"a","b","c"}
print(set_a)

set_a={"a",["c","a"]}
print(set_a)

set_a=set()
print(type(set_a))
print(set_a)

set_a=set([1,2,1])
print(type(set_a))
print(set_a)

set_a=set("apple")
print(set_a)

set_a=set((1,2,1))
print(set_a)

set_a = {1,2,3}
print(set_a[1])
print(set_a[1:3])

#add items

set_a={1,2,3,8,8}
set_a.add(20)
print(set_a)

set_a.add(2)
print(set_a)

set_a={1,3,9}
set_a.update([2,3])
print(set_a)


