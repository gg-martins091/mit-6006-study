from datetime import datetime

d = [y for y in range(100000000)]
start_time = datetime.now()
for i in range(len(d)):
	#print(d[i])
	if i == 0 and d[i] >= d[i+1]:
		print(i)
		break
	if i == len(d) - 1 and d[i] >= d[i-1]:
		print(i)
		break

	if d[i] >= d[i-1] and d[i] >= d[i+1]:
		print(i)
		break


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
