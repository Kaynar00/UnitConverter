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
    
    
    NewUnit = ''

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
                NewUnit += '[cm]'
            else:
                continue
        elif i == 'N':
            if Add == True:
                if Div == False:
                    conv *= 1e5
                elif Div == True:
                    conv /= 1e5
                NewUnit += '[dyn]'
            else:
                continue
        elif i == 'J':
            if Add == True:
                if Div == False:
                    conv *= 1e7
                elif Div == True:
                    conv /= 1e7
                NewUnit += '[erg]'
            else:
                continue
        elif i == 'W':
            if Add == True:
                if Div == False:
                    conv *= 1e7
                elif Div == True:
                    conv /= 1e7
                NewUnit += '([erg]/[s])'
            else:
                continue
        elif i == 'P':
            continue
        elif i == 'a' and Unit[Unit.index(i)-1] == 'P':
            if Add == True:
                if Div == False:
                    conv *= 1e1
                elif Div == True:
                    conv /= 1e1
                NewUnit += '[Ba]'
            else:
                continue
        elif i == 's':
            NewUnit += '[s]'
        elif i == 'g':
            NewUnit += '[g]'
        elif i == ']':
            Add = False
        elif i == '/':
            Div = True
            NewUnit += '/'
        #Prefixes
        elif i == 'k':
            if Add == True:
                if Div == False:
                    conv *= 1e3
                elif Div == True:
                    conv /= 1e3
            else:
                continue
        else:
            continue
    return conv, NewUnit