tries = 4 
mainPassword = "Reem123"

inputPassword = input("write your password:")

while inputPassword != mainPassword:
    
    tries -=1
    
    print(f"wrong password, {'last'if tries == 0 else tries} chance left")
    
    inputPassword = input("write your password:")
    
    if tries == 0:
        
        print("All Tries is Finished.")
        
        break
    
        print("All Tries is Finished.")
else:
    print("correct password")
    
    
    