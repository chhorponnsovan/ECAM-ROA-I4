package QuizQuestion;
// use switch case 1 is celcius to fahrenheit, 2 is fahrenheit to celsius.
import java.util.Scanner;
public class Quiz3Question12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose conversion type:");
        System.out.println("1: Celsius to Fahrenheit");
        System.out.println("2: Fahrenheit to Celsius");
        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                System.out.print("Enter temperature in Celsius: ");
                double celsius = scanner.nextDouble();
                double fahrenheit = (celsius * 9 / 5) + 32;
                System.out.printf("%.2f Celsius is %.2f Fahrenheit\n", celsius, fahrenheit);
                break;
            case 2:
                System.out.print("Enter temperature in Fahrenheit: ");
                fahrenheit = scanner.nextDouble();
                celsius = (fahrenheit - 32) * 5 / 9; // (fahrenheit - 32) * 5.0/9.0
                System.out.printf("%.2f Fahrenheit is %.2f Celsius\n", fahrenheit, celsius);
                break;
            default:
                System.out.println("Invalid choice. Please select 1 or 2.");
        }
        scanner.close();
    }
}
