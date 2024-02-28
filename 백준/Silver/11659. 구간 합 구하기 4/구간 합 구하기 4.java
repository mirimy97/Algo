import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] sum = new int[N + 1];

        int cur = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < (N + 1); i++) {
            cur += Integer.parseInt(st.nextToken());
            sum[i] = cur;
        }

        int s, e;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            bw.write(String.valueOf(sum[e] - sum[s-1])+"\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}