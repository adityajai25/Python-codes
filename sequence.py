# Question 1. Write a for loop to iterate through the list A = [1, 2, 3, 4, 5, 6]. Square each element of the list in one by one fashion and print them. After the end of the iteration, print - "The sequence has ended".

lst = [1,2,3,4,5,6]

for element in lst:
    print(element**2)
else:
    print("The sequence has ended")