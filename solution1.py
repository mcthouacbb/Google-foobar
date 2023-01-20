def solution(str):
	chars = list(str);
	for i, c in enumerate(chars):
		if c.isalpha() and c.islower():
			chars[i] = chr(ord('a') + ord('z') - ord(c))
	return "".join(chars)
