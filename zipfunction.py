list1=[1,2,3]

list2=['a','b','c']

list3=['x','y','z']

zipped_list=zip(list1,list2,list3)

result=list(zipped_list)

print(result)

unzipped_list=zip(*result)

unzipped_result=[print(list(item)) for item in unzipped_list]

#print(unzipped_list)