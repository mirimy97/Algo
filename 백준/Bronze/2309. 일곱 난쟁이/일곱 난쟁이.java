import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] hList = new int[9];
        int total = 0;
        for (int i = 0; i < 9; i++) {
            hList[i] = Integer.parseInt(br.readLine());
            total += hList[i];
        }
        total -= 100;
        boolean find = false;
        Arrays.sort(hList);
        int xi = 0;
        int xj = 0;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j ++) {
                if (hList[i] + hList[j] == total) {
                    find = true;
                    xi = i;
                    xj = j;
                    break;
                }
            }
            if (find) break;
        }

        for (int i = 0; i < 9; i ++) {
            if (i != xi && i != xj) {
                System.out.println(hList[i]);
            }
        }


        br.close();

    }
}