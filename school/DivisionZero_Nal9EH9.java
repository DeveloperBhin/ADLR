import java.util.Scanner;
class DivisionZero{
int age;

	void calculate(){
		/*int A[] ={1,2,3,4,5};
				try{
					System.out.println("an array 10 is " + A[10]);
					}
					catch(Exception e){
						System.out.println("there is a problem with code ");
				}
				finally{
					System.out.println("code error no:101; ");
					}*/

					if(age < 18){
					throw new ArithmeticException("Access denied - your age is not enough");
						}
						else{
							System.out.println("Access granted - your age is enough");
							}
		}
	public static void main(String args []){
		Scanner input = new Scanner(System.in);
		DivisionZero DZ = new DivisionZero();
		System.out.println("enter your age");
		 DZ.age=input.nextInt();
		DZ.calculate();

				}
				}