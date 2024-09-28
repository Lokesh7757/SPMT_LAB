import java.util.Scanner;

public class Commission{

    public static void main(String[] args) 
{
        Scanner scanner = new Scanner(System.in);

        
        System.out.print("Enter the total sales amount: ");
        double salesAmount = scanner.nextDouble();

        
        System.out.print("Enter the commission rate (in percentage): ");
        double commissionRate = scanner.nextDouble();

        
        double commission = calculateCommission(salesAmount, commissionRate);

        
        System.out.printf("The Total commission Is:"+commission);

       
    }

    
   	 public static double calculateCommission(double salesAmount, double commissionRate)
 	{
    	    return (salesAmount * commissionRate) / 100;
    	}
}