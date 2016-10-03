package grandpaBernie;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class GrandpaBernie {

	public static void main(String[] args) {
		new GrandpaBernie().processInput();
	}

	public void processInput() {
		Scanner scan = new Scanner(System.in);
		int totalTrips = scan.nextInt();
		
		List<Country> countries = new ArrayList<Country>();
		
		for(int tripNo = 0; tripNo < totalTrips; tripNo++) {
			countries.add(new Country(scan.next(), scan.nextInt()));
		}
		// Collections.sort(countries, (a,b) -> a.name.compareTo(b.name));
	    Collections.sort(countries, new Comparator<Object>() {

	        public int compare(Object o1, Object o2) {

	            String x1 = ((Country) o1).name;
	            String x2 = ((Country) o2).name;
	            int sComp = x1.compareTo(x2);

	            if (sComp != 0) {
	               return sComp;
	            } else {
	               return ((Country) o1).year - ((Country) o2).year;
	            }
	    }});		
		
		int totalQueries = scan.nextInt();
		for (int queryNo = 0; queryNo < totalQueries; queryNo++) {
			Country c = new Country(scan.next(), 2015);
			int searchThisTripNumber = scan.nextInt();
			
			int from = countries.indexOf(c);
			System.out.print(countries.get(from + searchThisTripNumber - 1).year + "\n");
		}		
		scan.close();
	}
}


