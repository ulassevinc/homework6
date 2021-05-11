num = 19547
flag = False
if num > 1:
 
    for i in range(2, num):
        if (num % i) == 0:
            
            flag = True
            
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
    
    
start = 1
end = 72
  
for i in range(start, end+1):
    if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        else:
            print(i)
        
thelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

print(thelist[0] * thelist[1])
print(thelist[1] * thelist[2])
print(thelist[2] * thelist[3])
print(thelist[3] * thelist[4])
print(thelist[4] * thelist[5])
print(thelist[5] * thelist[6])
print(thelist[6] * thelist[7])
print(thelist[7] * thelist[8])
print(thelist[8] * thelist[9])
print(thelist[9] * thelist[10])
print(thelist[10] * thelist[11])
print(thelist[11] * thelist[12])
print(thelist[12] * thelist[13])
print(thelist[13] * thelist[14])
print(thelist[14] * thelist[15])
print(thelist[15] * thelist[16])
print(thelist[16] * thelist[17])
print(thelist[17] * thelist[18])
print(thelist[18] * thelist[19])
print(thelist[19] * thelist[20])







        


        

    
    
        