def findDivisibleByAllTo(n, allSubDivisors):

    if(len(allSubDivisors) > n):
        print(allSubDivisors[n])
        return allSubDivisors
    
    divisor = len(allSubDivisors)
    currentNumber = allSubDivisors[-1]
    while divisor < n + 1:
        if currentNumber % divisor == 0:
            allSubDivisors.append(currentNumber)
            divisor += 1
        else:
            currentNumber += allSubDivisors[-1]
                
    print(allSubDivisors[n])
    return allSubDivisors

allSubDivisors = [0, 1, 2, 6]
                
cases = [3, 10, 11, 20, 21, 22, 23, 40]
for i in cases:
    allSubDivisors = findDivisibleByAllTo(i, allSubDivisors)
