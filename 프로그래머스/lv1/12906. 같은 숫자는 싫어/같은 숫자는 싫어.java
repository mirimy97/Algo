import java.util.*;

public class Solution {
    public Deque<Integer> solution(int []arr) {
        int[] answer = {};
        Deque<Integer> q = new ArrayDeque<Integer>();
        for (int a : arr) {
            if (q.isEmpty() || q.peekLast() != a) q.addLast(a);
        }

        return q;
    }
}