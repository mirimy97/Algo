import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] cost = new int[n];
        int[] old = new int[k + 1];
        int[] next = new int[k + 1];

        for (int i = 0; i < n; i++) {
            old[0] = 1;
            int c = Integer.parseInt(br.readLine());
            for (int j = 1; j <= (k / c); j++) { // 몇개 들어갈건지?
                int num = c * j;
                while (num < k + 1) {
                    next[num] += old[num - (c * j)];
                    num++;
                }
            }
            old = next.clone();

        }

        System.out.println(old[k]);

        br.close();
    }
}