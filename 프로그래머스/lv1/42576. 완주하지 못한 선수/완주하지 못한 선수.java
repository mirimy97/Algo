import java.util.HashMap;
class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for (String name : completion) {
            int value = map.get(name) == null ? 1 : map.get(name) + 1;
            map.put(name, value);
        }
        String answer = "";
        for (String name : participant) {
            if (!map.containsKey(name) || map.get(name) == 0) {
                answer = name;
            } else {
                map.replace(name, map.get(name) - 1);
            }
        }

        return answer;
    }
}