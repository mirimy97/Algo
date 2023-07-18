import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static int L, C;
    public static String [] apb;
    public static String [] result;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        // C 개 중 L 개 뽑기
        st = new StringTokenizer(br.readLine());
        apb = new String[C];

        for (int i=0; i<C; i++) {
            apb[i] = st.nextToken();
        }
        Arrays.sort(apb);

        result = new String[L];
        comb(0, 0);

        br.close();

    }

    public static void comb(int cnt, int start) {
        if(cnt==L) {
            int mo = 0;
            int ja = 0;
            for (int i = 0; i < L; i++) {
                if (result[i].equals("a") || result[i].equals("e") ||result[i].equals("i") ||result[i].equals("o") ||result[i].equals("u")) {
                    mo += 1;
                } else {
                    ja += 1;
                }
            }
            if (mo > 0 && ja > 1) {
                System.out.println(String.join("", result));
            }
            return;
        }
        for(int i=start; i<C; i++) {
            result[cnt] = apb[i];
            comb(cnt+1,i+1);

        }
    }
}