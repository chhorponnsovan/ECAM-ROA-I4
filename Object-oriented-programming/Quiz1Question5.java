/** If we input 50, the program below will produce result as following:
------- Program for calculating duration of travel from ITC to Airport -------
Given that distance from ITC to Airport is 30km and travel speed is average 30km/h.
Please input traffic jam factor (in percentage [0-100]): 50

Travelling Duration = 02:00:00
 */
import java.util.Scanner;
public class Quiz1Question5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int percentage, hours, minutes, seconds, totalSeconds;
        System.out.println("------- Program for calculating duration of travel from ITC to Airport -------");
        System.out.println("Given that distance from ITC to Airport is 30km and travel speed is average 30km/h.");
        System.out.print("Please input traffic jam factor (in percentage [0-100]): ");
        do{
            while(!sc.hasNextInt()){ // Check if the input is an integer using the hasNextInt() method of the Scanner class. If the input is not an integer, it will enter the while loop.
                System.out.println("\nInput integer only.");
                sc.nextLine();
                System.out.print("Please input traffic jam factor again (in percentage [0-100]): ");
            }
            percentage = sc.nextInt();
            if(percentage < 0 || percentage > 100){ // After confirming that the input is an integer, it checks if the input is within the valid range of 0 to 100. If the input is outside this range, it will prompt the user to input again until a valid percentage is entered.
                System.out.println("Input integer only between 0 to 100 inclusively.");
                System.out.print("Please input traffic jam factor again (in percentage [0-100]): ");
            }
        }while(percentage < 0 || percentage > 100); // The do-while loop continues to execute until the user inputs a valid percentage between 0 and 100, ensuring that the program receives appropriate input for the traffic jam factor.
        //distance from ITC to Airport is 30Km = 30000m
        //speed 30km/h
        totalSeconds = (int)Math.ceil(30000.0f  / (30 / 3.6f - (30 / 3.6f * percentage / 100))); 
        // Calculate the total travel time in seconds by dividing the distance (30000 meters) by the effective speed, which is the average speed (30 km/h converted to m/s) reduced by the traffic jam factor. The result is rounded up using Math.ceil() to ensure that any fractional seconds are accounted for, and then cast to an integer.
        minutes = totalSeconds / 60; // Convert the total seconds into minutes by dividing by 60.
        hours = minutes / 60; // Convert the total minutes into hours by dividing by 60.
        minutes -= hours * 60;
        seconds = totalSeconds % 60; // Calculate the remaining seconds after accounting for the hours and minutes by using the modulus operator to find the remainder when totalSeconds is divided by 60.
        System.out.printf("Travelling Duration = %02d:%02d:%02d \n",hours,minutes,seconds); //
        // Format the output to display the travel duration in the format "Travelling Duration = HH:MM:SS", where HH, MM, and SS are replaced with the calculated hours, minutes, and seconds, respectively. The %02d format specifier ensures that each component is displayed with at least two digits, padding with zeros if necessary.
        sc.close();
    }
}