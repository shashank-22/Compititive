#[1,7,3,5,5,4,6,8]
#k=10


from collections import defaultdict

def addUptoaNumber(nums,k):
	hashmap = defaultdict(lambda:0)

	for num in nums:
		# print(hashmap)
		if(k-num in hashmap):
			print(num,k-num)
			if(hashmap[num-k]==1):
				hashmap.pop(num-k)
		else:
			hashmap[num]+=1

numbers = [1,7,3,5,5,4,6,8,4,6,4,6]
k=10

addUptoaNumber(numbers,k)