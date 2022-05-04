
def merge(L, R):
	i = 0
	j = 0
	answer = []
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			answer.append(L[i])
			i += 1
		else:
			answer.append(R[j])
			j += 1


	# R finished before L so just extend L to answer
	if i < len(L):
		answer.extend(L[i:])

	if j < len(R):
		answer.extend(R[j:])

	return answer
def merge_sort(A):
	n = len(A)
	# could be == 1 because we wouldn't get to n = 0 anyway.
	if n < 2:
		return A

	mid = n // 2
	L = merge_sort(A[:mid])
	R = merge_sort(A[mid:])
	return merge(L, R)



import random
randomlist = random.sample(range(1, 100001), 100000)
def main():
	sorted = merge_sort(randomlist)
        print "finished sorting"
if __name__ == "__main__":
    import profile
    profile.run("main()")
