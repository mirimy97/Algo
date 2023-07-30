import java.util.Deque;
import java.util.ArrayDeque;
import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        Deque<Integer> q = new ArrayDeque<Integer>();
        
        int  day;
        for (int i = 0; i < speeds.length; i++) {
            day = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
            if (!q.isEmpty() && q.peekFirst() < day) {
                answer.add(q.size());
                q.clear();
            }
            q.addLast(day);
        }
        if (!q.isEmpty()) answer.add(q.size());
        return answer;
    }
}