
def modify_global():
    global x # Declare x in global in local function
    x = 'Hello'
    return x

modify_global()
print(x) # print x in global scope