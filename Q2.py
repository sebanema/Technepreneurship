#Interchangeable array with even/odd numbers
array = [6,9,4,2,0,26,0,9,66,420,69,8008]

#Set even/odd variables
no_even, no_odd = 0, 0
#Set empty list for calling vector of even/odd numbers
even = []
odd = []

#for loop extracting the count of even/odd numbers and appending the seperated numbers to a new list
for num in array:
    if num % 2 == 0:
        no_even += 1
        even.append(num)


    else:
        no_odd += 1
        odd.append(num)

#Print of the output
print(f"Even numbers: {no_even} elements {even}")
print(f"Odd numbers: {no_odd} elements {odd}")