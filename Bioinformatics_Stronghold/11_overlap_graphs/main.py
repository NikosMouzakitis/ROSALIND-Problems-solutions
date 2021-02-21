f=open("data.fasta","r")

lines=f.readlines()

idlist=[]
dnalist=[]
flaga=0
msg=""

k=3
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
dic={}
for i in range(0,len(dnalist)):
	dic[dnalist[i]]=idlist[i]
print(dnalist)
adjacency_list=[]
for seq1 in dnalist:
	for seq2 in dnalist:
		if(seq1==seq2):
			continue
		elif(seq1[0:k]==seq2[-k:]):
			adjacency_list.append([dic[seq2],dic[seq1]])

for i in range(0,len(adjacency_list)):
	print(adjacency_list[i][0],end=" ")			
	print(adjacency_list[i][1])			
