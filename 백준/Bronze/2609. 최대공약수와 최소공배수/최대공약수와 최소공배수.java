import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Math.min;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

//        최대공약수
        int gcd = 0;
        for (int i = min(a, b); i > 0; i--) {
            if (a % i == 0 && b % i == 0) {
                gcd = i;
                break;
            }
        }

//        최소공약수
        int lcm = (a / gcd) * (b / gcd) * gcd;

        System.out.println(gcd);
        System.out.println(lcm);
        br.close();

    }
}