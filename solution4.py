import copy

def lu_decomp(m):
	p = []
	for i in range(len(m) + 1):
		p.append(i)
	for i in range(len(m)):
		max_i = i
		max_val = absRational(m[i][i])
		for k in range(i, len(m)):
			if gtRational(absRational(m[k][i]), max_val):
				maxVal = absRational(m[k][i])
				max_i = k

		if max_i != i:
			tmp = p[i]
			p[i] = p[max_i]
			p[max_i] = tmp

			tmp = m[i]
			m[i] = m[max_i]
			m[max_i] = tmp

			p[len(m)] += 1

		for j in range(i + 1, len(m)):
			m[j][i] = divRational(m[j][i], m[i][i])

			for k in range(i + 1, len(m)):
				m[j][k] = subRational(m[j][k], mulRational(m[j][i], m[i][k]))

	return p

def inverse(m):
	m = copy.deepcopy(m)
	p = lu_decomp(m)
	inv = []
	for i in range(len(m)):
		row = []
		inv.append(row)
		for j in range(len(m)):
			row.append(Rational(0, 1))

	for j in range(len(m)):
		for i in range(len(m)):
			if (p[i] == j):
				inv[i][j] = Rational(1, 1)
			for k in range(i):
				inv[i][j] = subRational(inv[i][j], mulRational(m[i][k], inv[k][j]))

		for i in range(len(m) - 1, -1, -1):
			for k in range(i + 1, len(m)):
				inv[i][j] = subRational(inv[i][j], mulRational(m[i][k], inv[k][j]))

			inv[i][j] = divRational(inv[i][j], m[i][i])

	return inv

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def mul(a, b):
	out = []
	for i in range(len(a)):
		row = []
		out.append(row)
		for i in range(len(b[0])):
			row.append(Rational(0, 1))
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				out[i][j] = addRational(out[i][j], mulRational(a[i][k], b[k][j]))
	return out
	
def addRational(r0, r1):
	g = gcd(r0.bottom, r1.bottom)
	a = r0.bottom // g
	b = r1.bottom // g
	return Rational(r0.top * b + r1.top * a, r0.bottom * b)

def subRational(r0, r1):
	g = gcd(r0.bottom, r1.bottom)
	a = r0.bottom // g
	b = r1.bottom // g
	return Rational(r0.top * b - r1.top * a, r0.bottom * b)

def mulRational(r0, r1):
	top = r0.top * r1.top
	bottom = r0.bottom * r1.bottom
	divAmt = gcd(top, bottom)
	return Rational(top // divAmt, bottom // divAmt)

def divRational(r0, r1):
	top = r0.top * r1.bottom
	bottom = r0.bottom * r1.top
	divAmt = gcd(top, bottom)
	return Rational(top // divAmt, bottom // divAmt)

def negRational(r0):
	return Rational(-r0.top, self.bottom)

def gtRational(r0, r1):
	g = gcd(r0.bottom, r1.bottom)
	a = r0.bottom // g
	b = r1.bottom // g
	return r0.top * b > r1.top * a

def absRational(r):
	return Rational(abs(r.top), r.bottom)

class Rational:
	def __init__(self, numerator, denominator):
		g = gcd(numerator, denominator)
		self.top = numerator // g;
		self.bottom = denominator // g;

	def __str__(self):
		return str(self.top) + "/" + str(self.bottom)

	def __repr__(self):
		return str(self.top) + "/" + str(self.bottom)

def solution(m):
	terminal = []
	nonterminal = []
	for index, state in enumerate(m):
		for prob in state:
			if prob != 0:
				nonterminal.append(index)
				break
		else:
			terminal.append(index)
	if terminal[0] == 0:
		result = [1]
		for i in range(len(terminal) - 1):
			result.append(0)
		result.append(1)
		return result

	for row in m:
		row_sum = sum(row)
		if row_sum == 0:
			row_sum = 1
		for i, c in enumerate(row):
			row[i] = Rational(c, row_sum)

	fundamental = []
	for i in range(len(nonterminal)):
		row = []
		fundamental.append(row)
		for j in range(len(nonterminal)):
			ident = Rational(0, 1)
			if i == j:
				ident = Rational(1, 1)
			row.append(subRational(ident, m[nonterminal[i]][nonterminal[j]]))

	inv = inverse(fundamental)

	r = []
	for i in nonterminal:
		row = []
		r.append(row)
		for j in terminal:
			row.append(m[i][j])

	absorption = mul(inv, r)
	result = []
	curr = 1
	for prob in absorption[0]:
		curr = curr * prob.bottom // gcd(curr, prob.bottom)

	for prob in absorption[0]:
		result.append(prob.top * curr // prob.bottom)

	result.append(curr)
	return result
