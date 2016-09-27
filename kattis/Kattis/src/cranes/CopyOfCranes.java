package cranes;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class CopyOfCranes {

	public static void main(String[] args) {
		new CopyOfCranes().processInput();
	}

	void processInput() {
		Scanner scan = new Scanner(System.in);
		
		int totalTestCases = scan.nextInt();
		scan.nextLine();
		for (int testCaseIndex = 0; testCaseIndex < totalTestCases; testCaseIndex++) {
			Set<Crane> craneSet = new HashSet<Crane>();

			int totalCranePositions = scan.nextInt();			
			scan.nextLine();
			for (int craneIndex = 0; craneIndex < totalCranePositions; craneIndex++) {
				Crane crane = new Crane(scan.nextInt(), scan.nextInt(), scan.nextInt());
				craneSet.add(crane);
			}
			// System.err.println("Testing this set: " + craneSet);
		
			int area = maxPossibleArea((Set<Crane>) new HashSet<Crane>(), craneSet, 0);
			// System.err.print ("Result is: " + area + "\n\n");
			System.out.print (area + "\n");
		}
		scan.close();
	}

	private int maxPossibleArea(Set<Crane> selectedCranes, Set<Crane> remainingCranes, int curBiggest) {
		if (remainingCranes.size() == 0) {
			return (Math.max(getArea(selectedCranes), curBiggest));			
		} else {		
			int trackBiggest = curBiggest;
			for (Crane crane : remainingCranes) {
				Set<Crane> nextRemaining = new HashSet<Crane>(remainingCranes);
				Set<Crane> nextSelected = new HashSet<Crane>(selectedCranes);
	
				nextRemaining.remove(crane);
				if (addIsAllowed(selectedCranes, crane)) {
					nextSelected.add(crane);
				}
				trackBiggest = maxPossibleArea(nextSelected, nextRemaining, trackBiggest);
			}
			return trackBiggest;
		}
	}

	private int getArea(Set<Crane> craneSet) {
		int area = 0;
		for (Crane crane : craneSet) {
			area += (crane.radius * crane.radius);
		}
		return area;
	}

	private boolean addIsAllowed(Set<Crane> alreadySelected, Crane newCrane) {
		for (Crane selected : alreadySelected) {
			double dX = selected.x - newCrane.x;
			double dY = selected.y - newCrane.y;
			double distance = Math.sqrt(dX * dX + dY * dY);
			if (distance < selected.radius + newCrane.radius) {
				return false;
			}
		}
		return true;
	}
}
