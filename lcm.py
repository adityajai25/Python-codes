a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    largest = a
else:
    largest = b
    
while True:
    if largest % a == 0 and largest % b == 0:
        print("LCM of {} and {} is {}".format(a,b,largest))
        break
    largest += 1
