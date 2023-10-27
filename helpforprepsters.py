
def find(n,k):
    
    for i in range(n+1):
        if str(bin(i)).count('1')==k:
            print(bin(i).replace('0b',''))
            
            
find(7,2)
