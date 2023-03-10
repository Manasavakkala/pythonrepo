class Car:
    someclassdummyvar="dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyvar)

carObj=Car()
carObj.sample_car_instance_method("Hello again!")

carObj2=Car()
carObj2.sample_car_instance_method(2)



class CarSample:
    dummyvar1="dummyvar1"
    dummyvar2="dummyvar2"
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def displayCarDetails(self):
        print(self.name)
        print(self.model)

carObj=CarSample("Audi","A5")
carObj.displayCarDetails()





#static Method

class StaticClass:
    @staticmethod
    def sample_static_method_addition(x,y):
        return x+y
    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x*y

staticObj=StaticClass()
output_add=staticObj.sample_static_method_addition(2,3)
output_mul=staticObj.sample_static_method_multiplication(2,3)
print(output_add,output_mul)

StaticClass.sample_static_method_addition(2,3)


#class Method

class ClassMethodExample:
    classVar1=False
    classVar2="ON"
    @classmethod
    def sample_class_method(cls):
        cls.classVar1=True
        cls.classVar2="OFF"

ClassMethodExample.sample_class_method()
print(ClassMethodExample.classVar1)
print(ClassMethodExample.classVar2)


class my_class:
    dummyVar="Test"
    def instance_method_example(self,a):
        print(a)
        print(self.dummyVar)

myclassObj=my_class()
myclassObj.instance_method_example("Hola!")

class my_instance_class:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sample_instance_class(self):
        print(self.a,self.b)

obj=my_instance_class("Cap","IronMan")
obj.sample_instance_class()

#Class Methods

class ClassMethod:
    @classmethod
    def class_method(cls):
        print("this is class method")

obj=ClassMethod()
obj.class_method()

ClassMethod.class_method()

#static method

class StaticMethod:
    @staticmethod
    def static_method():
        print("this is static method")

obj=StaticMethod()
obj.static_method()

StaticMethod.static_method()


class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    @classmethod
    def price(cls,name,year):
        return cls(name,"2022")










Car.price("Audi",2015)







# Static Method

class StaticClass:
    @staticmethod
    def sample_static_method_addition(x,y):
        return x+y
    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x*y

staticObj=StaticClass()
output_add=staticObj.sample_static_method_addition(2,3)
output_mul=staticObj.sample_static_method_multiplication(2,3)
print(output_add,output_mul)

StaticClass.sample_static_method_addition(2,3)




