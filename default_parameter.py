def rectangle(lenght = 2, width = 3):
    return lenght * width

print('Result without parameter:', rectangle())
print('Result with only 1 parameter:',rectangle(4))
print('Result with 2 parameter:', rectangle(5, 7))
print("Result with keyword arguments:", rectangle(lenght=5,width=8))

print(min(88, 75, 96, 55, 83)) #arbitrary argument lists
#third parameter of min function is a *args or a tuple


def average(*args):
    return sum(args) / len(args)

print(average(5, 10, 15, 20))

