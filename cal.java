import java.util.Scanner;
class cal
{public static void main(String[] args) {
    

{
    double num1;
    double num2;
    double ans;
    char op;
    Scanner reader = new Scanner(System.in);
    System.out.println("enter num:");
    num1=reader.nextDouble();
    num2=reader.nextDouble();
    System.out.print("enter he operator(=,-,*,/):");
    op=reader.next().charAt(0);
    switch(op) {
        case '+':
            ans=num1 + num2;
            break;
        case '-':
            ans=num1 - num2;
            break;
        case '*':
            ans=num1 * num2;
            break;
        case '/':
            ans=num1 / num2;
            break;
        default:
            System.out.print("eroor");
            break;

    }
    System.out.println("/n the result is given");
    {
        System.out.println(num1+ op +num2);
    }
}}
}