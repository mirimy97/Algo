import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());
        int p = 0;
        long s = 0L;
        for (p = 0; p < N; p++) {
            s += p;
            if (s > N) break;
        }
        if (N == 1) p = 2;
        System.out.println(p-1);

        br.close();
    }
}