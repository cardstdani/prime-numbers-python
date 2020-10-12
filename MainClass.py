numberToCheck = 7

def isPrimeNumber(n):
    if (n < 1):
        return False
    else:
        for i in range(2, n):
            if (n % i == 0):
                return False
        return True

def isMersennePrimeNumber(n):
  return isPrimeNumber(2 ** n - 1)

def isPerfectNumber(n):
    sum = 0
    for i in range(1, n):
        if (n % i == 0):
            sum += i
    return sum == n

print(isPrimeNumber(numberToCheck))
print(isMersennePrimeNumber(numberToCheck))
print(isPerfectNumber(numberToCheck))
