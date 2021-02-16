def gc_content_calc(s):
#calculation of GC content
	nuc=['A','G','C','T']
	cnt=0	

	for i in range (0,len(s)):
		if( (s[i]=='C') or (s[i] =='G') ):
			cnt+=1
	return (float(cnt)/float(len(s)))*100

f=open("data.fasta","r")

lines=f.readlines()

idlist=[]
dnalist=[]
flaga=0
msg=""

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

gc_content=[]

for i in dnalist:
	gc_content.append(gc_content_calc(i))

meg=0
for i in range(0,len(gc_content)):
	if(gc_content[i]>gc_content[meg]):
		meg=i

f.close()

print(idlist[meg])
print(gc_content[meg])



