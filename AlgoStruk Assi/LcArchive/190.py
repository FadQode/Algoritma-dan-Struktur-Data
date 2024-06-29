#190   
def reverseBits(n):
    result = 0
    for i in range(32):
        result <<= 1
        #explain //
        result |= n & 1
        n >>= 1
    return result

# Test the function
print(reverseBits(43261596))  # Output: 964176192