import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Pair> pr = new PriorityQueue<Pair>();
        
        for (int i = 0; i < priorities.length; i++) {
            pr.add(new Pair(priorities[i], i));
        }
        int t = 0;
        int cnt = 1;
        while (!pr.isEmpty()) {
            int v = pr.poll().value;
            while (v != priorities[t % priorities.length]) {
                t++;
            }
            if (t % priorities.length == location) break;
            else {
                cnt++;
                t++;
            }
        }
        
        return cnt;
    }
}

class Pair implements Comparable<Pair> {
    int value;
    int index;
    
    public Pair(int value, int index) {
        this.value = value;
        this.index = index;
    }
    
    @Override
    public int compareTo(Pair other) {
        return Integer.compare(-this.value, -other.value);
    }
}