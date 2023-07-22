import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int J; // 사탕 개수
        int N; // 상자 개수
        int R; // 가로
        int C; // 세로
        
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {

            st = new StringTokenizer(br.readLine());
            J = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            int[] boxes = new int[N];

            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                R = Integer.parseInt(st.nextToken());
                C = Integer.parseInt(st.nextToken());

                boxes[j] = R * C;
            }

            Arrays.sort(boxes);

            int cnt = 0;
            for (int j = N-1; j >= 0; j--) {
                J -= boxes[j];
                cnt += 1;
                if (J <= 0) break;
            }

            System.out.println(cnt);
        }

        br.close();

    }

}