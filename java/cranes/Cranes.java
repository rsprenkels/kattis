package cranes;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Cranes {

	static long counter = 0;
	
	public static void main(String[] args) {
		new Cranes().processInput();
	}

	void processInput() {
		Scanner scan = new Scanner(System.in);
		Set<Crane> craneSet = new HashSet<Crane>();
		Set<Crane> emptySet = new HashSet<Crane>();
		
		int totalTestCases = scan.nextInt();
		scan.nextLine();
		for (int testCaseIndex = 0; testCaseIndex < totalTestCases; testCaseIndex++) {
			craneSet.clear();

			int totalCranePositions = scan.nextInt();			
			scan.nextLine();
			for (int craneIndex = 0; craneIndex < totalCranePositions; craneIndex++) {
				craneSet.add(new Crane(scan.nextInt(), scan.nextInt(), scan.nextInt()));
			}
			// System.err.println("Testing this set: " + craneSet);
		
			int area = maxPossibleArea(emptySet, craneSet, 0);
			System.err.printf ("Result counter is: %d\n", Cranes.counter);
			System.out.print (area + "\n");
		}
		scan.close();
	}

	private int maxPossibleArea(Set<Crane> selectedCranes, Set<Crane> remainingCranes, int curBiggest) {
		if (remainingCranes.size() == 0) {
			return (Math.max(getArea(selectedCranes), curBiggest));			
		} else {
			// System.err.printf("%d cranes left in remaining ", remainingCranes.size());
			// System.err.println (remainingCranes);
			int trackBiggest = curBiggest;
			Set<Crane> nextRemaining = new HashSet<Crane>();
			Set<Crane> nextSelected = new HashSet<Crane>();
			for (Crane crane : remainingCranes) {
				nextRemaining.clear();
				nextRemaining.addAll(remainingCranes);
				nextRemaining.remove(crane);
				nextSelected.clear();
				nextSelected.addAll(selectedCranes);
				if (addIsAllowed(nextSelected, crane)) {
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
			Cranes.counter++;
			int dX = selected.x - newCrane.x;
			int dY = selected.y - newCrane.y;
			float distance = (float) Math.sqrt(dX * dX + dY * dY);
			if (distance < selected.radius + newCrane.radius) {
				return false;
			}
		}
		return true;
	}
}
