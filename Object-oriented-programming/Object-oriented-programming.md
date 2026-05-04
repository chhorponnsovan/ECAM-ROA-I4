# Object Oriented Programming

This file contains reviews for the Object Oriented Programming course.

The Java quiz review section below is generated automatically from the `.java` files in this folder. When you add new quiz files, run `python generate_review.py` and the review content will refresh.

<!-- BEGIN JAVA QUIZ REVIEW -->
## Java Quiz Review

Generated automatically from the `.java` files in the `QuizQuestion` folder.
To regenerate this section, run `python generate_review.py`.

### Quiz 1 - Question 1

```java
package QuizQuestion;
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
package QuizQuestion;
// This program prompts the user to input a positive integer, increments it by 1, and then displays the result as a message about being luckier. It also includes error handling for non-integer inputs.
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
package QuizQuestion;
// This program converts a given time in hours, minutes, and seconds into total seconds. It prompts the user to input hours, minutes, and seconds, calculates the total seconds using the formula (hours * 3600) + (minutes * 60) + seconds, and then displays the result in a formatted manner.
import java.util.Scanner;
public class Quiz1Question3 {
    public static void main(String[] args) {
        System.out.println("------- Program for converting from seconds into hours:minutes:seconds ------- ");
        Scanner sc = new Scanner(System.in);
        int totalSeconds, hours, minutes, seconds; **// Declare four integer variables, totalSeconds, hours, minutes, and seconds.**
        System.out.print("Input number of seconds: "); **// Prompt the user to input the number of seconds.**
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

### Quiz 1 - Question 4

```java
package QuizQuestion;
// This program converts a given time in hours, minutes, and seconds into total seconds. It prompts the user to input hours, minutes, and seconds, calculates the total seconds using the formula (hours * 3600) + (minutes * 60) + seconds, and then displays the result in a formatted manner.
import java.util.Scanner;
public class Quiz1Question4 {
    public static void main(String[] args) {
        System.out.println("------- Program for converting from seconds into hours:minutes:seconds ------- ");
        Scanner sc = new Scanner(System.in);
        int totalSeconds, hours, minutes, seconds; **// Declare four integer variables, totalSeconds, hours, minutes, and seconds.**
        System.out.print("Please input hours: ");
        hours = sc.nextInt(); **// Prompt the user to input hours and read the input using the Scanner object, storing it in the variable hours.**
        System.out.print("Please input minutes: ");
        minutes = sc.nextInt();
        System.out.print("Please input seconds: ");
        seconds = sc.nextInt();
       
        totalSeconds = (hours * 3600) + (minutes * 60) + seconds; **// Calculate the total number of seconds by multiplying hours by 3600, minutes by 60, and adding all three components together.**

        System.out.printf("Number of seconds = %dx3600 + %dx60 + %d = %d seconds\n", hours, minutes, seconds, totalSeconds); 
        // Format the output to display the calculation of total seconds, showing the contribution of hours, minutes, and seconds in the format "Number of seconds = Hx3600 + Mx60 + S = TotalSeconds", where H, M, S, and TotalSeconds are replaced with their respective values.
        sc.close();
    }
}
```

### Quiz 1 - Question 5

```java
package QuizQuestion;
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
            while(!sc.hasNextInt()){ **// Check if the input is an integer using the hasNextInt() method of the Scanner class. If the input is not an integer, it will enter the while loop.**
                System.out.println("\nInput integer only.");
                sc.nextLine();
                System.out.print("Please input traffic jam factor again (in percentage [0-100]): ");
            }
            percentage = sc.nextInt();
            if(percentage < 0 || percentage > 100){ **// After confirming that the input is an integer, it checks if the input is within the valid range of 0 to 100. If the input is outside this range, it will prompt the user to input again until a valid percentage is entered.**
                System.out.println("Input integer only between 0 to 100 inclusively.");
                System.out.print("Please input traffic jam factor again (in percentage [0-100]): ");
            }
        }while(percentage < 0 || percentage > 100); **// The do-while loop continues to execute until the user inputs a valid percentage between 0 and 100, ensuring that the program receives appropriate input for the traffic jam factor.**
        //distance from ITC to Airport is 30Km = 30000m
        //speed 30km/h
        totalSeconds = (int)Math.ceil(30000.0f  / (30 / 3.6f - (30 / 3.6f * percentage / 100))); 
        // Calculate the total travel time in seconds by dividing the distance (30000 meters) by the effective speed, which is the average speed (30 km/h converted to m/s) reduced by the traffic jam factor. The result is rounded up using Math.ceil() to ensure that any fractional seconds are accounted for, and then cast to an integer.
        minutes = totalSeconds / 60; **// Convert the total seconds into minutes by dividing by 60.**
        hours = minutes / 60; **// Convert the total minutes into hours by dividing by 60.**
        minutes -= hours * 60;
        seconds = totalSeconds % 60; **// Calculate the remaining seconds after accounting for the hours and minutes by using the modulus operator to find the remainder when totalSeconds is divided by 60.**
        System.out.printf("Travelling Duration = %02d:%02d:%02d \n",hours,minutes,seconds); **//**
        // Format the output to display the travel duration in the format "Travelling Duration = HH:MM:SS", where HH, MM, and SS are replaced with the calculated hours, minutes, and seconds, respectively. The %02d format specifier ensures that each component is displayed with at least two digits, padding with zeros if necessary.
        sc.close();
    }
}
```

### Quiz 2 - Question 1

```java
package QuizQuestion;
// display all numbers from 120 to 150
public class Quiz2Question1 {
        public static void main(String[] args) {
        int k = 120;
        System.out.print(k);
        for (int i = 1; k+i < 151; i++) {
            int h= k+i;
            System.out.print("," + h);
        }
    }
}
```

### Quiz 2 - Question 2

```java
package QuizQuestion;
// display all odd numbers from 1 to 500
public class Quiz2Question2 {
        public static void main(String[] args) {
        int runner = 1;
        int n = 500;
        while(runner < n){
                System.out.printf("%d ", runner);
            runner += 2;         
        }
    }
}
```

### Quiz 2 - Question 3

```java
package QuizQuestion;
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
            while(!sc.hasNextInt()){ **//check if input is integer**
                System.out.println("\nInput integer only.");
                sc.nextLine();
                System.out.print("Please input traffic jam factor again (in percentage [0-100]): ");
            }
            percentage = sc.nextInt();
            if(percentage < 0 || percentage>100){ **//check if input is between 0 to 100**
                System.out.println("Input integer only between 0 to 100 inclusively.");
                System.out.print("Please input traffic jam factor again (in percentage [0-100]): ");
            }
        }while(percentage < 0 || percentage>100); **//keep looping until input is valid**
        //distance from ITC to Airport is 30Km = 30000m
        //speed 30km/h
        totalSeconds = (int)Math.ceil((30000.0f ) / ((30 / 3.6f) - ((30 / 3.6f) * (percentage) / 100))); **//convert speed from km/h to m/s and calculate total seconds needed to travel**
        minutes = (totalSeconds / 60); **//convert total seconds to minutes**
        hours = (minutes / 60); **//convert minutes to hours**
        minutes -= hours * 60;
        seconds = (totalSeconds % 60); **// get remaining seconds after converting to minutes**
        System.out.printf("Travelling Duration = %02d:%02d:%02d",hours,minutes,seconds); **//print result in format of HH:MM:SS**
        sc.close();
    }
}
```

### Quiz 2 - Question 4

```java
package QuizQuestion;
/*Display even numbers (ex: 2, 4, 6, 8, etc.)
located between A and 500.
Where A is given by user (0<A<500).
 */
