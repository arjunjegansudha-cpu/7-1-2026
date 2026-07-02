list=[4,5,1,2,9,7,10,8]
print("original list:",list)
sum=0
for i in list:
    sum=sum+i
print("sum=",sum)
avg=sum/len(list)
print("Average=",avg)
list.sort()
print("smallest element is:",list[0])
print("Largest element is:",list[-1])