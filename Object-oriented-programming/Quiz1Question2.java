// This program prompts the user to input a positive integer, increments it by 1, and then displays the result as a message about being luckier. It also includes error handling for non-integer inputs.
import java.util.Scanner;
public class Quiz1Question2 {   
    public static void main(String[] args) {
        System.out.println("‑‑‑‑‑‑‑ Program for guessing your luckiness ‑‑‑‑‑‑‑"); // Program for guessing your luckiness
        Scanner sc = new Scanner(System.in);
        int guess;                                                            // Declare an integer variable, guess.
        System.out.print("Please input a positive number: ");
        if(!sc.hasNextInt()){
            System.out.println("Please input only integer.");
            sc.nextLine();
            System.out.print("Please input again: ");                       // Prompt the user to input again if the input is not an integer.
        }
        guess = sc.nextInt();
        guess++;                                                               // Increment the value of guess by 1.

        System.out.printf("I got %d. I am luckier.\n", guess);          // %d 
        sc.close();                                                             // Close the scanner to prevent resource leak.
    }
}