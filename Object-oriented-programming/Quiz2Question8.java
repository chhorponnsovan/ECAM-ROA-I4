/*If we input NOON in program below it produces output:
Please gives a word to check: NOON
NOON is a Palindrome
 */
import java.util.Scanner;
public class Quiz2Question8 {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String pal; //declare variable pal to store user input
    System.out.print("Please gives a word to check: "); //prompt user to input a word
    pal = sc.nextLine();
    StringBuilder input1 = new StringBuilder(pal); //create a StringBuilder object input1 and initialize it with the value of pal
    String rev = input1.reverse().toString(); //reverse the string using StringBuilder's reverse() method and convert it back to a String, storing the result in variable rev
    if(rev.equalsIgnoreCase(pal)){ //compare the reversed string with the original string, ignoring case sensitivity, to check if it is a palindrome
        System.out.printf("%s is a Palindrome\n", pal); //if the reversed string is equal to the original string, print that it is a palindrome
    }else{
        System.out.printf("%s is NOT a Palindrome\n", pal); //if the reversed string is not equal to the original string, print that it is not a palindrome
    }
    sc.close(); //close the Scanner object to prevent resource leaks
    }   
}
