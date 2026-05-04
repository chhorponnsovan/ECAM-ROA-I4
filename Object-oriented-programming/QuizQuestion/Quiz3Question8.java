package QuizQuestion;

import java.util.Scanner;
    public class Quiz3Question8 {
        public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
       
        System.out.print("Enter a string: ");
        String input = scanner.nextLine(); // nextLine()
       
        int wordCount = 0;
        if(input != null && !input.trim().isEmpty() ){ // isEmpty()
            String[] words = input.trim().split("\\s+"); // split("\\s+")
            wordCount = words.length; // wordCount
        }
        System.out.println("Number of words: " + wordCount); // wordCount
       
        scanner.close(); // close()
    }
}
