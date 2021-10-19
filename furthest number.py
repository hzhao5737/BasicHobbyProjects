#finds number furthest from numbers in list between 0 and 9999
numbers = [9635,309,6765,7485,2378,310,7950,4612,5103,7532,9010,7425,1012,3786
           ,1234,4165,3348,5678,6184,6349,5224,8214,3749,2565,7036,8412,3501,
           2485,5573,3750,4712,6592,7523,2805,1012,3567,9696,6969,6275,6046,
           7072,2500,9635,5847,3500,6765,4612,7950]
numbers.sort()
i=0
distance = numbers[i]
j=0
first = True
last = False
while i < len(numbers)-1:
    if(numbers[i+1] - numbers[i])/2 > distance:
        distance = (numbers[i+1] - numbers[i])/2
        j = i
        first = False
    i += 1
if(9999 - numbers[i]) > distance:
    first = False
    last = True
if(first):
    output = distance - 1
elif(last):
    output = numbers[i] + 1
else:
    output = numbers[j] + distance
print(output)
