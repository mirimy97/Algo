class Solution {
    public int[] solution(int brown, int yellow) {
        // yellow = a * b
        // (brown - 4) = 2 * (a + b)
        brown = (brown - 4) / 2;
        int a = 0;
        int b = 0;
        for (a = 0; a <= brown / 2; a++) {
            b = brown - a;
            if (a * b == yellow) break;
        }
        int[] answer = {b+2, a+2};
        return answer;
    }
}