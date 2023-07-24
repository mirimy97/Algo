import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import static java.lang.Math.max;
import static java.lang.Math.min;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int [] scores = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            scores[i] = Integer.parseInt(st.nextToken());
        }

        int [] memo = new int[N];
        memo[0] = 0;
        int max_num, min_num;
        for (int i = 1; i < N; i++) {
            for (int j = i; j >= 0; j--) {
                min_num = scores[j];
                max_num = scores[j];
                for (int k = j; k <= i; k++) {
                    min_num = min(min_num, scores[k]);
                    max_num = max(max_num, scores[k]);
                }
                if (j == 0) memo[i] = max(memo[i], max_num - min_num);
                else memo[i] = max(memo[i], memo[j - 1] + max_num - min_num);
            }
            
        }
        System.out.println(memo[N - 1]);
        br.close();

    }

}