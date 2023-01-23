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
        
    #Simplifying new unit
    #Boleans for identifying if the loop is in the denominator or numerator and if its in a paranthesis or not
    DemMode = False
    ParMode = False
    ParDemMode = False
    
    #Add bolean used for adding in NumList or Demlist
    Add = False
    
    #List for sorting units depending on wether they end up in the denominator or numerator
    NumList = []
    DemList = []
    
    for i in NewUnit:
        if i == '[':
            Add = True
        elif i == ']':
            Add = False
        elif i == '(':
            ParMode = True
        elif i == '/':
            if ParMode == True:
                ParDemMode = True
            else:
                DemMode = True
        elif i == ')':
            ParMode = False
            ParDemMode = False
        elif i == 'c' and NewUnit[NewUnit.index(i)+1] == 'm':
            if DemMode == False:
                NumList.append('cm')
            elif DemMode == True:
                DemList.append('cm')
        elif i == 'd' and NewUnit[NewUnit.index(i)+1] == 'y' and NewUnit[NewUnit.index(i)+2] == 'n':
            if DemMode == False:
                NumList.append('dyn')
            elif DemMode == True:
                DemList.append('dyn')
        elif i == 'e' and NewUnit[NewUnit.index(i)+1] == 'r' and NewUnit[NewUnit.index(i)+2] == 'g':
            if DemMode == False:
                NumList.append('erg')
            elif DemMode == True:
                DemList.append('erg')
        elif i == 'B' and NewUnit[NewUnit.index(i)+1] == 'a':
            if DemMode == False:
                NumList.append('Ba')
            elif DemMode == True:
                DemList.append('Ba')
        elif i == 's':
            if DemMode == False:
                NumList.append('s')
            elif DemMode == True:
                DemList.append('s')
        elif i == 'g' and NewUnit[NewUnit.index(i)-1] != 'r':
            if DemMode == False:
                if ParMode == False:
                    NumList.append('g')
                elif ParMode == True and ParDemMode == False:
                    NumList.appen('g')
                elif ParMode == True and ParDemMode == True:
                    DemList.append('g')
            elif DemMode == True:
                if ParMode == False:
                    DemList.append('g')
                elif ParMode == True and ParDemMode == False:
                    DemList.append('g')
                elif ParMode == True and ParDemMode == True:
                    NumList.append('g')
    
    NewUnit = ''
    NumListCopy = NumList.copy()
    DemListCopy = DemList.copy()
    s = 0
    
    for i in range(len(NumList)):
        for j in range(len(DemList)):
            if NumList[i] == DemList[j]:
                DemListCopy.pop(j-s)
                s += 1
                continue
    
    NumList = NumListCopy
    DemList = DemListCopy
    
    for i in NumList:
        NewUnit += '['+i+']'
    
    if DemList != []:
        NewUnit += '/'
        
        for i in DemList:
            NewUnit += '['+i+']'
            
    return conv, NewUnit