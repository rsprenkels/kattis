package yoda;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.PrintStream;
import java.util.Scanner;
import java.util.Arrays;

public class Yoda {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		PrintStream out = new PrintStream(new BufferedOutputStream(System.out));
		String first = scan.nextLine();
		String second = scan.nextLine();

		int ndxFirst = first.length() - 1;
		int ndxSecond = second.length() - 1;
		
		String newFirst = "";
		String newSecond = "";
		
		while (ndxFirst >= 0 || ndxSecond >= 0) {
			char chFirst = ndxFirst >= 0 ? first.charAt(ndxFirst) : '0';
			char chSecond= ndxSecond >= 0 ? second.charAt(ndxSecond) : '0';
			if (chFirst > chSecond) {
				newFirst = chFirst + newFirst;
			} else if (chSecond > chFirst) {
				newSecond = chSecond + newSecond;
			} else {
				newFirst = chFirst + newFirst;
				newSecond = chSecond + newSecond;
			}
			ndxFirst--;
			ndxSecond--;
		}
		if (newFirst.length() > 0) {
			out.printf("%d\n", Integer.parseInt(newFirst));
		} else {
			out.print("YODA\n");
		}
		if (newSecond.length() > 0) {
			out.printf("%d\n", Integer.parseInt(newSecond));
		} else {
			out.print("YODA\n");
		}
		out.flush();
		scan.close();
	}
}

