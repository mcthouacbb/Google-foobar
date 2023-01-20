# PROBLEM # 2
def search(root, val):
	prev = -1
	left = 1
	counter = 0
	right_move = (root + 1) // 2
	while root != val:
		prev = root
		span = root - left
		mid = left + span // 2
		if val >= mid:
			left = mid
			root -= 1
		else:
			root -= right_move
		right_move >>= 1
	return prev

def solution_problem2(h, q):
	# Your code here
	root_val = (1 << h) - 1
	result = []
	for n in q:
		result.append(search(root_val, n))
	return result
