def isUgly(n):
        if n <= 0:
              return False
        ugly = [2, 3, 5]
        for factor in ugly:
            while n % factor == 0:
                  n //= factor
                  print(n, factor)
        return n == 1          

print(isUgly(20))