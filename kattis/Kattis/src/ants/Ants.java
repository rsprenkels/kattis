package ants;

import java.util.Arrays;
import java.util.Scanner;

public class Ants {

	public static void main(String[] args) {
		new Ants().processInput();
	}

	public void processInput() {
		Scanner scan = new Scanner(System.in);
		int numberOfCases = scan.nextInt();
		scan.nextLine();
		for (int caseNumber = 1; caseNumber <= numberOfCases; caseNumber++) {
			int poleLength = scan.nextInt();
			int numberOfAnts = scan.nextInt();
			int [] ants = new int[numberOfAnts];
			for (int antCounter = 0; antCounter < numberOfAnts; antCounter++) {
				ants[antCounter] = scan.nextInt();
			}
			
			System.err.println (caseNumber + " " + poleLength + " " + numberOfAnts + " ");
			Arrays.sort(ants);
			Pair<Integer,Integer> result = calculateMinMaxDuration(ants, 0, poleLength);
			System.out.print(result.t + " " + result.u + "\n");
		}
		scan.close();
	}
	
	public Pair<Integer, Integer> calculateMinMaxDuration(int [] ants, int varyFromThisAntOnwards, int poleLength) {

		if (varyFromThisAntOnwards < ants.length) {
			Pair<Integer,Integer> p1 = calculateMinMaxDuration(ants, varyFromThisAntOnwards + 1, poleLength);
			ants[varyFromThisAntOnwards] *= -1;
			Pair<Integer,Integer> p2 = calculateMinMaxDuration(ants, varyFromThisAntOnwards + 1, poleLength);
			int min = Math.min(p1.t, p2.t);
			int max = Math.max(p1.u, p2.u);
			System.err.println("so far: " + min + " " + max);
			return new Pair<Integer, Integer>(min,max);
		} else {
			System.err.print("checking ant combi: ");			
			for (int antNo = 0; antNo < ants.length; antNo++) {
				System.err.print(ants[antNo] + " ");
			}
			System.err.println();
			int time = 0;
			int antsRemaining = ants.length;
			int [] oldAnts = ants.clone();
			int [] newAnts = new int[ants.length];
			int ant;
			while (antsRemaining > 0) {
				time++;
				for (int antNo = 0; antNo < oldAnts.length; antNo++) {
					// you fall off at 0 and at poleLength
					// negativeL: moving left. Positive: moving right.
					ant = oldAnts[antNo];
					if (ant == -1) {
						newAnts[antNo] = 0; // fell off
						antsRemaining--;
					} else if (ant == poleLength - 1) {
						newAnts[antNo] = poleLength; // fell off
						antsRemaining--;
					} else {
						if (ant < 0) { // if its moving left
							if (antNo == 0) { // if it is the leftmost ant
								newAnts[antNo] = ant + 1;
							} else {  //TODO model also the 1 -3 situation where they result in 2 -2 and then in -1 3.
								if(oldAnts[antNo - 1] == -(ant + 1)) { // if the ant on our left is direct adjacent, and moving right
									newAnts[antNo] = -ant; // same spot, but opposite direction	
								} else if (oldAnts[antNo - 1] == -ant) {
									newAnts[antNo] = -ant + 1; // we WERE on same spot, but opposite direction, now bounced back and 1 further
								} else {
									newAnts[antNo] = ant + 1; // moved one more to the left e.g. -7 to -6
								}
							}
						} else { // its moving right
							if (antNo == oldAnts.length - 1) { // if its the rightmost ant
								newAnts[antNo] = ant + 1; // now one more to the right
							} else {
								if (oldAnts[antNo + 1] == -(ant+1)) { // the ant to our right is direct adjacent and moving left
									newAnts[antNo] = -ant; // same spot, but opposite direction
								} else if (oldAnts[antNo + 1] == -ant ) {
									newAnts[antNo] = -ant + 1; // we WERE on same spot, but opposite direction, now bounced back and 1 further
								} else {
									newAnts[antNo] = ant + 1; // moved one more to the right, e.g. 7 to 8
								}
							}
						}
					}
				}
				if (antsRemaining > 0) {
					oldAnts = new int[antsRemaining];
					int newAntindex = 0;
					for (int antNo = 0; antNo < newAnts.length; antNo++) {
						if (newAnts[antNo] != 0 && newAnts[antNo] != poleLength) {
							if (newAntindex < antsRemaining) {
								oldAnts[newAntindex++] = newAnts[antNo];
							} else {
								System.err.println("bad stuff");
							}
						}
					}
				}
			}
			return new Pair<Integer, Integer>(time,time);			
		}
	}
}


