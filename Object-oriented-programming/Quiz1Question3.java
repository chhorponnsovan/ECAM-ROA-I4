import java.util.Scanner;
public class Quiz1Question3 {
    public static void main(String[] args) {
        System.out.println("------- Program for converting from seconds into hours:minutes:seconds ------- ");
        Scanner sc = new Scanner(System.in);
        int totalSeconds, hours, minutes, seconds; // Declare four integer variables, totalSeconds, hours, minutes, and seconds.
        System.out.print("[Input number of seconds: ]");
        if(!sc.hasNextInt()){
            System.out.println("Please input only integer.");
            sc.nextLine();
            System.out.print("Please input seconds again: ");
        }
        totalSeconds = sc.nextInt();
        minutes = totalSeconds / 60; // Calculate the number of minutes by dividing totalSeconds by 60.
        hours = minutes / 60;  // Calculate the number of hours by dividing minutes by 60.
        minutes -= hours * 60;  // Update minutes by subtracting the number of hours (converted to minutes) from the total minutes.
        seconds = totalSeconds % 60;

        System.out.printf("Time corresponding to %dseconds is %02d:%02d:%02d.\n", totalSeconds, hours, minutes, seconds); // Format the output to display hours, minutes, and seconds in the format HH:MM:SS, ensuring that each component is displayed with two digits (using %02d).
        sc.close();
    }
}