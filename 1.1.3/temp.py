# Multiply 8 x 4, only using addition

num1 = 800
product = 0

#example:multiply 800 x 10000
for t in range(10000):
    product = product + num1
#  print(product)

#play with range function
#range(stop) or range(start,stop,step=1)
#below works but also try
##example_list = range(22)
#print(list(example_list))

print(list(range(10, 96, 7)))
#if you want 22 you need to put 23 and the 0 counts!!!
#starts at 10 and goes up to 96 but if it goes by 7s it will only go up to 94 since there is no 7s to get to 96
