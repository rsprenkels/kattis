package t9;

import java.io.BufferedInputStream;
import java.util.Arrays;
import java.util.Scanner;

public class T9 {
	
	static String [] t9Codes = {"2", "22", "222","3","33","333","4","44","444","5","55","555","6","66","666","7","77","777","7777","8","88","888","9","99","999","9999"};
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		int numOfTestCases = Integer.parseInt(scan.nextLine());
		
		for (int testCase=1; testCase <= numOfTestCases; testCase++) {
			String line = scan.nextLine();
			String output = "";
			String code = "";
			for (char c : line.toCharArray()) {
				if (c == ' ') {
					code = "0";
				} else {
					code = t9Codes[c - 'a'];
				}
				if ((output.length() > 0) && output.charAt(output.length()-1) == code.charAt(0)) {
					output += " ";
				}
				output += code;
			}
			System.out.printf("Case #%d: %s\n", testCase, output);
		}
		scan.close();
	}
}