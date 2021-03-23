#Task1
x = lambda a, b : a.title()+'(firstname)' + b+'(Last Name)' 

a=input('First Name=')
b=input('First Name=')
print(x(a,b))

# list=[1,2.....10]
# list**3=[1,8,27....1000]

#3
cub=lambda x:x**3
n=[1,2,3,4,5,6,7,8,9,10]
cub_n=[]

for i in n:
  result=cub(i)
  cub_n.append(result)
print(cub_n)