// display all numbers from 120 to 150
public class Quiz2Question1 {
        public static void main(String[] args) {
        int k = 120;
        System.out.print(k);
        for (int i = 1; k+i < 151; i++) {
            int h= k+i;
            System.out.print("," + h);
        }
    }
}