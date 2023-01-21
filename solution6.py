def solution(x, y):
	if x == y:
		return "impossible"
	x = int(x)
	y = int(y)
	count = 0
	for i in range(200):
		if x > y:
			quo, rem = divmod(x, y)
			if rem == 0:
				if y == 1:
					return str(count + quo - 1)
				else:
					return "impossible"
			else:
				x = rem
				count += quo
		elif y > x:
			quo, rem = divmod(y, x)
			if rem == 0:
				if x == 1:
					return str(count + quo - 1)
				else:
					return "impossible"
			else:
				y = rem
				count += quo
		else:
			return "impossible"
