array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5]

#Empty list created
lst = []
#Iteration through array and every unique item is added to the empty list
for i in array:
    if i not in lst:
        lst.append(i)
#array with unique items printed, with its length
length = len(lst)
print(f"Length = {length}, where the new array is {lst}")