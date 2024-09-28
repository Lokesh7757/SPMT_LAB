import java.util.Scanner;

public class Triangle{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Accept three sides of the triangle
        System.out.println("Enter side 1: ");
        int side1 = scanner.nextInt();
        
        System.out.println("Enter side 2: ");
        int side2 = scanner.nextInt();
        
        System.out.println("Enter side 3: ");
        int side3 = scanner.nextInt();
        
       if(side1==10 || side2==10 || side3==10)
	{
      
            if (side1 == side2 && side2 == side3) {
                System.out.println("This is an Equilateral triangle.");
            } else if (side1 == side2 || side2 == side3 || side1 == side3) {
                System.out.println("This is an Isosceles triangle.");
            } else {
                System.out.println("This is a Scalene triangle.");
            }
        } 
		else{ System.out.println("Enter the side less then 10");
        }
    }  
     
    }