 import java.util.Scanner;


 class Number{
//instance variable
	 private int num1;
// instance method
	 public boolean greaterThanZero(){
		 return num1>0;
		 }


//main method
	 public static void main(String [] args){

		 //scanner object
		 Scanner input = new Scanner(System.in);

//class object
		 Number nr = new Number();
// user prompt
		 System.out.print("Enter the  number: ");
		 nr.num1 = input.nextInt();
//calling our method
		 System.out.println("The value entered is : " + nr.greaterThanZero());

		 }

	 }