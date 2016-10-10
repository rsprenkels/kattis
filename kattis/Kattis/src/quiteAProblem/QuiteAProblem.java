package quiteAProblem;

import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class QuiteAProblem {
	
	static HashMap<Character, Character> convert;
	static {
		convert = new HashMap<Character, Character>(5);
		convert.put(' ', ' ');
		convert.put('+', '+');
		convert.put('-', '|');
		convert.put('|', '-');
	}
		
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));

		while (scan.hasNextLine()) {
			String line = scan.nextLine();
			if (line.toLowerCase().contains("problem")) {
				System.out.print("yes\n"); 
			} else {
				System.out.print("no\n"); 
			}
		}
		scan.close();
	}
	
	public static String trimTrailing(String str) {
	    if (str != null) {
	        for (int i = str.length() - 1; i >= 0; --i) {
	            if (str.charAt(i) != ' ') {
	                return str.substring(0, i + 1);
	            }
	        }
	    }
	    return str;
	}
}
