import java.util.ArrayList;
import java.util.Arrays;

class Graph {
	public int size;
	public ArrayList<ArrayList<Integer>> neighbors;
	public Graph(int size) {
		this.size = size;
		this.neighbors = new ArrayList<ArrayList<Integer>>(size);
		for (int i = 0; i < size; i++) {
			this.neighbors.add(new ArrayList<Integer>());
		}
	}

	public void addEdge(int u, int v) {
		this.neighbors.get(u).add(v);
		this.neighbors.get(v).add(u);
	}
}

class Solution {
	public static int gcd(int a, int b) {
		if (b == 0)
			return a;
		return gcd(b, a % b);
	}
	public static boolean isInf(int a, int b) {
		// found the pattern by just listing out a bunch of cases
		// and trial and error
		
		// pattern: sum is a power of 2
		// or sum divided by gcd of 2 numbers is power of 2
		int sum = a + b;
		if ((sum & (sum - 1)) == 0)
			return false;

		int div = gcd(a, b);
		if (((sum / div) & (sum / div - 1)) == 0)
			return false;
		return true;
	}

	public static int findAugmentingPath(Graph graph, int[] match, int[] p, int root, int[] base, boolean[] mergeBases, int[] queue) {
		Arrays.fill(p, -1);
		p[root] = root;
		// use array as queue
		// queue will never overflow, can't insert more than number of nodes in graph
		int qh = 0, qt = 1;
		queue[0] = root;

		for (int i = 0; i < graph.size; i++) {
			base[i] = i;
		}

		while (qt > qh) {
			int v = queue[qh++];
			for (int w : graph.neighbors.get(v)) {
				// ignore previous vertex or vertices in same blossom
				if (base[v] == base[w] || p[v] == w)
					continue;

				if (p[w] == -1 && match[w] != -1) {
					// add new match pair to path
					p[w] = v;
					p[match[w]] = w;
					// possibly continue search later from end of match
					queue[qt++] = match[w];
				} else if (p[w] != -1) {
					// cycle found, must be handled if odd
					int n1 = w;
					int n2 = v;
					int n1Count = 1;
					int n2Count = 1;

					Arrays.fill(mergeBases, false);

					// traverse up to root
					while (n1 != root) {
						n1 = base[n1];
						n1 = p[n1];
						n1Count++;
					}
					while (n2 != root) {
						n2 = base[n2];
						n2 = p[n2];
						n2Count++;
					}

					if ((n1Count + n2Count) % 2 == 1) {
						// cycle is even, nothing to be done
						continue;
					}

					// odd length cycle must be contracted
					// to single base

					int lca = v;
					n1 = w;
					n2 = v;
					// only one of these loops will run
					while (n1Count > n2Count) {
						n1 = base[n1];
						mergeBases[n1] = true;
						n1 = p[n1];
						n1Count--;
					}

					while (n2Count > n1Count) {
						n2 = base[n2];
						mergeBases[n2] = true;
						n2 = p[n2];
						n2Count--;
					}

					while (n2 != n1) {
						n1 = base[n1];
						n2 = base[n2];
						mergeBases[n1] = true;
						mergeBases[n2] = true;
						n1 = p[n1];
						n2 = p[n2];
					}
					lca = n1;

					for (int i = 0; i < graph.size; i++) {
						if (mergeBases[i]) {
							base[i] = lca;
						}
					}
				} else if (match[w] == -1) {
					// found unmatched vertex
					// augmenting path is complete
					p[w] = v;
					return w;
				}
			}
		}
		// augmenting path was not able to be found
		return -1;
	}

	public static int[] findMaxMatching(Graph graph) {
		int[] match = new int[graph.size];
		Arrays.fill(match, -1);
		int[] p = new int[graph.size];
		Arrays.fill(p, -1);
		int[] base = new int[graph.size];
		boolean[] mergeBases = new boolean[graph.size];
		int[] queue = new int[graph.size];

		while (true) {
			boolean foundPath = false;
			for (int root = 0; root < graph.size; root++) {
				// avoid already matched vertices
				if (match[root] != -1)
					continue;
				// find path starting from root
				int v = findAugmentingPath(graph, match, p, root, base, mergeBases, queue);
				// no path was found
				if (v == -1)
					continue;
				foundPath = true;
				// augment match along augmenting path
				// check to v != root may be redundant/unnecessary
				while (v != root && v != -1) {
					int prev = p[v];
					int prevMatch = match[prev];
					match[v] = prev;
					match[prev] = v;
					v = prevMatch;
				}
			}

			// Berge's lemma: If no augmenting path is found
			// then the matching is maximum
			if (!foundPath)
				break;
		}

		return match;
	}
	
    public static int solution(int[] bananaList) {
		Graph graph = new Graph(bananaList.length);
		for (int i = 0; i < bananaList.length - 1; i++) {
			for (int j = i + 1; j < bananaList.length; j++) {
				if (isInf(bananaList[i], bananaList[j])) {
					graph.addEdge(i, j);
				}
			}
		}
		int[] match = findMaxMatching(graph);
		int matchCount = 0;
		for (int i = 0; i < match.length; i++) {
			if (match[i] != -1)
				matchCount++;
		}
		return bananaList.length - matchCount;
    }
}
