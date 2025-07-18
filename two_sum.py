def two_sum(arr, target):
	'''Given a list and target, this function finds the positions of two elements such that the addition of which equals the target without using inbuilt methods.'''
	mapp = {}
	for i in range(len(arr)):
		if target - arr[i] in mapp:
			for j in mapp:
				if target - arr[i] == j:
					return [mapp[j], i]
		else:
			mapp[arr[i]] = i
	return [-1, -1]
arr = [1, 2, 3, 4, 5 ,6, 7]
print(two_sum(arr, 12))
