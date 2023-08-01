import java.util.Deque;
import java.util.ArrayDeque;
import java.util.HashMap;
class Solution {
    int len;
    public int solution(String begin, String target, String[] words) {
        len = begin.length();
        int wlen = words.length;
        HashMap<String, Integer> v = new HashMap<String, Integer>();
        Deque<String> q = new ArrayDeque<String>();
        q.add(begin);
        v.put(begin, 0);
        for (int i = 0; i < wlen; i++) {
            v.put(words[i], 0);
        }
        if (!v.containsKey(target)) return 0;

        String s = begin;
        String n = "0";
        while (!q.isEmpty() && v.get(target) == 0) {
            s = q.pollFirst();
            for (int i = 0; i < wlen; i++) {
                n = words[i];
                if (change(s, n) && v.get(n) == 0) {
                    v.put(n, v.get(s) + 1);
                    q.add(n);
                }
            }
        }
        int answer = 0;
        if (v.get(target) != 0) answer = v.get(target);
        return answer;
    }
    
    public boolean change(String a, String b) {
        int cnt = 0;
        for (int j = 0; j < len; j++) {
            if (a.charAt(j) == b.charAt(j)) cnt++;
        }
        if (cnt == len - 1) return true;
        return false;
    }
}