package ants;

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
				ants[antCounter++] = scan.nextInt();
			}
			scan.nextLine();
			System.err.println (caseNumber + " " + poleLength + " " + numberOfAnts + " " + ants);
		}
	}
}
