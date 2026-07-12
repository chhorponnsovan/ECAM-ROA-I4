package QuizQuestion;
/** If we input 5289, the proram below will produce result as following:
 *
------- Program for converting from seconds into hours:minutes:seconds -------
Input number of seconds: 5289
Time corresponding to 5289seconds is 01:28:09.
 */
import java.util.Scanner;
public class Quiz2Question7 {
        public static void main(String[] args) {
        System.out.println("------- Program for converting from seconds into hours:minutes:seconds ------- ");
        Scanner sc = new Scanner(System.in);
        int totalSeconds, hours, minutes, seconds; // Declare four integer variables, totalSeconds, hours, minutes, and seconds.
        System.out.print("Please input hours: ");
        hours = sc.nextInt(); // Prompt the user to input hours and read the input using the Scanner object, storing it in the variable hours.
        System.out.print("Please input minutes: ");
        minutes = sc.nextInt();
        System.out.print("Please input seconds: "); // Prompt the user to input seconds and read the input using the Scanner object, storing it in the variable seconds.
        seconds = sc.nextInt();
       
        totalSeconds = (hours * 3600) + (minutes * 60) + seconds; // Calculate the total number of seconds by multiplying hours by 3600, minutes by 60, and adding all three components together.

        System.out.printf("Number of seconds = %dx3600 + %dx60 + %d = %d\n", hours, minutes, seconds, totalSeconds);
        // Format the output to display the calculation of total seconds, showing the contribution of hours, minutes, and seconds in the format "Number of seconds = Hx3600 + Mx60 + S = TotalSeconds", where H, M, S, and TotalSeconds are replaced with their respective values.
        sc.close();
    }
}
