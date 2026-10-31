info={
    "name":"praba",
    "name":"joe",
    "age":23,
    "city":"pondy",
    "number":"9345367576",
    "role":"software developer"
}

print(info["name"])
print(info["city"])
info["age"]=25
print(info.get("age"))
print(info.keys())
print(info.values())
print(info.items())


for key in info:
    print(key,":",info.get(key))
    
for key ,value in info.items():
    print("key : ",key ,"value : ",value)



