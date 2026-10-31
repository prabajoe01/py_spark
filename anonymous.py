import function as fl

# total=lambda a,b:a+b
# print(total(10,20))
# product=lambda a,b:a*b
# print(product(10,10))

# find_even=lambda x:"even" if x%2==0 else "odd"
# print(find_even(5))


# number=[1,2,3,4,5]


# # def square(n):
# #     return n*n

# map=map(lambda n:n+n,number)
# print(list(map))



# filter=filter(lambda x:x>3 ,number)
# print(list(filter))


# from functools import reduce

# total_value=reduce(lambda x,y:x*y,number)
# print(total_value)


def totalvalue(n):
    if n==1:
        return n
    
    return n*totalvalue(n-1)



print(totalvalue(5))

print(fl.demo())