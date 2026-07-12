package QuizQuestion;
import java.util.Scanner;
public class Quiz3Question15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("How many item in your cart? ");
        int itemCount = scanner.nextInt();

        if (itemCount <= 0) { // itemCount
            System.out.println("Item count cannot be negative.");
            scanner.close();
            return;
        }
        double subtotal = 0;

        System.out.println("Enter the price of each item:");
        for (int i = 0; i < itemCount; i++) { // itemcount
            System.out.print("Item " + (i + 1) + " price:$: ");
            double price = scanner.nextDouble(); // scanner.nextDouble()
            if (price < 0) { // price
                System.out.println("Price cannot be negative.");
                scanner.close();
                return;
            }
            subtotal += price;
        }
        System.out.println("Enter tax rate (as a percentage): ");
        double taxRate = scanner.nextDouble(); // scanner.nextDouble()

        double taxAmount = subtotal * (taxRate / 100); // taxRate
        double totalCost = subtotal + taxAmount; // taxAmount
        
        System.out.printf("Shopping cart summary\n");
        System.out.printf("Subtotal: $%.2f\n", subtotal);
        System.out.printf("Tax (%.2f%%): $%.2f\n", taxRate, taxAmount); //taxRate
        System.out.printf("Total Cost: $%.2f\n", totalCost);

        scanner.close(); // .close()
    }
}
