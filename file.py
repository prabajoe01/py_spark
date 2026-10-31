# file=open("D:\\py_spark\\demo.txt","x")
# file=open("D:\\py_spark\\demo.txt","w")
# file=open("D:\\py_spark\\demo.txt","a")
# file=open("D:\\py_spark\\demo.txt","w")

# file.write("\ni love java")

# reader=file.read()
# print(reader)

# file.close()

with open("D:\\py_spark\\demo.txt","r") as fl:
     print( fl.read())
    

# import os

# if os.path.exists("D:\\py_spark\\demo.txt"):
#     print("file existed")
#     os.remove("D:\\py_spark\\demo.txt")
# else:
#     print("file is not existed")
