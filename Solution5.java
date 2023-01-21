public class Solution {
    public static int solution(int[] l) {
        int count = 0;
        for (int i = 0; i < l.length - 2; i++) {
            int li = l[i];
            for (int j = i + 1; j < l.length - 1; j++) {
                int lj = l[j];
                if (lj % li != 0)
                    continue;
                for (int k = j + 1; k < l.length; k++) {
                    int lk = l[k];
                    if (lk % lj != 0)
                        continue;
                    count++;
                }
            }
        }
        return count;
    }
}
