
print("start")

class AgeInvalidException(Exception):
    pass

try:
    age=int(input("enter the age : "))
    
    print(age)
    if age<0 or age>100:
      raise AgeInvalidException("enter the valid age")

except Exception as e:
    print(e)
    print(type(e))
    
else:
    print("execution is done")
     
finally:
    print("i execute the whether error occur or not ")
    

    

  

    



print("end")