import os
import codecs

def AND_LOGIC(index1,index2,i):
	if index1 and index2 >= 0:
		print("Keywords found in file :" + i +" with AND LOGIC")
	else:
		pass

def OR_LOGIC(index1,index2,i):
	if index1 or index2 >= 0:
		print("Keywords found in file :" + i +" with OR LOGIC")
	else:
		pass

list=[]
keyword1=raw_input("Enter the first keyword: ")
keyword2=raw_input("Enter the second keyword: ")
for txt in os.listdir('/home/sukruti/2nd_sem/trse_assignment/corpus'):
	list.append(txt)
for i in list:
	fileExtension = i.split(".")[-1]
	if fileExtension == "txt":
		with codecs.open(i, "r",encoding='utf-8', errors='ignore') as file:
			content=file.read()
			index1=content.find(keyword1)
			index2=content.find(keyword2)
			AND_LOGIC(index1,index2,i)
			OR_LOGIC(index1,index2,i)


			


