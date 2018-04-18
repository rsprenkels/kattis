package vauvau;

import java.util.Scanner;

public class Vauvau {

	public static void main(String[] args) {
		new Vauvau().processInput();
	}

	public void processInput() {
		Scanner scan = new Scanner(System.in);
		
		int A = scan.nextInt();
		int B = scan.nextInt();
		int C = scan.nextInt();
		int D = scan.nextInt();

		int pmg[] = new int [3];
		pmg[0] = scan.nextInt();
		pmg[1] = scan.nextInt();
		pmg[2] = scan.nextInt();

		for (int visit = 0; visit < pmg.length; visit++) {
			int arrived = pmg[visit] - 1;
			boolean annoyedAB = (arrived % (A + B)) < A;
			boolean annoyedCD = (arrived % (C + D)) < C;
			if (annoyedAB && annoyedCD) {
				System.out.print("both\n");
			} else if (!annoyedAB && !annoyedCD) {
				System.out.print("none\n");
			} else {
				System.out.print("one\n");				
			}
		}
		scan.close();
	}
}


