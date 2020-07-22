l1 = [1,3,4,5]
l2 = [3,4,5,7,8]

out = [1,3,3,4,5,5,7,8]

def merge2lists(l1,l2):
	expexted_out = []
	p1 = 0
	p2 = 0
	while(p1<len(l1) and p2<len(l2)):
		if(l1[p1]<l2[p2]):
			expexted_out.append(l1[p1])
			p1+=1
		elif(l1[p1]>l2[p2]):
			expexted_out.append(l2[p2])
			p2+=1
		else:
			expexted_out.append(l1[p1])
			expexted_out.append(l2[p2])
			p1+=1
			p2+=1

	while(p1<len(l1)):
		expexted_out.append(l1[p1])
		p1+=1

	while(p2<len(l2)):
		expexted_out.append(l2[p2])
		p2+=1
	
	# print(expexted_out)
	return expexted_out

print(merge2lists(l1,l2))