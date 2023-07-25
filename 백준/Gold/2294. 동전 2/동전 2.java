import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] coin = new int[n];
        int[] memo = new int[k + 1];

        for (int i = 0; i < n; i++) {
            int c = Integer.parseInt(br.readLine());
            coin[i] = c;
            if (c > k) continue;
            memo[c] = 1;
        }

        int cnt = 1;
        while (memo[k] == 0 && cnt < k) {
            for (int i = k; i >= 0; i--) {
                if (memo[i] == cnt) {
                    for (int c:coin) {
                        if (i + c <= k) memo[i + c] = cnt + 1;
                    }
                }
            }
            cnt += 1;
        }

        if (memo[k] == 0) System.out.println(-1);
        else System.out.println(memo[k]);
        br.close();

    }
}