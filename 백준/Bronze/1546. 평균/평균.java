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
        
        // sum은 int, 계산하려는 결과는 float 일 때, 계산과정에 소수점을 임의로 넣어서 float로 형변환 할 수 있다.
        System.out.println(sum * 100.0 / N / maxVal);
    }
}