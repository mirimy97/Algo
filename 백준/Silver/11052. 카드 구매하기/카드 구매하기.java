import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] cost = new int[N];
        for (int i = 0; i < N; i++) {
            cost[i] = Integer.parseInt(st.nextToken());

            if (i != 0) {
                for (int j = 0; j <= (i-1) / 2; j++) {
                    cost[i] = Math.max(cost[i], cost[j] + cost[i-1-j]);
                }
            }
        }
        System.out.println(cost[N-1]);

        br.close();
    }
}