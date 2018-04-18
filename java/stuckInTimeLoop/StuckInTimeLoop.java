package stuckInTimeLoop;

import java.util.Scanner;

public class StuckInTimeLoop {

	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);
		
		int aantal = s.nextInt();
		
		for (int i = 1; i <= aantal; i++) {
			System.out.println (i + " " + "Abracadabra");
		}
		s.close();
	}

}
