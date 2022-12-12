"""Return the maximum of tree values"""
def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print("Enter three values for looking the biggest number in three entered values")
x = int(input("Enter value 1:"))
y = int(input("Enter value 2:"))
z = int(input("Enter value 3:"))
max = maximum(x,y,z)
print("The biggest number is:",max)
