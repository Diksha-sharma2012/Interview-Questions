# Print 1 to 100 if a number is multiple of 3 print "Fizz", if the number is multiple of 5 print "Buzz" and if the number is multiple of both 3 and 5 then print "FizzBuzz".
for i in range (1,101):   
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")    
    elif i%3 == 0 :
        print("Fizz")
    else:
        print(i)    
        
