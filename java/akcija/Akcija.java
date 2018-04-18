package akcija;

import java.io.BufferedInputStream;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Akcija {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		PrintStream ps = new PrintStream(System.out);
		int numOfBooks = Integer.parseInt(scan.nextLine());
		int [] bookPrice = new int[numOfBooks];
		for (int bookIndex = 0; bookIndex < numOfBooks; bookIndex++) {
			bookPrice[bookIndex] = scan.nextInt();
		}
		Arrays.sort(bookPrice);
		int groupCounter=0;
		int totalPrice = 0;
		for (int bookIndex = numOfBooks-1; bookIndex>=0; bookIndex--) {
			if (++groupCounter % 3 != 0) {
				totalPrice += bookPrice[bookIndex];
			}
		}
		ps.printf("%d\n", totalPrice);
		ps.flush();
		scan.close();
	}
}