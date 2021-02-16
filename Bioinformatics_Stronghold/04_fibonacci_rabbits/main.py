n=36
k=4
cnt=0
seq=[]

for i in range(1,n+1):
	print(cnt)
	if i == 1:
		cnt+=1
		seq.append(1)
	elif i == 2:
		cnt=1
		seq.append(1)
	else:
		cnt = seq[i-3]*k+seq[i-2]
		seq.append(cnt)
print(cnt)
