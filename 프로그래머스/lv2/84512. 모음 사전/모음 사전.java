class Solution {
    public char[] chars = {'A', 'E', 'I', 'O', 'U'};
    public int len, count, answer;
    public String result = "";
    public String w;
    public int solution(String word) {
        len = word.length();
        w = word;
        count = 0;
        answer = 0;
        perm(0);
        return answer;
    }
    
    public void perm(int cnt) {
        if (result.equals(w)) {
            answer = count;
            return;
        }
        if (cnt == 5 || answer != 0 ) return;

        for (char c : chars) {
            result += String.valueOf(c);
            count++;
            perm(cnt + 1);
            result = result.substring(0, cnt);
        }
    }
}