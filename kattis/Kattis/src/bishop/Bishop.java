package bishop;

import java.io.BufferedInputStream;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Bishop {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		PrintStream ps = new PrintStream(System.out);

		while (scan.hasNextLine()) {
			long N = Integer.parseInt(scan.nextLine());
			ps.printf(Locale.CANADA, "%d\n", N>1 ? 2*N -2 : 1);
		}
		ps.flush();
		scan.close();
	}
}