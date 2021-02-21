import numpy as np

f=open("data.fasta","r")
lines=f.readlines()
idlist=[]
dnalist=[]
flaga=0
for i in lines:

	if (i[0]=='>'):
		idlist.append(i[1:len(i)-1])
		flaga+=1
		
		if(flaga!=1):
			dnalist.append(msg)
		msg=""
	else:
		msg+=i[:len(i)-1]			

dnalist.append(msg)
lenght=len(dnalist[0])
print("We have "+str(len(dnalist))+" dna strings of len: "+str(lenght))
f.close()

profile=np.zeros((4,lenght))

print("Profile array of "+str(profile.shape))
consensus=""
for i in range(0,lenght):
	a=0
	t=0
	c=0
	g=0

	for j in range(0,len(dnalist)):
		print("i: "+str(i)+"j "+str(j))
		if(dnalist[j][i] == 'A'):
			a+=1
		elif(dnalist[j][i] == 'T'):
			t+=1
		elif(dnalist[j][i] == 'C'):
			c+=1
		elif(dnalist[j][i] == 'G'):
			g+=1
	profile[0][i]=a
	profile[1][i]=c
	profile[2][i]=g
	profile[3][i]=t
	
	if( a>=c and a>=g and a>=t):
		consensus+="A"
	elif(c>=a and c>=g and c>=t):
		consensus+="C"
	elif(g>=a and g>=c and g>=t):
		consensus+="G"
	else:
		consensus+="T"
		


print(consensus)	
for i in range(0,4):
	if(i==0):
		print("A:",end=" ")
	elif(i==1):
		print("C:",end=" ")
	elif(i==2):		
		print("G:",end=" ")
	elif(i==3):
		print("T:",end=" ")
	for j in range(0,len(dnalist[0])):
		print(int(profile[i][j]),end=" ")
	print("")


