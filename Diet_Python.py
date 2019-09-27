#D:\\ML_Python\\Diet_Record\\db
import os
print("Welcome to the Health Managment System")
c=int(input("SElect any one:\n1.Add a new client\n2.Open existing client file\n------->"))
if c==1:
	name=input("Enter the name of the client:")
	name="D:\\ML_Python\\Diet_Record\\db\\"+name+".txt"
elif c==2:
	import os
	l=os.listdir("D:\\ML_Python\\Diet_Record\\db")
	print("Exixting clients are:")
	n=1
	#sprint(l)
	for i in l:
		print(n,".",i.split(".txt")[0])
		n+=1
	num=int(input("Chose the file no.:"))
	name=l[num-1]#file name already include .txt
	name="D:\\ML_Python\\Diet_Record\\db\\"+name
else:
	print("You Entered Wrong choice!")
	os._exit(1)
#time.asctime(time.localtime(time.time()))          gives current timereturn string
import time
#print(name)
f=open(name,'a+')
while True:
	c=int(input("Select any one:\n1.Add Diet intake\n2.Add exercise done\n------->"))
	if c==1:
		tfood=""#tfood=totalfood
		while True:
			food=input("Enter the food taken:")
			t=time.asctime(time.localtime(time.time()))
			tfood=tfood+food+","
			choice=input("Want to enter more diet<Y/N>:")
			if choice=='Y' or choice=='y':
				pass
			else:
				tfood=tfood+" taken at "+t+"\n"
				f.write(tfood)
				break
	elif c==2:
		tex=""#tex=totalexercise
		while True:
			ex=input("Enter the type of exercise done:")
			t=time.asctime(time.localtime(time.time()))
			tex=tex+ex+","
			choice=input("Want to enter more Exercise<Y/N>:")
			if choice=='Y' or choice=='y':
				pass
			else:
				tex=tex+" exercise done at "+t+"\n"
				f.write(tex)
				break
	else:
		print("You Entered Wrong choice!")
		os._exit(1)
	q=input("Want to add more info<Y/N>:")
	if q=='Y' or q=='y':
		pass
	else:
		break

print("\n")
f.seek(0)
data=f.read()
print(data)
f.close()