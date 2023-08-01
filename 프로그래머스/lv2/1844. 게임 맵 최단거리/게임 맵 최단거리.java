import java.util.Arrays;
import java.util.Deque;
import java.util.ArrayDeque;
class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int[][] v = new int[n][m];
        Deque<Point> q = new ArrayDeque<Point>();
        q.add(new Point(0, 0));
        int[][] delta = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        // System.out.println(Arrays.toString(v));
        // System.out.println(q);
        
        int ni, nj;
        while (!q.isEmpty()) {
            if (v[n-1][m-1] != 0) break;
            Point s = q.pollFirst();
            for (int[] d : delta) {
                ni = s.i + d[0];
                nj = s.j + d[1];
                if (ni>=0 && nj>=0 && ni<n && nj<m && maps[ni][nj]>0 && v[ni][nj]==0) {
                    q.add(new Point(ni, nj));
                    v[ni][nj] = v[s.i][s.j] + 1;
                }
            }
        }
        int answer;
        if (v[n-1][m-1] == 0) answer = -1;
        else  answer = v[n-1][m-1] + 1;
        return answer;
    }
}

class Point {
    int i;
    int j;
    
    public Point (int i, int j) {
        this.i = i;
        this.j = j;
    }
}