import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[][] games = new int[N][3];
        StringTokenizer st;
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<3; j++) {
                games[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int cnt = 0;
        for (int a = 1; a < 10; a++) {
            for (int b = 1; b < 10; b++) {
                for (int c = 1; c < 10; c++) {
                    if (a != b & b != c & c != a) {

                        boolean isPossible = true;
                        for (int i = 0; i < N; i++) {
                            int strike = 0;
                            int ball = 0;
                            if (games[i][0] / 100 == a || games[i][0] / 100 == b || games[i][0] / 100 == c) {
                                if (games[i][0] / 100 == a) {
                                    strike += 1;
                                } else {
                                    ball += 1;
                                }
                            }
                            if ((games[i][0] / 10) % 10 == a || (games[i][0] / 10) % 10 == b || (games[i][0] / 10) % 10 == c) {
                                if ((games[i][0] / 10) % 10  == b) {
                                    strike += 1;
                                } else {
                                    ball += 1;
                                }
                            }
                            if (games[i][0] % 10 == a || games[i][0] % 10 == b || games[i][0] % 10 == c) {
                                if (games[i][0] % 10 == c) {
                                    strike += 1;
                                } else {
                                    ball += 1;
                                }
                            }
                            if (strike != games[i][1] | ball != games[i][2]) {
                                isPossible = false;
                                break;
                            }

                        }
                        if (isPossible == true) {
                            cnt += 1;
                        }
                    }
                }
            }
        }
        System.out.println(cnt);

        br.close();

    }
}