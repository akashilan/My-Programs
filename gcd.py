def gcd(n, m):
	if n == m:
		return n

	if (n ==0 and m != 0) or (m==0 and n!=0):
		return abs(m) if m!=0 else abs(n)

	if n == 0 and m == 0:
		return '0 or undefined'
	
	small, big = 0, 0
	if n < m:
		small, big= n, m
	else:
		small, big = m, n
  	
	if big % small == 0:
		return small

	for i in range(small, 0, -1):
		if small % i == 0 and big % i == 0:
			return i


should_continue = 'y'
while(should_continue == 'y'):
	n = int(input("Enter n: "))
	m = int(input("Enter m:"))
	print(gcd(n,m))
	should_continue = input("Want to continue? : (y/n) ").lower()
