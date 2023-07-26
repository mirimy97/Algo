import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];
        int[] cnts = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            cnts[i] = 1;
        }

        int i = 1;
        int max_cnt = 1;
        while (i < N) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) cnts[i] = Math.max(cnts[i], cnts[j] + 1);
            }
            if (max_cnt < cnts[i]) max_cnt = cnts[i];
            i++;
        }
        System.out.println(max_cnt);
        br.close();
    }
}