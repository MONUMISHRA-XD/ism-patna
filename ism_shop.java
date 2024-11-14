import java.util.Scanner;

class Shop {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int[] prices = {60, 80, 600, 70, 10, 10, 7, 60, 260, 60}; // Prices of the items😒
        String[] items = {
            "ALLU🥔", "MIRCHI🌶️", "LAHSUN🧄", "PYAJ🧅", "SABUN(DETOL)", "COLGATE", "MAGGIE", "AATA", "DAL", "NAMAK"
        };
        int[] quantities = new int[10]; // To store the quantities selected by the user
        int totalBill = 0;

        System.out.println("         _      _      _                                                                 _            _                    ");
        System.out.println("        | |    | |    (_)                                                               | |          | |                   ");
        System.out.println("   __ _ | |__  | |__   _  _ __    __ _ __   __      __ _   ___  _ __    ___  _ __  __ _ | |      ___ | |_  ___   _ __  ___ ");
        System.out.println("  / _` || '_ \\ | '_ \\ | || '_ \\  / _` |\\ \\ / /     / _` | / _ \\| '_ \\  / _ \\| '__|/ _` || |     / __|| __|/ _ \\ | '__|/ _ \\");
        System.out.println(" | (_| || |_) || | | || || | | || (_| | \\ V /     | (_| ||  __/| | | ||  __/| |  | (_| || |     \\__ \\| |_| (_) || |  |  __/");
        System.out.println("  \\__,_||_.__/ |_| |_||_||_| |_| \\__,_|  \\_/       \\__, | \\___||_| |_| \\___||_|   \\__,_||_|     |___/ \\__|\\___/ |_|   \\___|");
        System.out.println("                                                    __/ |                                                                 ");
        System.out.println("                                                   |___/                                                                  ");
        
        while (true) {
            System.out.println("\n1. BUY GROCERY");
            System.out.println("2. HELP DESK");
            System.out.println("3. EXIT");
            System.out.println("Choose an option: ");
            int options = sc.nextInt();

            if (options == 1) {
                System.out.println("Here are the available items:");
                for (int i = 0; i < items.length; i++) {
                    System.out.printf("%d. %s          %d rs per kg\n", (i + 1), items[i], prices[i]);
                }

                while (true) {
                    System.out.println("Enter the item number to buy (or enter 0 to calculate bill): ");
                    int itemNo = sc.nextInt();
                    if (itemNo == 0) break; // Exit when 0 is selected

                    if (itemNo >= 1 && itemNo <= items.length) {
                        System.out.println("Enter the quantity (in kg/pcs): ");
                        int quantity = sc.nextInt();

                        // Add the price to the total bill based on quantity
                        quantities[itemNo - 1] += quantity;
                    } else {
                        System.out.println("Invalid item number. Please try again.");
                    }
                }

                // Calculate total bill
                for (int i = 0; i < items.length; i++) {
                    totalBill += quantities[i] * prices[i];
                }

                System.out.println("Your total bill is: " + totalBill + " Rs");
                totalBill = 0; // Reset for next customer
            } else if (options == 2) {
                System.out.println("Welcome to the help desk! Contact us on Instagram for any help:");
                System.out.println("https://www.instagram.com/mishra__monu/");
            } else if (options == 3) {
                System.out.println("Thank you for visiting!");
                break;
            } else {
                System.out.println("Invalid option. Please try again.");
            }
        }
        sc.close();
    }
}
