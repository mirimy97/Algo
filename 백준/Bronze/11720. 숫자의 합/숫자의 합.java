import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String sNum = br.readLine();
        char[] cNums = sNum.toCharArray();
        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += cNums[i] - '0'; // 문자열 -> 숫자 변환 시 아스키코드 기준 48을 빼면 된다.
        }

        System.out.println(sum);
    }
}