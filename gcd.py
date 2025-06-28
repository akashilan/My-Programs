def gcd(n, m):
	if n == m:
		return n
	if (n ==0 and m != 0) or (m==0 and n!=0):
		return m if m!=0 else n
	if n == 0 and m == 0:
		return '0 or undefined'
	
	small, big = 0, 0
	if n < m:
		small = n
		big = m
	else:
		small = m
		big = n
	
	if big % small == 0:
		return small
	
	gcd_factor = 1
	for i in range(1, small+1):
		if small % i == 0 and big % i == 0:
			gcd_factor = i
	return gcd_factor


should_continue = 'y'
while(should_continue == 'y'):
	n = int(input("Enter n: "))
	m = int(input("Enter m:"))
	print(gcd(n,m))
	should_continue = input("Want to continue? : (y/n) ")
