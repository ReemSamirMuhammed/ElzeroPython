#for loop
# example one

myNumber = [1,2,3,4,5,6,7,8,9]
for number in myNumber:
    
    #print( number * 17)
    
    if number % 2 == 0: #to figure out even numbers
        print (f"the number  {number} is even ")
    else: 
        print( f"the number  {number} is odd")
        
else: 
    print("the loop is finished")
    
#the second example

myName = "Rema"
for letter in myName:
    print (letter.upper())