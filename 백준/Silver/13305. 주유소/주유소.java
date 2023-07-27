import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] road = new int[N];
        int[] oil = new int[N];
        for (int i = 0; i < N - 1; i++) {
            road[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            oil[i] = Integer.parseInt(st.nextToken());
        }
        int cost = oil[0];
        int total = oil[0] * road[0];
        for (int i = 1; i < N; i++) {
            cost = Math.min(cost, oil[i]);
            total += cost * road[i];
        }
        System.out.println(total);

        br.close();
    }
}