
//prints out the lyrics to the classic song, "99 bottles of Beer on the Wall."
 public class BottlesofBeer {

     public static void main(String[] args) {
     	  int beer = 99;
     	  String bottles = " bottles";
	  while(beer > 0) {
	

	 
	   System.out.println(beer + bottles + " of beer on the wall ");
	   System.out.println(beer +  bottles + " of beer,\n");
	   System.out.println("Take one down, pass it around, \n");
	   beer --;
	   
	      if (beer == 1) { 
	  
	  bottles = " bottle";
	  }
	  if (beer > 0) {
	  
	   System.out.println(beer + bottles + " of beer on the wall. \n");
	  }
        	  
        	  

     else { //there are no more bottles left at all
          System.out.println("No more bottles of beer on the wall, no more bottles of beer,\n");
          System.out.println("No more bottles of beer on the wall, no more bottles of beer,");
	  System.out.println("Go to the store and buy some more! 99 Bottles of beer on the wall!");
    }
   }
}
}
