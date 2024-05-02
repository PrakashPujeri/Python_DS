import java.util.Scanner;

public class subu26 {
    public static void main(String[] args) {
        double num1;
        double num2;
        double ans = 0;
        char op;
        Scanner reader = new Scanner(System.in);
        System.out.println("Enter the two num:");
        num1 = reader.nextDouble();
        num2 = reader.nextDouble();
        System.out.println("\n Enter an operator(+,-              ,*,/):");
        op = reader.next().charAt(0);
        switch (op) {
            case '+':
                ans = num1 + num2;
                break;
            case '-':
                ans = num1 - num2;
                break;
            case '*':
                ans = num1 * num2;
                break;
            case '/':
                ans = num1 / num2;
                break;
            default:
                System.out.println("error");
                break;
        }
        System.out.println(ans);
    }
}
