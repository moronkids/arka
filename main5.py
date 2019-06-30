x = str(input())
data = x.split('0',)

i=0
bucket=[]
for loop in data:
    res = [int(z) for z in str(data[i])]
    res.sort()
    bucket.append(res)
    # print(res)
    i=i+1

list1 = bucket
str1 = "".join(str(e) for e in list1)

i=0
a=[]
for x in list1:
    z= ""
    if i < len(list1):
        list2 = list1[i]
        x = "".join(str(e) for e in list2)
        z = z+x
        a.append(z)
    i=i+1
x = "".join(str(e) for e in a)
print(x)
