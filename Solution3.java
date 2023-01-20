import java.util.ArrayList;

class Solution {
	public static boolean inRange(int pos) {
		return pos >= 0 && pos <= 7;
	}
	public static int solution(int src, int dest) {
		if (src == dest)
			return 0;
		boolean[] map = new boolean[64];
		ArrayList<Integer> currNodes = new ArrayList<Integer>();
		currNodes.add(src);
		map[src] = true;
		int steps = 1;
		while (true) {
			ArrayList<Integer> newNodes = new ArrayList<Integer>();
			for (int i = 0; i < currNodes.size(); i++) {
				int x = currNodes.get(i) & 7;
				int y = currNodes.get(i) >> 3;
				if (inRange(x + 2) && inRange(y + 1)) {
					int pos = (x + 2) | ((y + 1) << 3);
					if (pos == dest) {
						return steps;
					}
					if (!map[pos]) {
						map[pos] = true;
						newNodes.add(pos);
					}
				}
				if (inRange(x + 2) && inRange(y - 1)) {
					int pos = (x + 2) | ((y - 1) << 3);
					if (pos == dest) {
						return steps;
					}
					if (!map[pos]) {
						map[pos] = true;
						newNodes.add(pos);
					}
				}
				if (inRange(x - 2) && inRange(y + 1)) {
					int pos = (x - 2) | ((y + 1) << 3);
					if (pos == dest) {
						return steps;
					}
					if (!map[pos]) {
						map[pos] = true;
						newNodes.add(pos);
					}
				}
				if (inRange(x - 2) && inRange(y - 1)) {
					int pos = (x - 2) | ((y - 1) << 3);
					if (pos == dest) {
						return steps;
					}
					if (!map[pos]) {
						map[pos] = true;
						newNodes.add(pos);
					}
				}
				if (inRange(x + 1) && inRange(y + 2)) {
					int pos = (x + 1) | ((y + 2) << 3);
					if (pos == dest) {
						return steps;
					}
					if (!map[pos]) {
						map[pos] = true;
						newNodes.add(pos);
					}
				}
				if (inRange(x - 1) && inRange(y + 2)) {
					int pos = (x - 1) | ((y + 2) << 3);
					if (pos == dest) {
						return steps;
					}
					if (!map[pos]) {
						map[pos] = true;
						newNodes.add(pos);
					}
				}
				if (inRange(x + 1) && inRange(y - 2)) {
					int pos = (x + 1) | ((y - 2) << 3);
					if (pos == dest) {
						return steps;
					}
					if (!map[pos]) {
						map[pos] = true;
						newNodes.add(pos);
					}
				}
				if (inRange(x - 1) && inRange(y - 2)) {
					int pos = (x - 1) | ((y - 2) << 3);
					if (pos == dest) {
						return steps;
					}
					if (!map[pos]) {
						map[pos] = true;
						newNodes.add(pos);
					}
				}
			}

			currNodes = newNodes;
			steps++;
		}
	}
}
