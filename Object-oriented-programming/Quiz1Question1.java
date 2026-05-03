// count the number of hundreds in a positive integer
import java.util.Scanner;
public class Quiz1Question1 {
    public static void main (String[] args) {
        System.out.println("Program for counting the number of hundreds.");
        int number, hundreds;                                   // Declare two integer variables, number and hundreds.
        Scanner sc = new Scanner(System.in);
        System.out.print("Please input a positive number: "); // Prompt the user to input a positive number.
        while(!sc.hasNextInt()){                                // Check if the next input is not an integer.
            System.out.println("Please input only integer.");
            sc.nextLine();
            System.out.print("Please input again: ");       
        }
        number = sc.nextInt(); // input
        hundreds = number / 100;

        System.out.printf("There are %d hundred in number %d.\n", hundreds, number); // format hundred first then number
        sc.close();
    }
}