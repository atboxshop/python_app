def cube(number):
    print('id (number) before modifying number:', id(number)) #passing by reference
    number **= 3 #trying to modify the immutable int objects
    #because it can not modify an inmmutable object so it will create a new address object
    print('id (number) after modifying number:', id(number))
    return number
x = 7
print('id (x) is:', id(x))#passing fucntion argument in python is alway passing by reference.
cube(x)