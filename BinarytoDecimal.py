def toDecimal(Binary):
    decimal=0
    Binary=Binary[::-1]
    for i in range(len(Binary)):
        if Binary[i]=='1':
            decimal +=2**i
    return decimal
binary=eval(input("Enter the binary number: "))
display = toDecimal(binary)
print(display)