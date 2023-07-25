import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 수열 크기 N

        StringTokenizer st = new StringTokenizer(br.readLine());
        int [] nums = new int[N];    // 홍준이가 적은 수 nums
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());    // 질문 개수 M
        int[][] memo = new int[N][N];
        for (int i = 0; i < N; i++) {
            memo[i][i] = 1;
            if (i > 0 && nums[i - 1] == nums[i]) memo[i][i - 1] = 1;
        }


        int S, E;
        int record = 1;
        for (int t = 0; t < M; t++) {
            st = new StringTokenizer(br.readLine());
            S = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());

            // E까지 끝자리 순회하면서 memo 배열 채워넣기
            for (int i = record; i < E; i++) {
                // 내 전번째 (i-1) 자리에 저장돼있는 펠린드롬 시작 index들 순회
                for (int j = 0; j < N; j++) {
                    if (j > 0 && memo[i-1][j] == 1 && nums[j - 1] == nums[i]) {
                        memo[i][j - 1] = 1;
                    }
                }
            }
            if (record < E - 1) record = E - 1;

            if (memo[E - 1][S - 1] == 1) bw.write(1 + "\n");
            else bw.write(0 + "\n");
        }

        br.close();
        bw.close();

    }

}