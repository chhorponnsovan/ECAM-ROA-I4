package QuizQuestion;
import java.util.Scanner;
public class Quiz3Question10 {
 public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("How many numbers do you want to enter? ");
        int count = scanner.nextInt(); //nextInt()
        if (count <= 0) {
            System.out.println("Please enter a positive number of elements.");
            scanner.close();
            return; //return
        }
        double[] numbers = new double[count]; // count
        System.out.println("Enter the numbers:");
        for (int i = 0; i < count; i++) { //count
            System.out.print("Number " + (i + 1) + ": ");
            numbers[i] = scanner.nextDouble(); // nextDouble()
        }
        double sum = 0;
        for (double number : numbers) { // numbers
            sum += number;
        }
        double average = sum / numbers.length; // numbers
        System.out.printf("Average: %.2f\n", average);
       
        scanner.close();
    }
}
