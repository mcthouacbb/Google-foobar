INT_MAX = int(0xFFFFFFFF)

def bellman_ford(times, src, distance):
	n = len(times)
	for i in range(n):
		distance[i] = INT_MAX
	distance[src] = 0
	for i in range(n - 1):
		for u in range(n):
			for v in range(n):
				if u == v:
					continue
				w = times[u][v]
				if distance[u] + w < distance[v]:
					distance[v] = distance[u] + w

	for u in range(n):
		for v in range(n):
			if u == v:
				continue
			w = times[u][v]
			if distance[u] + w < distance[v]:
				return True
	return False

def dfs(result, times, distances, curr_time, node, visited, prev_nodes):
	if node == len(times) - 1:
		res = []
		j = 0
		for i in range(1, len(times) - 1):
			if visited[i] > 0:
				res.append(i - 1)
		if len(res) == len(times) - 2:
			result[0] = res
			return True
		if len(res) > len(result[0]):
			result[0] = res
		if len(res) == len(result[0]):
			for i in range(len(res)):
				if res[i] < result[0][i]:
					result[0] = res
					break

	for i in range(node + 1, len(times)):
		if i == node:
			continue
		if curr_time - times[node][i] < distances[i][len(times) - 1]:
			continue

		for j in range(len(prev_nodes) - 1, -1, -1):
			if prev_nodes[j] == i:
				break

		
		hasLoop = False
		for k in range(j):
			if prev_nodes[k] == i and prev_nodes[k + len(prev_nodes) - j] == i:
				match = True
				for l in range(len(prev_nodes) - j):
					if prev_nodes[k + l] != prev_nodes[j + l]:
						break
				else:
					hasLoop = True
					break

		if hasLoop:
			continue

		prev_nodes.append(i)
		visited[i] += 1
		if dfs(result, times, distances, curr_time - times[node][i], i, visited, prev_nodes):
			return True
		visited[i] -= 1
		prev_nodes.pop()
		
	for i in range(0, node):
		if i == node:
			continue
		if curr_time - times[node][i] < distances[i][len(times) - 1]:
			continue

		for j in range(len(prev_nodes) - 1, -1, -1):
			if prev_nodes[j] == i:
				break

		hasLoop = False
		for k in range(j):
			if prev_nodes[k] == i and prev_nodes[k + len(prev_nodes) - j] == i:
				match = True
				for l in range(len(prev_nodes) - j):
					if prev_nodes[k + l] != prev_nodes[j + l]:
						break
				else:
					hasLoop = True
					break

		if hasLoop:
			continue

		prev_nodes.append(i)
		visited[i] += 1
		if dfs(result, times, distances, curr_time - times[node][i], i, visited, prev_nodes):
			return True
		visited[i] -= 1
		prev_nodes.pop()
	
	return False

def solution(times, times_limit):
	distances = []
	n = len(times)
	for i in range(n):
		row = []
		distances.append(row)
		for j in range(n):
			row.append(-1)
		if bellman_ford(times, i, row):
			result = []
			for i in range(n - 2):
				result.append(i)
			return result
			
	if times_limit < distances[0][n - 1]:
		return []
	visited = []
	for i in range(n):
		visited.append(0)
	# outer array is for pass-by-reference
	result = [[]]
	prev_nodes = [0]
	dfs(result, times, distances, times_limit, 0, visited, prev_nodes)
	return result[0]
