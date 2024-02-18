#given three arrays, we have to find common elements in three sorted lists using sets

s1=[1,5,10,20,40,80]
s2=[6,7,20,80,100]
s3=[3,4,15,20,30,70,80,120]

#type cast to set
s1_set=set(s1)
s2_set=set(s2)
s3_set=set(s3)

#finding common elements
s1s2=s1_set.intersection(s2)
s1s2s3=s1s2.intersection(s3)

#type cast to list
final_list=list(s1s2s3)
print(final_list)

