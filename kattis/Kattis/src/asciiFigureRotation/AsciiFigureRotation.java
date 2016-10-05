package asciiFigureRotation;

import java.io.BufferedInputStream;
import java.util.HashMap;
import java.util.Scanner;

public class AsciiFigureRotation {
	
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

		int numberOflines = Integer.parseInt(scan.nextLine());
		while (numberOflines > 0) {
			String [] image = new String[numberOflines];
			int imageWidth = 0;
			for (int lineNo = 0; lineNo < numberOflines; lineNo++) {
				image[lineNo] = scan.nextLine();
				imageWidth = Math.max(imageWidth, image[lineNo].length());
			}
			StringBuilder output = new StringBuilder(numberOflines);
			for (int outputLine = 0; outputLine < imageWidth; outputLine++) {
				for (int outputCol = numberOflines - 1; outputCol >= 0; outputCol--) {
					output.append(outputLine > image[outputCol].length() - 1 ? ' ' : convert.get(image[outputCol].charAt(outputLine)));
				}
				System.out.print(trimTrailing(output.toString()) + "\n");
				output.setLength(0);
			}
			numberOflines = Integer.parseInt(scan.nextLine());
			if (numberOflines > 0) {
				System.out.print("\n");
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
