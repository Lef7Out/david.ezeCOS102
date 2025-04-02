
print("Izifin Technology Annual Tax Revenue(ATR) allocator")

age = int(input("Enter your age:"))
exp = int(input("How many years have you worked with us:"))

if age >= 55 and exp > 25:
    print("YOUR ATR FOR THIS YEAR IS N5,600,000.")
    
elif age >= 45 and exp >20 :
    print("YOUR ATR FOR THE YEAR IS N4,480,000")
    
elif age >= 35 and exp > 10:
    print("YOUR ATR FOR THE YEAR IS N1,500,000")

elif age < 35 and exp < 10 :
    print("YOUR ATR FOR THE YEAR IS N550,000") 

else:
    print("YOUR ATR FOR THE YEAR IS N550,000") 
