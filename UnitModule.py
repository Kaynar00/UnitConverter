def SItoCGS(Unit):
    """
    Calculates the value one needs to multiply to change the input unit from SI to cgs.
    The input values for this function is:
        Unit: The units in a string like \'[m]/[s]\' or \'[J]*[s]\'
    """
    #Bolean values for the loop
    Div = False
    Add = False

    #The variable for the convertion value for cgs
    conv = 1 

    #Loop that calculates the convertion value
    for i in Unit:
        
        if i == '[':
            Add = True
        elif i == 'm':
            if Add == True:
                if Div == False:
                    conv *= 1e2
                elif Div == True:
                    conv /= 1e2
            else:
                continue
        elif i == 's':
            continue
        elif i == ']':
            Add = False
        elif i == '/':
            Div = True
    return conv