

population=[18233, 19716, 17394, 17386, 17990, 19729]
#population=[1, 0, 0, 1, 0, 1]
mult=[1,1,1,0.75,0.5,0]

exp=0
for i in range(0,6):
	exp+= 2*mult[i]*population[i]
print("exp: "+str(exp))
