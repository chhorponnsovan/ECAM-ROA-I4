/*Display even numbers (ex: 2, 4, 6, 8, etc.)
located between A and 500.
Where A is given by user (0<A<500).
 */
import java.util.Scanner;
public class Quiz2Question4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); //create Scanner object to read user input
        int A; // declare variable A to store user input
        do{ //loop until user input is valid
            System.out.print("Input A: "); //prompt user to input A
            A = sc.nextInt();
        }while(A<0 && A>500); //check if input is between 0 and 500
        A = A + A % 2; // if A is odd, add 1 to make it even. If A is even, it remains unchanged.
        while(A <= 500){ //loop until A is greater than 500
            System.out.printf("%d ",A); //print A followed by a space
            A += 2;
        }
        sc.close();
    }
}
