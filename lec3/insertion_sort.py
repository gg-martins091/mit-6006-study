def search(A, key, low, high):
	if high <= low: return low + 1 if key > A[low] else low

	mid = (low + high) // 2

	if key == A[mid]: return mid + 1

	if key > A[mid]:
		return search(A, key, mid + 1, high)

	return search(A, key, low, mid - 1)

def sort(A):
	for j in range(len(A)):
		if j == 0: continue
		v = A[j]
		i = j - 1

		# binary search for binary insertion sort
		#n = search(A, v, 0, j)

		#while i >= n:
		#	A[i+1] = A[i]
		#	i = i - 1
		#A[i + 1] = v
		# end binary insertion sort

		# simple isertion sort without binary search
		while i > -1 and v > A[i]:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = v
		#end simple insertion sort
	return A



import random
randomlist = random.sample(range(1, 100001), 100000)
def main():
	sorted = sort(randomlist)
        print "finished sorting"

if __name__ == "__main__":
    import profile
    profile.run("main()")
