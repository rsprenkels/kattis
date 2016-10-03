package grandpaBernie;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.regex.Pattern;

public class GrandpaBernie {

	public static void main(String[] args) {
		new GrandpaBernie().processInput();
	}

	public void processInput() {
		Scanner scan = new Scanner(System.in);
		int totalTrips = scan.nextInt();
		
		ArrayList<Country> countries = new ArrayList<Country>();
		
		for(int tripNo = 0; tripNo < totalTrips; tripNo++) {
			countries.add(new Country(scan.next(), scan.nextInt()));
		}
		Collections.sort(countries);
		
		int totalQueries = scan.nextInt();
		for (int queryNo = 0; queryNo < totalQueries; queryNo++) {
			String countryName = scan.next();
			int searchThisTripNumber = scan.nextInt();
			int tripNumber = 0;
			for (Country c: countries) {
				if (c.name.equals(countryName)) {
					if (++tripNumber == searchThisTripNumber) {
						System.out.print(c.year + "\n");
					}
				}
			}
		}
		
		scan.close();
	}
}


