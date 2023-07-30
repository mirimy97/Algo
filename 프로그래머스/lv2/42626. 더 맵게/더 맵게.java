import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pr = new PriorityQueue<Integer>();
        
        for (int s : scoville) pr.add(s);
        
        int less1, less2;
        int cnt = 0;
        while (pr.size() > 1) {
            less1 = pr.poll();
            less2 = pr.poll();
            if (less1 >= K && less2 >= K) break;
            pr.add(less1 + (less2 * 2));
            cnt++;
        }
        if (!pr.isEmpty() && pr.poll() < K) cnt = -1;
        
        return cnt;
    }
}