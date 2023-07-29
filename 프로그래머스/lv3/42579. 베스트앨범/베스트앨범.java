import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Comparator;

class Solution {
    public ArrayList<Integer> solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        HashMap<String, ArrayList<Integer>> map = new HashMap<String, ArrayList<Integer>>();
        HashMap<String, Integer> hap = new HashMap<String, Integer>();
        
        for (int i = 0; i < genres.length; i++) {
            ArrayList<Integer> value = map.get(genres[i]);
            if (value == null) value = new ArrayList<Integer>();
            value.add(i);
            map.put(genres[i], value);
            
            Integer s = hap.get(genres[i]);
            if (s == null) s = 0;
            s += plays[i];
            hap.put(genres[i], s);
        }
        int max1 = 0;
        int max2 = 0;
        List<Map.Entry<String, Integer>> entryList = new ArrayList<>(hap.entrySet());
        entryList.sort((e1, e2) -> -e1.getValue().compareTo(e2.getValue()));
        System.out.println(entryList);
        int k = 0;
        int v = 0;

        int idx1, idx2;
        max1 = 0;
        max2 = 0;
        // gen1
        for (Map.Entry<String, Integer> entry : entryList) {
            
            ArrayList<Integer> indexList = map.get(entry.getKey());
            System.out.println(indexList);
            idx1 = -1;
            idx2 = -1;  
            max1 = -1;
            max2 = -1;
            for (int i = 0; i < indexList.size(); i++) {
                if (plays[indexList.get(i)] > max1) {
                    max2 = max1;
                    idx2 = idx1;
                    max1 = plays[indexList.get(i)];
                    idx1 = indexList.get(i);
                } else if (plays[indexList.get(i)] > max2) {
                    max2 = plays[indexList.get(i)];
                    idx2 = indexList.get(i);
                }
            }
            if (idx1 != -1) answer.add(idx1);
            if (idx2 != -1) answer.add(idx2);
        }        
        
      
        
        System.out.println(map);
        System.out.println(hap);
        return answer;
    }
}