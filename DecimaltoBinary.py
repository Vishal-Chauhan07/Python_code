def toBinary(decimal):
    Binary=" "
    if decimal==0:
        Binary=0
    else:
        while decimal>0:
            remainder=decimal%2
            Binary=str(remainder)+Binary
            decimal=decimal//2
    
    return Binary

decimal_number=eval(input("Enter the decimal number :"))
display = toBinary(decimal_number)
print(display)