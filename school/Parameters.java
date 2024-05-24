
class Parameter1{

	double w;
   double	h;
   Parameter1(double weight,double height)
   {
	   weight=w;
	   height=h;
	   }

double parameter(double w,double h){

		double area = w*h;
		return area;
		}
	}
	class Parameters extends Parameter1{
		double parameter(double d){


			double volume = parameter(7,7.2) * d;
			return volume;
			}

		public static void main(String args []){

			Parameters Pa = new Parameters();
			//parameters Ps = new Parameters();

			Pa.parameter(7.8);
		//	Ps.Parametre(7.0);
			System.out.println("The area is " + Pa.parameter(7,7.2));
			System.out.println("The volume  is " + Pa.parameter(7.8));

			}

		}