import java.util.Scanner;
public class Quiz2Question4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); **//create Scanner object to read user input**
        int A; **// declare variable A to store user input**
        do{ **//loop until user input is valid**
            System.out.print("Input A: "); **//prompt user to input A**
            A = sc.nextInt();
        }while(A<0 && A>500); **//check if input is between 0 and 500**
        A = A + A % 2; **// if A is odd, add 1 to make it even. If A is even, it remains unchanged.**
        while(A <= 500){ **//loop until A is greater than 500**
            System.out.printf("%d ",A); **//print A followed by a space**
            A += 2;
        }
        sc.close();
    }
}
```

### Quiz 2 - Question 5

```java
package QuizQuestion;
/* If we input 20 30 50 in sequences, the proram below will produce result as following:
 *
------- Program for converting time to seconds -------
Please input hours: 20
Please input minutes: 30
Please input seconds: 50

Number of seconds = 20x3600 + 30x60 + 50 = 73850
    */
import java.util.Scanner;
public class Quiz2Question5 {
        public static void main(String[] args) {
        System.out.println("------- Program for converting from seconds into hours:minutes:seconds ------- ");
        Scanner sc = new Scanner(System.in);
        int totalSeconds, hours, minutes, seconds; **// Declare four integer variables, totalSeconds, hours, minutes, and seconds.**
        System.out.print("Please input hours: ");
        hours = sc.nextInt(); **// Prompt the user to input hours and read the input using the Scanner object, storing it in the variable hours.**
        System.out.print("Please input minutes: ");
        minutes = sc.nextInt();
        System.out.print("Please input seconds: "); **// Prompt the user to input seconds and read the input using the Scanner object, storing it in the variable seconds.**
        seconds = sc.nextInt();
       
        totalSeconds = (hours * 3600) + (minutes * 60) + seconds; **// Calculate the total number of seconds by multiplying hours by 3600, minutes by 60, and adding all three components together.**

        System.out.printf("Number of seconds = %dx3600 + %dx60 + %d = %d\n", hours, minutes, seconds, totalSeconds);
        // Format the output to display the calculation of total seconds, showing the contribution of hours, minutes, and seconds in the format "Number of seconds = Hx3600 + Mx60 + S = TotalSeconds", where H, M, S, and TotalSeconds are replaced with their respective values.
        sc.close();
    }
}
```

### Quiz 2 - Question 6

```java
package QuizQuestion;
/* Write a Java program to display a triangle made from stars. The number of lines and number of columns is given by user. Example:

*
**
***
****
*****
*/

