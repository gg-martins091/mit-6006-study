from datetime import datetime
d = [y for y in range(100000000)]
start_time = datetime.now()
def check(a):
	s = len(a)//2 
	if len(a) == 2:
		if (a[0] >= a[1]): return a[0]
		else: return a[1]

	if len(a) == 1: return a[0]

	if a[s] < a[s-1]:
		return check(a[:s])
	elif a[s] < a[s+1]:
		return check(a[s+1:])
	else:
		return a[s]
print("Ans:" ,check(d))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
