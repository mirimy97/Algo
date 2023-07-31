import java.util.Arrays;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.HashSet;
class Solution {
    public int len;
    public int[] nums;
    public int[] q;
    public int[] v;
    public int cnt;
    public HashSet<Integer> set = new HashSet<Integer>();
    public int solution(String numbers) {
        len = numbers.length();
        nums = new int[len];
        for (int i = 0; i < len; i++) {
            nums[i] = Character.getNumericValue(numbers.charAt(i));
        }
        q = new int[len];
        v = new int[len];
        cnt = 0;
        for (int j = 1; j < len + 1; j++) {
            perm(j, 0);
        }
        for (int s : set) isPrime(s);
        return cnt;
    }
    
    public void isPrime(int n) {
        if (n == 0 || n == 1) return;
        if (n == 2 || n == 3) {
            cnt++;
            return;
        }
        for (int i = 2; i <= (int) Math.sqrt(n); i++) {
            if (n % i == 0) return;
        }
        cnt++;
        return;
    }
    
    public void perm(int k, int cnt) {
        // System.out.println(Arrays.toString(q));
        // System.out.println(Arrays.toString(v));
        if (cnt == k) {
            int ja = 0;
            int result = 0;
            while (ja < k) {
                result += q[ja] * (int) Math.pow(10, ja);
                ja++;
            }
            set.add(result);
        } else {
            for (int i = 0; i < len; i++) {
                if (v[i] == 0) {
                    v[i] = 1;
                    q[cnt] = nums[i];
                    perm(k, cnt + 1);
                    v[i] = 0;
            }

        }    
            
        }
        
        return;
    }
}