# Object Oriented Programming

This file contains reviews for the Object Oriented Programming course.

The Java quiz review section below is generated automatically from the `.java` files in this folder. When you add new quiz files, run `python generate_review.py` and the review content will refresh.

<!-- BEGIN JAVA QUIZ REVIEW -->
## Java Quiz Review

Generated automatically from the `.java` files in this folder.
To regenerate this section, run `python generate_review.py`.

### Quiz 1 - Question 1

```java
// count the number of hundreds in a positive integer
import java.util.Scanner;
public class Quiz1Question1 {
    public static void main (String[] args) {
        System.out.println("Program for counting the number of hundreds.");
        int number, hundreds;                                   **// Declare two integer variables, number and hundreds.**
        Scanner sc = new Scanner(System.in);
        System.out.print("Please input a positive number: "); **// Prompt the user to input a positive number.**
        while(!sc.hasNextInt()){                                **// Check if the next input is not an integer.**
            System.out.println("Please input only integer.");
            sc.nextLine();
            System.out.print("Please input again: ");       
        }
        number = sc.nextInt(); **// input**
        hundreds = number / 100;

        System.out.printf("There are %d hundred in number %d.\n", hundreds, number); **// format hundred first then number**
        sc.close();
    }
}
```

### Quiz 1 - Question 2

```java
import java.util.Scanner;

public class Quiz1Question2 {   
    public static void main(String[] args) {
        System.out.println("‑‑‑‑‑‑‑ Program for guessing your luckiness ‑‑‑‑‑‑‑"); **// Program for guessing your luckiness**
        Scanner sc = new Scanner(System.in);
        int guess;                                                            **// Declare an integer variable, guess.**
        System.out.print("Please input a positive number: ");
        if(!sc.hasNextInt()){
            System.out.println("Please input only integer.");
            sc.nextLine();
            System.out.print("Please input again: ");                       **// Prompt the user to input again if the input is not an integer.**
        }
        guess = sc.nextInt();
        guess++;                                                               **// Increment the value of guess by 1.**

        System.out.printf("I got %d. I am luckier.\n", guess);          **// %d **
        sc.close();                                                             **// Close the scanner to prevent resource leak.**
    }
}
```

### Quiz 1 - Question 3

```java
import java.util.Scanner;
public class Quiz1Question3 {
    public static void main(String[] args) {
        System.out.println("------- Program for converting from seconds into hours:minutes:seconds ------- ");
        Scanner sc = new Scanner(System.in);
        int totalSeconds, hours, minutes, seconds; **// Declare four integer variables, totalSeconds, hours, minutes, and seconds.**
        System.out.print("[Input number of seconds: ]");
        if(!sc.hasNextInt()){
            System.out.println("Please input only integer.");
            sc.nextLine();
            System.out.print("Please input seconds again: ");
        }
        totalSeconds = sc.nextInt();
        minutes = totalSeconds / 60; **// Calculate the number of minutes by dividing totalSeconds by 60.**
        hours = minutes / 60;  **// Calculate the number of hours by dividing minutes by 60.**
        minutes -= hours * 60;  **// Update minutes by subtracting the number of hours (converted to minutes) from the total minutes.**
        seconds = totalSeconds % 60;

        System.out.printf("Time corresponding to %dseconds is %02d:%02d:%02d.\n", totalSeconds, hours, minutes, seconds); **// Format the output to display hours, minutes, and seconds in the format HH:MM:SS, ensuring that each component is displayed with two digits (using %02d).**
        sc.close();
    }
}
```

<!-- END JAVA QUIZ REVIEW -->

