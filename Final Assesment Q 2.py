#Find nth fibonacci number. If it starts with 0,1,1,2.....
#Also, Print Incorrect Input if n is less than or equal to 0.




def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2 , n ):
            c = a + b
            a = b
            b = c
        return b



print(fibonacci(4))