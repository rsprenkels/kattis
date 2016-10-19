package sumoftheothers;

import java.io.BufferedInputStream;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class SumOfTheOthers {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		PrintStream ps = new PrintStream(System.out);

		while (scan.hasNextLine()) {
			String [] valStrings = scan.nextLine().split("\\s");
			int [] values = new int[valStrings.length];
			int runningTotal = 0;
			for (int index=0; index<valStrings.length; index++) {
				int oneValue = Integer.parseInt(valStrings[index]);
				values[index] = oneValue;
				runningTotal += oneValue;
			}
			for (int index=0; index<values.length; index++) {
				if (runningTotal - values[index] == values[index]) {
					ps.printf(Locale.CANADA, "%d\n", values[index]);
					break;
				}
			}
		}
		ps.flush();
		scan.close();
	}
}