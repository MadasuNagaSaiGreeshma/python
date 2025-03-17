n=100
for i in range(1,100):
    if i % 2 == 0:
       if i % 4 == 0:
           print(i)      
       else:  
           print("even numbers but not multiples of 4")
    else:
         if i % 3 == 0:
             print(i)
         else:
            print("odd numbers but not multiples of 3")
