package QuizQuestion;

//sum all even from 1 to given
import java.util.Scanner;
public class Quiz3Question16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();

        int sum = 0;
        
        for (int i = 2; i <= n; i += 2) {
            sum += i; // sum += i;
        }
        System.out.println("Sum of even numbers from 1 to " + n + " is: " + sum);
        scanner.close();
    }
}
