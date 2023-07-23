import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static boolean [] chosen;
    public static int [] p;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        chosen = new boolean[N];
        Arrays.fill(chosen, false);
        p = new int[N];
        perm(N, 0);

        br.close();

    }

    public static void perm(int N, int cnt) {
        if (cnt == N) {
            //  p 출력
            for (int j = 0; j < N; j++) {
                System.out.print(p[j]+" ");
            }
            System.out.println();
            return;
        }
        for (int i = 0; i < N; i++) {
            if (chosen[i] == true) continue;
            chosen[i] = true;
            p[cnt] = i + 1;
            perm(N, cnt + 1);
            chosen[i] = false;
        }
    }


}