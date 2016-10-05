package ladder;

import java.io.BufferedInputStream;

import java.util.Scanner;

public class Ladder {
		
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		
		int h = scan.nextInt();
		int angle = scan.nextInt();
		
		int minLadderLen = (int) Math.ceil(h / Math.sin(Math.toRadians(angle)));
		
		System.out.print (minLadderLen + "\n");
		scan.close();
	}
}
