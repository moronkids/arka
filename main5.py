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
print(bucket)
list1 = bucket
str1 = ''.join(str(e) for e in list1)
print(str(str1))
