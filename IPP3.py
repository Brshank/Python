x=int(input('Quantity of items u want='))
cp=x*100
if cp>1000:
    print('After discount now the, total value=',(cp-cp/10))
 else:
     print('Discount not available, total value=',cp)

a=int(input('Enter Marks='))
if a<25:
    print('F')
elif 25<a<=45:
    print('E')
elif 45<a<=50:
    print('D')
elif 50<a<=60:
    print('C')
elif 60<a<=80:
    print('B')
elif a>80 :
    print('A')


a=int(input('Enter Age='))
g,m=map(str,input('enter age, gender ( M or F ), marital status ( Y or N )=').split())
if g=='F':
    print('You will work in Urban Areas')
elif g=='M' and 20<a<=40 :
    print('you may work anywhere')
elif g=='M' and 40<a<=60 :
    print('you may work in urban areas only')
else:
    print('"ERROR"')

    
year
d,m,y=map(str,input('Enter DD MM YYYY=').split())


print('Next day is',nxt)

l=[1,2,3,4,5,6,7,8,9,12,17,33,24,10] #no.of elem is 14
l1=[] #even 2,4,6,8,10,12,24,
l2=[] #odd 1,3,5,7,9,17,33

for i in l :
    if i % 2==0:
        l1.append(i)
    else:
        l2.append(i)

print('l1=',l1)
print('l2=',l2)


x=int(input('Enter Your Number to check for armstrong number='))
l=[1452, 11.23, 1+2j, True, 'Mumbai', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in l:
    print(i)
    