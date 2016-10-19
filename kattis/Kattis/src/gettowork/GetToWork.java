package gettowork;

import java.io.BufferedInputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class GetToWork {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		PrintStream ps = new PrintStream(System.out);
//		GetToWork bs = new GetToWork();

		int numOfTestcases = Integer.parseInt(scan.nextLine());
		for (int testCase = 1; testCase <= numOfTestcases; testCase++) {
			int numOfTowns = scan.nextInt();
			int officeTown = scan.nextInt();
			int numOfEmployees = scan.nextInt();
			HashMap<Integer, ArrayList<Integer>> towns = new HashMap<Integer, ArrayList<Integer>>();
			for (int townIndex = 1; townIndex <= numOfTowns; townIndex++) {
				towns.put(townIndex, new ArrayList<Integer>());
			}
			
			for (int employeeIndex = 0; employeeIndex < numOfEmployees; employeeIndex++) {
				int homeTown = scan.nextInt();
				int carCapacity = scan.nextInt();
				ArrayList<Integer> oneTown = towns.get(homeTown);
				oneTown.add(carCapacity);
			}
			ps.printf("Case #%d:", testCase);
			int [] carsRunning = new int[numOfTowns];
			boolean stillPossible = true;
			for (int townIndex = 1; stillPossible && townIndex <= numOfTowns; townIndex++) {
				if (townIndex == officeTown) {
					carsRunning[townIndex-1] = 0;
					continue;
				}
				ArrayList<Integer> oneTown = towns.get(townIndex);
				Collections.sort(oneTown);
				int fillFrom = 0;
				int carsNeeded = 0;
				for (int index = oneTown.size()-1; stillPossible && (index >= 0); index--) {
					int carCapacity = oneTown.get(index);
					stillPossible = carCapacity-- > 0; // put ourselves into own car, if possible
					carsNeeded++;
					while (carCapacity > 0 && fillFrom < index) {
						carCapacity--;
						fillFrom++;
					}
					if (fillFrom == index) {
						break;
					}
				}
				carsRunning[townIndex-1] = carsNeeded;
				System.err.printf("%d %d\n", townIndex, oneTown.size());
			}			
			if (stillPossible) {
				for (int townIndex = 0; townIndex < numOfTowns; townIndex++) {
					ps.printf(" %d", carsRunning[townIndex]);
				}
				ps.print("\n");
			} else {
				ps.printf(" IMPOSSIBLE\n");				
			}
			System.err.print("\n\n");
		}
		ps.flush();
		scan.close();
	}
}