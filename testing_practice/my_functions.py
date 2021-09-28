## Funcitons for Testing ##

def max3(num1, num2, num3):
    
    # Return Max 
    return max(num1, num2, num3)

def odd(bool1, bool2, bool3):
    boolList = [bool1, bool2, bool3]

    counter = 0
    for i in range(len(boolList)):
        if bool(boolList[i]) is True:
            counter += 1
        else: 
            next
    
    # return bool 
    if counter == 0:
        return False
    elif counter == 2:
        return False
    else: 
        return True


def majority(bool1, bool2, bool3):
    boolList = [bool1, bool2, bool3]

    # Gets num True
    counter = 0
    for i in range(len(boolList)):
        if bool(boolList[i]) == True:
            counter += 1
        else:
            next

    # Return 
    if counter >= 2:
        return True
    else: 
        return False