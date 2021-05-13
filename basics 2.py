a={6,7,8,9,10}
b={5,6,7,8,9}
a.add(4)
print(a)
b.add(3)
print(b)
x=a.union(b)
print(x)
y=a.difference(b)
print(y)
p=a.intersection(b)
print (p)


lst=[11,100,99,1000,999,99]
lst.insert(0,-1)
print(lst)
print(lst[1])
lst.count(99)
# print(sum)   print sum of num in the list
# print(min(lst))   print min



e=range(2020,2070)
for x in e:
    if x%4==0:
        print(x)

x=range(1000,2000)
for s in x:
    if s%7==0 and s%5!=0:
        print(s)

# t=range(1,10)  count num in the range(1,10)
# for r in t:
#     r.count()
#         print(r)
#

d=range(30,50)
for num in d:
    if num%2!=0:
        print(num)

x=[]
r=range(100,200)
for i in r:
    if i%7==0:
        x.append(i)
print(x)


t=range(1,50)
for s in t:
    if s%3==0:
        print("purple")
    elif(s%5==0):
        print("white")
    elif s%3==0 and s%5==0:
        print(s)
    else:
        print(s)

