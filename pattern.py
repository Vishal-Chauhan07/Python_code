def Rectangle(n):  # Change this value to adjust the size of the square
    for i in range(n):
         for j in range(n):
           print("* ", end="")
         print()
n=eval(input("Enter the number:"))


Rectangle(n)


def Right_Triagle1(n):
    # Change this value to adjust the height of the triangle
    for i in range(1, n + 1):
         for j in range(i):
             print("* ", end="")
         print()


Right_Triagle1()


def Inverted_Right_Triangle(n):
    # Change this value to adjust the height of the triangle
    for i in range(n, 0, -1):
        for j in range(i):
           print("* ", end="")
        print()


Inverted_Right_Triangle(8)

def Pyramid(n):
    # Change this value to adjust the height of the pyramid
    for i in range(1, n + 1):
         print(" " * (n - i) + "* " * i)


Pyramid(9)

def Hollow_Rectangle(r,c):
     # Change the number of rows
     # Change the number of columns
    for i in range(r):
        for j in range(c):
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


Hollow_Rectangle(4,6)