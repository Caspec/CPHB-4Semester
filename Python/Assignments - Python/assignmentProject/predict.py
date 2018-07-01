
def predict(arr_blue, arr_red, arr_green):
    #Two checks to conclude if picture contain BIF or FCK fan
    checkBIF = False
    #Not used yet as FCK range is not decided.
    checkFCK = False

    for x in range(50, 70):
        if 1999 < arr_blue[x-1] < 4201:
            checkBIF = True
        else:
            checkBIF = False
        if not checkBIF:
            break

    #Add another loop for the range of FCK, and change return
    #logic to include checkFCK and return the final conclusion.
    if checkBIF and not checkFCK:
        return "Brøndby fan!"
    else:
        return "Ikke en brøndby fan..."

#Test data for en brøndby fan    
result = predict([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 
2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 
2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 0, 0, 0, 0], [], [])

#Test data for en ikke brøndby fan
#result = predict([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 0, 0, 0, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 1900, 
# 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 
# 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 0, 0, 0, 0], [], [])

print(str(result))