import java.util.Arrays;
class Solution {
    public int hp, len, maxDG;
    public int[][] dg;
    public int[] v;
    public int solution(int k, int[][] dungeons) {
        hp = k;
        len = dungeons.length;
        dg = dungeons;
        maxDG = 0;
        v = new int[len];
        perm(0);
        return maxDG;
    }
    
    public void perm(int cnt) {
        int s = 0;
        for (int a : v) s += a;
        // System.out.println(s);
        maxDG = Math.max(maxDG, s); 
        if (cnt == len) {
            return;
        } else {
            for (int i = 0; i < len; i++) {
                if (hp < dg[i][0]) continue;
                if (v[i] == 1) continue;
                v[i] = 1;
                hp -= dg[i][1];
                perm(cnt + 1);
                hp += dg[i][1];
                v[i] = 0;
            }
        }
    }
}