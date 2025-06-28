def is_perfect_number(num:int) -> bool:
	'''Returns True if the input number is a perfect number(A number is a perfect number if the sum of the factors of the number, 
  except the number itself, is equal to the number). Otherwise False'''
	factors = [i for i in range(1, num//2+1) if num%i==0]
	sum = 0
	for factor in factors:
		sum += factor
	return True if sum == num else False

ch='y'
while(ch == 'y'):
	num = int(input("Enter num"))
	print(is_perfect_number(num))
	ch = str(input("Want to continue? y/n"))
