import java.util.HashMap;

class Solution {
    public int solution(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        //  System.out.println(map.containsKey(1));   // true
        
        for (int i = 0; i < nums.length; i++) {
            // if (map.containsKey(nums[i])) map
            int pre = map.get(nums[i]) == null ? 0 : map.get(nums[i]);
            map.put(nums[i], pre + 1);
        }
        int answer = Math.min(nums.length / 2, map.size());

        return answer;
    }
}