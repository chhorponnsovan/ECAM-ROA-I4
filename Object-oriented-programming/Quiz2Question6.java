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
