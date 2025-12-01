num1 = 6
num2 = 7

# Nested loop example
for n in range(num1):
    #print("n: " + str(n))
    for o in range(num2):
       # print("o: " + str(o))
        if n > o:
            print("n was bigger!")
        elif n < o:
            print("o was bigger!")
        else:
            print("they are equal!!!")