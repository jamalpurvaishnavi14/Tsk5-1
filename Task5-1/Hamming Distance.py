class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

       
        longer = len(bin(y))-2 
        if x > y: longer = len(bin(x))-2
		 
            
       
        x, y, count = format(x, '0b').zfill(longer), format(y, '0b').zfill(longer), 0 
        for i in range(len(x)):
            if x[i] != y[i]: count += 1
        return count

        
        xor = x ^ y 
        ham = 0 
        while xor != 0: 
            ham += xor % 2 
            xor >>= 1 
        return ham
