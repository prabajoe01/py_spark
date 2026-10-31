fruits=["apple","banana","kiwi","orange","watermelon"]
items=["praba",23,77.7,True,"praba"]

print(fruits[3])
fruits[3]="grape"
print(fruits)
print(items)
print(len(items))

print(type(fruits))

for item in items:
    print(item)
    
    
print(items.append("Python"))
print(items.insert(0,"ocean academy"))
print(items.pop())
print(items.extend(fruits))
print(items.remove(True))
print(items.index(23))
print(items.count("praba"))

# print(items.clear())
num=[2,6,3,8,7,0,19,22,11]
print(num)
print(num.sort())
print(num)
print(num.reverse())
print(num)
num2=num.copy()
print(num2)
print(items)
print(sum(num2))
print(max(num2))
print(min(num2))

name="joe"

name_list=list(name)
print(name_list)

