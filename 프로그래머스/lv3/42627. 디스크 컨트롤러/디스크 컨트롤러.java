import java.util.PriorityQueue;
import java.util.ArrayList;
class Solution {
    public int solution(int[][] jobs) {
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
        ArrayList<Pair> arr = new ArrayList<Pair>();
        int t = 1001;
        for (int[] j : jobs) {
            pq.add(new Pair(j[0], j[1]));
            t = Math.min(t, j[0]);
        }
        int answer = 0;
        while (!pq.isEmpty()) {
            Pair p = new Pair(0, 0);
            while (!pq.isEmpty()) {
                // 뽑고
                p = pq.poll();
                // 아니면 다시 넣기
                if (p.start > t) arr.add(p);
                else {
                    for (Pair a : arr) {
                        pq.add(a);
                    }
                    arr.clear();
                    break;
                };
                
                if (pq.isEmpty()) {
                    for (Pair a : arr) {
                        pq.add(a);
                    }
                    arr.clear();
                    t++;
                }
            }
            answer += (t - p.start) + p.time;
            // System.out.println(p.time);
            // System.out.println(answer);
            t += p.time;

        }
        answer /= jobs.length;
        return answer;
    }
}

class Pair implements Comparable<Pair> {
    int start;
    int time;
    
    public Pair(int start, int time) {
        this.start = start;
        this.time = time;
    }
    
    @Override
    public int compareTo(Pair other) {
        return Integer.compare(this.time, other.time);
    }
}