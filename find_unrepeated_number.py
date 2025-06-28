def is_arr_length_3_4n_type(start, end):
	return True if ((end-start+1) - 3) % 4 == 0 else False

def find_unique(arr:list)->int:
	'''list contains sorted integers where every number is repeated twice except one. 
        this function returns that unique number in log(n) time.'''
	i=0
	end = len(arr)-1
	count = 0
	while(i <= end):
		count+=1
		print(f"count: {count}")
		mid = (i+end)//2

		if mid == 0 and arr[mid] != arr[mid+1]:
			return arr[mid]
		if mid == end and arr[mid-1] != arr[mid]:
			return arr[mid]
		if arr[mid] != arr[mid+1] and arr[mid-1] != arr[mid]:
			return arr[mid]
		if is_arr_length_3_4n_type(i, end):
			
			if arr[mid] == arr[mid+1]:
				end = mid - 1
			else:
				i = mid+1
		else:
			
			if arr[mid] == arr[mid+1]:
				i = mid + 2
			else:
				end = mid -2

arr = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9]
print(find_unique(arr))











'''-----------------x----------------------'''
'''The while loop below generates array'''
'''
unique=1
while(unique!=2):
	arr = []
	for i in range(1, 65):
		if i != unique:
			arr.append(i)
			arr.append(i)
		else:
			arr.append(i)
	print(arr)
	print(find_unique(arr), f"length of array: {len(arr)}")
	unique += 1
'''
'''
length = 3 + 4n
    m
[1, 2, 2]
[1, 1, 2]
--------------------------
length = 5+4n
       m
[1, 2, 2, 3, 3]
[1, 1, 2, 2, 3]
-------------------------
length = 3+4n
          m
[1, 2, 2, 3, 3, 4, 4]
[1, 1, 2, 2, 3, 3, 4]
'''
