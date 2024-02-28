import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int sum=0, val, maxVal=0;
        for (int i = 0; i < N; i++) {
            val = Integer.parseInt(st.nextToken());
            sum += val;
            maxVal = Math.max(val, maxVal);
        }
        float avg = (float) sum / N;
        System.out.println(avg / maxVal * 100);
    }
}