input = [[1,3], [2,6], [8,10], [15,18]]

#Boolean Function to check whether elements in intervals overlap
def overlapping_check(a,b):
    if b[0] > a[0] and b[0] < a[1]:
        return True
    else:
        return False

#Function that performs merging of intervals
def overlap_merge(input):
#Empty list for new merges
    new = []
#First element of interval appended to empty list
    new.append(input[0])
#Iteration through length of input intervals
    for i in range(1,len(input)):
#New variable, that takes last number from first interval
        last = new.pop()
#If first number from new interval created overlaps with input intervals, appends the max number that fits in overlapping intervals to make new interval
        if overlapping_check(last, input[i]):
            new_input = last[0], max(last[1], input[i][1])
            new.append(new_input)
        else:
#if no overlap, the input intervals are recreated
            new.append(last)
            new.append(input[i])
    return new

print(overlap_merge(input))



