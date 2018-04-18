package gb;

import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;

public class GrandpaBernie {
	
	HashMap<String, List<Integer>> mem;
	HashSet<String> sorted;
	
	public GrandpaBernie(int numOfMemories) {
		mem = new HashMap<String, List<Integer>>();
		sorted = new HashSet<String>();
	}

	public static void main(String [] args) {
		Scanner sc = new Scanner(new BufferedInputStream(System.in));
		int numOfMemories = sc.nextInt();
		
		GrandpaBernie gb = new GrandpaBernie(numOfMemories);
		
		for (int memory = 0; memory < numOfMemories; memory++) {
			gb.addMemory(sc.next(), sc.nextInt());
		}
		
		int numOfQueries = sc.nextInt();

		for (int querie = 0; querie < numOfQueries; querie++) {
			System.out.print(gb.getYear(sc.next(), sc.nextInt()) + "\n");
		}	
		sc.close();
	}

	private Integer getYear(String country, int visit) {		
		List<Integer> years = mem.get(country);
		if (!sorted.contains(country)) {
			Collections.sort(years);;
			sorted.add(country);
			mem.put(country, years);
		}
		return years.get(visit - 1);
	}

	private void addMemory(String country, int year) {
		List<Integer> years = mem.get(country);
		if (years == null) {
			years = new ArrayList<Integer>();
			mem.put(country, years);
		}
		years.add(year);
	}
}
