import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static int [] memo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        memo = new int[1000002];
        memo[0] = 0;
        memo[1] = 1;
        memo[2] = 1;

        fibo(N + 1);

        System.out.println(memo[N + 1] % 1000000007);

        br.close();

    }

    public static int fibo(int N) {
        if (memo[N] != 0) return memo[N];

        memo[N] = fibo(N - 1) + fibo(N - 2);
        return memo[N];
    }

}