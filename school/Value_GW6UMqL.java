import java.util.Scanner;

class Value{


	//int mayai;



	boolean checkIntValue(int mayai){
		boolean abool = false;

		if(mayai>0) {
			abool = true;


			}
		return abool;
		}

	 public static void main ( String [] args){
		 Scanner input = new Scanner(System.in);
		 intValue iv = new intValue();
		  System.out.print("Enter the  number: ");
		 int maya = input.nextInt();
//calling our method
		 System.out.println("The value entered is : " + iv.checkIntValue());


		 }





	}