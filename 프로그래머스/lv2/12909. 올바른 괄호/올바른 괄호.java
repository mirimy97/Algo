import java.util.Deque;
import java.util.ArrayDeque;
// import java.util.Arrays;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Deque<Character> q = new ArrayDeque<Character>();
        char c;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if (c == ')' && !q.isEmpty() && q.peekLast() == '(') q.pollLast();
            else q.addLast(c);
        }
        if (!q.isEmpty()) answer = false;

        return answer;
    }
}