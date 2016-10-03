package grandpaBernie;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Pattern;

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
		Collections.sort(countries, (a,b) -> a.name.compareTo(b.name));
		
		int totalQueries = scan.nextInt();
		for (int queryNo = 0; queryNo < totalQueries; queryNo++) {
			Country c = new Country(scan.next(), 2015);
			int searchThisTripNumber = scan.nextInt();
			
			int from = countries.indexOf(c);
			int to = countries.lastIndexOf(c);
			List<Country> justOneCountry = countries.subList(from, to + 1);
			justOneCountry.sort((a,b) -> a.year - b.year);
			System.out.print(justOneCountry.get(searchThisTripNumber - 1).year + "\n");
		}
		
		scan.close();
	}
}


