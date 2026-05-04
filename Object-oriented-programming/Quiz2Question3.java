/** If we input 50, the program below will produce result as following:
 *
------- Program for calculating duration of travel from ITC to Airport -------
Given that distance from ITC to Airport is 30km and travel speed is average 30km/h.
Please input traffic jam factor (in percentage [0-100]): 50

Travelling Duration = 02:00:00

 */
import java.util.Scanner;
public class Quiz2Question3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int percentage, hours, minutes, seconds, totalSeconds;
        System.out.println("------- Program for calculating duration of travel from ITC to Airport -------");
        System.out.println("Given that distance from ITC to Airport is 30km and travel speed is average 30km/h.");
        System.out.print("Please input traffic jam factor (in percentage [0-100]): ");
        do{
            while(!sc.hasNextInt()){ //check if input is integer
                System.out.println("\nInput integer only.");
                sc.nextLine();
                System.out.print("Please input traffic jam factor again (in percentage [0-100]): ");
            }
            percentage = sc.nextInt();
            if(percentage < 0 || percentage>100){ //check if input is between 0 to 100
                System.out.println("Input integer only between 0 to 100 inclusively.");
                System.out.print("Please input traffic jam factor again (in percentage [0-100]): ");
            }
        }while(percentage < 0 || percentage>100); //keep looping until input is valid
        //distance from ITC to Airport is 30Km = 30000m
        //speed 30km/h
        totalSeconds = (int)Math.ceil((30000.0f ) / ((30 / 3.6f) - ((30 / 3.6f) * (percentage) / 100))); //convert speed from km/h to m/s and calculate total seconds needed to travel
        minutes = (totalSeconds / 60); //convert total seconds to minutes
        hours = (minutes / 60); //convert minutes to hours
        minutes -= hours * 60;
        seconds = (totalSeconds % 60); // get remaining seconds after converting to minutes
        System.out.printf("Travelling Duration = %02d:%02d:%02d",hours,minutes,seconds); //print result in format of HH:MM:SS
        sc.close();
    }
}
