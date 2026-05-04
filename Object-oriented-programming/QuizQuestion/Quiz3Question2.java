package QuizQuestion;
// speed operation given distance and time
import java.util.Scanner;

public class Quiz3Question2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the distance (in kilometers): ");
        double distance = scanner.nextDouble();
        System.out.print("Enter the time (in hours): ");
        double time = scanner.nextDouble();

        if (time == 0) { // time == 0
            System.out.println("Time must be greater than zero.");
        } else {
            double speed = distance / time;
            System.out.printf("The speed is: %.2f km/h\n", speed);
        }
        scanner.close();
    }
}