import java.util.Scanner;

public class Quiz2Question6 {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input number of lines: ");
        int lines = sc.nextInt();
        System.out.print("Enter number of columns: ");
        int columns = sc.nextInt();
        int k;
        if (lines>=columns){
            k = lines;
        } else {
            k = columns;
        }

        for (int i = 1; i <= k; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Quiz 2 - Question 7

```java
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
        int totalSeconds, hours, minutes, seconds; **// Declare four integer variables, totalSeconds, hours, minutes, and seconds.**
        System.out.print("Please input hours: ");
        hours = sc.nextInt(); **// Prompt the user to input hours and read the input using the Scanner object, storing it in the variable hours.**
        System.out.print("Please input minutes: ");
        minutes = sc.nextInt();
        System.out.print("Please input seconds: "); **// Prompt the user to input seconds and read the input using the Scanner object, storing it in the variable seconds.**
        seconds = sc.nextInt();
       
        totalSeconds = (hours * 3600) + (minutes * 60) + seconds; **// Calculate the total number of seconds by multiplying hours by 3600, minutes by 60, and adding all three components together.**

        System.out.printf("Number of seconds = %dx3600 + %dx60 + %d = %d\n", hours, minutes, seconds, totalSeconds);
        // Format the output to display the calculation of total seconds, showing the contribution of hours, minutes, and seconds in the format "Number of seconds = Hx3600 + Mx60 + S = TotalSeconds", where H, M, S, and TotalSeconds are replaced with their respective values.
        sc.close();
    }
}
```

### Quiz 2 - Question 8

```java
package QuizQuestion;
/*If we input NOON in program below it produces output:
Please gives a word to check: NOON
NOON is a Palindrome
 */
import java.util.Scanner;
public class Quiz2Question8 {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String pal; **//declare variable pal to store user input**
    System.out.print("Please gives a word to check: "); **//prompt user to input a word**
    pal = sc.nextLine();
    StringBuilder input1 = new StringBuilder(pal); **//create a StringBuilder object input1 and initialize it with the value of pal**
    String rev = input1.reverse().toString(); **//reverse the string using StringBuilder's reverse() method and convert it back to a String, storing the result in variable rev**
    if(rev.equalsIgnoreCase(pal)){ **//compare the reversed string with the original string, ignoring case sensitivity, to check if it is a palindrome**
        System.out.printf("%s is a Palindrome\n", pal); **//if the reversed string is equal to the original string, print that it is a palindrome**
    }else{
        System.out.printf("%s is NOT a Palindrome\n", pal); **//if the reversed string is not equal to the original string, print that it is not a palindrome**
    }
    sc.close(); **//close the Scanner object to prevent resource leaks**
    }   
}
```

### Quiz 3 - Question 1

```java
package QuizQuestion;
//Calculator of two numbers
import java.util.Scanner;
public class Quiz3Question1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter the second number: ");
        double num2 = scanner.nextDouble();
        System.out.println("Choose operation: ");
        System.out.println("1. Addition");    
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");

        int choice = scanner.nextInt(); **// choice = scanner.nextInt()**
        double result = 0;
        switch (choice) {
            case 1:
                result = num1 + num2;
                System.out.printf("Result: %.2f\n", result);
                break;
            case 2:
                result = num1 - num2;
                System.out.printf("Result: %.2f\n", result);
                break;
            case 3:
                result = num1 * num2;
                System.out.printf("Result: %.2f\n", result);
                break;
            case 4:
                if (num2 != 0) {
                    result = num1 / num2;
                    System.out.printf("Result: %.2f\n", result);
                } else {
                    System.out.println("Error: Division by zero is not allowed.");
                }
                break;
            default:
                System.out.println("Invalid choice. Please select a valid operation.");
            }
        scanner.close();
    }
}
```

### Quiz 3 - Question 2

```java
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

        if (time == 0) { **// time == 0**
            System.out.println("Time must be greater than zero.");
        } else {
            double speed = distance / time;
            System.out.printf("The speed is: %.2f km/h\n", speed);
        }
        scanner.close();
    }
}
```

### Quiz 3 - Question 3

```java
package QuizQuestion;

import java.util.Scanner;

public class Quiz3Question3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the radius of the circle: ");
        double radius = scanner.nextDouble();
        double area = Math.PI * radius * radius; **// Math.PI * radius * radius**
        System.out.printf("The area of the circle with radius %.2f is: %.2f\n", radius, area);
        scanner.close();
    }
}
```

### Quiz 3 - Question 4

```java
package QuizQuestion;

import java.util.Scanner;

public class Quiz3Question4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the length of the rectangle: ");
        double length = scanner.nextDouble();
        System.out.print("Enter the width of the rectangle: ");
        double width = scanner.nextDouble();
        double area = length * width; 
        System.out.printf("The area of the rectangle with length %.2f and width %.2f is: %.2f\n", length, width, area);
        scanner.close(); **// scanner.close()**
    }
    
}
```

### Quiz 3 - Question 5

```java
package QuizQuestion;
// is leap year?
import java.util.Scanner;
public class Quiz3Question5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a year: ");
        int year = scanner.nextInt();
        boolean isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0); **// year % 4 == 0 && year % 100 != 0**
        if (isLeapYear) {
            System.out.println(year + " is a leap year.");
        } else {
            System.out.println(year + " is not a leap year.");  
        }           
        scanner.close();
    }
}
```

### Quiz 3 - Question 6

```java
package QuizQuestion;
// calculate exchange rate
import java.util.Scanner;
public class Quiz3Question6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter amount in original currency: ");
        double originalAmount = scanner.nextDouble();

        System.out.print("The equivalent amount in the target currency is: ");
        double targetAmount = scanner.nextDouble();

        double exchangeRate = targetAmount / originalAmount; **// targetAmount / originalAmount**
        System.out.printf("The exchange rate is %.2f.\n", exchangeRate);
        scanner.close();
    }
}
```

### Quiz 3 - Question 7

```java
package QuizQuestion;
// name + age print
import java.util.Scanner;
public class Quiz3Question7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.println("Hello " + name + ", you are " + age + " years old."); **// + name +**
        scanner.close();
    }
}
```

### Quiz 3 - Question 8

```java
package QuizQuestion;

import java.util.Scanner;
    public class Quiz3Question8 {
        public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
       
        System.out.print("Enter a string: ");
        String input = scanner.nextLine(); **// nextLine()**
       
        int wordCount = 0;
        if(input != null && !input.trim().isEmpty() ){ **// isEmpty()**
            String[] words = input.trim().split("\\s+"); **// split("\\s+")**
            wordCount = words.length; **// wordCount**
        }
        System.out.println("Number of words: " + wordCount); **// wordCount**
       
        scanner.close(); **// close()**
    }
}
```

### Quiz 3 - Question 9

```java
package QuizQuestion;
import java.util.Scanner;
public class Quiz3Question9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int num1 = scanner.nextInt();

        System.out.print("Enter second number: ");
        int num2 = scanner.nextInt();

        int a = Math.abs(num1);
        int b = Math.abs(num2);
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        int gcd = a;
        int lcm = Math.abs(num1 * num2) / gcd; **// Math.abs(num1 * num2)**
        System.out.println("The LCM of " + num1 + " and " + num2 + " is: " + lcm);
        scanner.close();
    }
    
}
```

### Quiz 3 - Question 10

```java
package QuizQuestion;
import java.util.Scanner;
public class Quiz3Question10 {
 public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("How many numbers do you want to enter? ");
        int count = scanner.nextInt(); **//nextInt()**
        if (count <= 0) {
            System.out.println("Please enter a positive number of elements.");
            scanner.close();
            return; **//return**
        }
        double[] numbers = new double[count]; **// count**
        System.out.println("Enter the numbers:");
        for (int i = 0; i < count; i++) { **//count**
            System.out.print("Number " + (i + 1) + ": ");
            numbers[i] = scanner.nextDouble(); **// nextDouble()**
        }
        double sum = 0;
        for (double number : numbers) { **// numbers**
            sum += number;
        }
        double average = sum / numbers.length; **// numbers**
        System.out.printf("Average: %.2f\n", average);
       
        scanner.close();
    }
}
```

### Quiz 3 - Question 11

```java
package QuizQuestion;

import java.util.Scanner;
import java.util.Random;

public class Quiz3Question11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int targetNumber = random.nextInt(100) + 1;
        int attempts = 0;
        boolean hasGuessedCorrectly = false;

        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("I have selected a number between 1 and 100. Can you guess it?");
        while (!hasGuessedCorrectly) {
            System.out.print("Enter your guess: ");
            int guess = scanner.nextInt();
            attempts++; **// attempts++**

            if (guess < targetNumber) {
                System.out.println("Too low! Try again.");
            } else if (guess > targetNumber) {
                System.out.println("Too high! Try again.");
            } else {
                hasGuessedCorrectly = true;
                System.out.println("Congratulations! You've guessed the number " + targetNumber + " in " + attempts + " attempts.");
            }
        }

        scanner.close();
    }
}
```

### Quiz 3 - Question 12

```java
package QuizQuestion;
// use switch case 1 is celcius to fahrenheit, 2 is fahrenheit to celsius.
import java.util.Scanner;
public class Quiz3Question12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose conversion type:");
        System.out.println("1: Celsius to Fahrenheit");
        System.out.println("2: Fahrenheit to Celsius");
        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                System.out.print("Enter temperature in Celsius: ");
                double celsius = scanner.nextDouble();
                double fahrenheit = (celsius * 9 / 5) + 32;
                System.out.printf("%.2f Celsius is %.2f Fahrenheit\n", celsius, fahrenheit);
                break;
            case 2:
                System.out.print("Enter temperature in Fahrenheit: ");
                fahrenheit = scanner.nextDouble();
                celsius = (fahrenheit - 32) * 5 / 9; **// (fahrenheit - 32) * 5.0/9.0**
                System.out.printf("%.2f Fahrenheit is %.2f Celsius\n", fahrenheit, celsius);
                break;
            default:
                System.out.println("Invalid choice. Please select 1 or 2.");
        }
        scanner.close();
    }
}
```

### Quiz 3 - Question 13

```java
package QuizQuestion;
// is odd or even
import java.util.Scanner;
public class Quiz3Question13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();
        
        if (number % 2 == 0) { **// number % 2 == 0**
            System.out.println(number + " is even.");
        } else {
            System.out.println(number + " is odd.");
        }
        
        scanner.close();
    }
    
}
```

### Quiz 3 - Question 14

```java
package QuizQuestion;
// average of 3 numbers
import java.util.Scanner;
public class Quiz3Question14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        double num1 = scanner.nextDouble();
        
        System.out.print("Enter the second number: ");
        double num2 = scanner.nextDouble();
        
        System.out.print("Enter the third number: ");
        double num3 = scanner.nextDouble();
        
        double average = (num1 + num2 + num3) / 3; **// (num1 + num2 + num3) / 3**
        System.out.println("The average of the three numbers is: " + average);
        
        scanner.close();
    }
}
```

### Quiz 3 - Question 15

```java
package QuizQuestion;
import java.util.Scanner;
public class Quiz3Question15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("How many item in your cart? ");
        int itemCount = scanner.nextInt();

        if (itemCount <= 0) { **// itemCount**
            System.out.println("Item count cannot be negative.");
            scanner.close();
            return;
        }
        double subtotal = 0;

        System.out.println("Enter the price of each item:");
        for (int i = 0; i < itemCount; i++) { **// itemcount**
            System.out.print("Item " + (i + 1) + " price:$: ");
            double price = scanner.nextDouble(); **// scanner.nextDouble()**
            if (price < 0) { **// price**
                System.out.println("Price cannot be negative.");
                scanner.close();
                return;
            }
            subtotal += price;
        }
        System.out.println("Enter tax rate (as a percentage): ");
        double taxRate = scanner.nextDouble(); **// scanner.nextDouble()**

        double taxAmount = subtotal * (taxRate / 100); **// taxRate**
        double totalCost = subtotal + taxAmount; **// taxAmount**
        
        System.out.printf("Shopping cart summary\n");
        System.out.printf("Subtotal: $%.2f\n", subtotal);
        System.out.printf("Tax (%.2f%%): $%.2f\n", taxRate, taxAmount); **//taxRate**
        System.out.printf("Total Cost: $%.2f\n", totalCost);

        scanner.close(); **// .close()**
    }
}
```

### Quiz 3 - Question 16

```java
package QuizQuestion;

//sum all even from 1 to given
import java.util.Scanner;
public class Quiz3Question16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();

        int sum = 0;
        
        for (int i = 2; i <= n; i += 2) {
            sum += i; **// sum += i;**
        }
        System.out.println("Sum of even numbers from 1 to " + n + " is: " + sum);
        scanner.close();
    }
}
```

### Quiz 3 - Question 17

```java
package QuizQuestion;
// sum of first and second number 
import java.util.Scanner;
public class Quiz3Question17 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter the second number: ");
        double num2 = scanner.nextDouble();
        double sum = num1 + num2; **// double sum = num1 + num2;**
        System.out.println("The sum is: " + sum);

        scanner.close();
    }

}
```

<!-- END JAVA QUIZ REVIEW -->

