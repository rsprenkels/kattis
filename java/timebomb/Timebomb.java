package timebomb;

import java.util.Scanner;

public class Timebomb {

	public static void main(String[] args) {
		new Timebomb().processInput();
	}

	public void processInput() {
		Scanner scan = new Scanner(System.in);
		String [][] digits = new String [8][5];
		int lineNumber = 0;
		int totalDigits = 0;
				
		while (scan.hasNextLine()) {
			String oneLine = scan.nextLine() + " ";
			int digit = 0;
			while (oneLine.length() >= 3) {
				String chunck = oneLine.substring(0, 3);
				oneLine = oneLine.substring(4);
				digits[digit][lineNumber] = chunck;
				digit++;
			}
			totalDigits = digit;
			lineNumber++;
		}		
		scan.close();

		boolean allDigitsValid = true;
		int codeValue = 0;
		for (int digit = 0; allDigitsValid && (digit < totalDigits); digit++) {
			StarChar c = new StarChar(digits[digit]);
			allDigitsValid = c.isValidDigit();
			codeValue = 10 * codeValue + c.charValue;
		}
		System.err.print("code: " + codeValue + "  ");
		if (allDigitsValid && (codeValue % 6 == 0)) {
			System.out.print("BEER!!\n");
		} else {	
			System.out.print("BOOM!!\n");
		}
	}
}


