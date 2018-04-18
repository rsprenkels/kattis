package baconEggsSpam;

import java.io.BufferedInputStream;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.util.TreeSet;

public class BaconEggsSpam {
		
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		int noVisitors = Integer.parseInt(scan.nextLine());
		while (noVisitors != 0) {
			HashMap<String, HashSet<String>> dishes = new HashMap<String,HashSet<String>>();
			for (int visitor = 0; visitor < noVisitors; visitor++) {
				String [] words = scan.nextLine().split(" ");
				for (int dishIndex = 1; dishIndex < words.length; dishIndex++) {
					String dishName = words[dishIndex];
					if (!dishes.containsKey(dishName)) {
						dishes.put(dishName, new HashSet<String>());
					}
					dishes.get(dishName).add(words[0]);
				}
			}
			for (String dish : new TreeSet<String>(dishes.keySet())) {
				System.out.print(dish + " ");
				StringBuilder tmp = new StringBuilder();
				for (String guest : new TreeSet<String>(dishes.get(dish))) {
					tmp.append(guest + " ");					
				}
				System.out.printf("%s\n", tmp.toString().trim());
			}
			System.out.print("\n");
			noVisitors = Integer.parseInt(scan.nextLine());			
		}
		scan.close();
	}
}
