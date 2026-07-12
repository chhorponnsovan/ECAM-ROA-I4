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
        scanner.close(); // scanner.close()
    }
    
}
