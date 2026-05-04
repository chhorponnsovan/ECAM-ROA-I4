package QuizQuestion;
// calculate exchange rate
import java.util.Scanner;
public class Quiz3Question6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter amount in original currency: ");
        double originalAmount = scanner.nextDouble();

        System.out.print("The equivalent amount in the target currency is: ");
        double targetAmount = scanner.nextDouble();

        double exchangeRate = targetAmount / originalAmount; // targetAmount / originalAmount
        System.out.printf("The exchange rate is %.2f.\n", exchangeRate);
        scanner.close();
    }
}
