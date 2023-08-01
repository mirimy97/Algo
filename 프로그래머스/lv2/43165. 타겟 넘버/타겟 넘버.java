class Solution {
    public int len, s, t, answer;
    public int[] nums;
    public int solution(int[] numbers, int target) {
        len = numbers.length;
        nums = numbers;
        s = 0;
        t = target;
        
        answer = 0;
        plusMinus(0);
        return answer;
    }
    
    public void plusMinus(int cnt) {
        if (cnt == len) {
            if (s == t) answer++;
        } else {
            s += nums[cnt];
            plusMinus(cnt + 1);
            s -= nums[cnt] * 2;
            plusMinus(cnt + 1);
            s += nums[cnt];
        }
    }
}