import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        
        for (int i = 0; i < clothes.length; i++) {
            // String n = clothes[i][0];  // 이름
            String c = clothes[i][1];  // 카테고리
            
            int value = map.get(c) == null ? 1 : map.get(c) + 1;
            map.put(c, value);
        }
        
        for (int v : map.values()) answer *= v + 1;
        answer -= 1;
        
        return answer;
    }
}