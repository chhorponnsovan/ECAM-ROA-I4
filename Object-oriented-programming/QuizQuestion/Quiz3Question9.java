package QuizQuestion;
import java.util.Scanner;
public class Quiz3Question9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int num1 = scanner.nextInt();

        System.out.print("Enter second number: ");
        int num2 = scanner.nextInt();

        int a = Math.abs(num1);
        int b = Math.abs(num2);
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        int gcd = a;
        int lcm = Math.abs(num1 * num2) / gcd; // Math.abs(num1 * num2)
        System.out.println("The LCM of " + num1 + " and " + num2 + " is: " + lcm);
        scanner.close();
    }
    
}
