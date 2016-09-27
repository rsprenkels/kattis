package textMessaging;

import java.util.Arrays;
import java.util.Scanner;

public class TextMessaging {

	int numberOfTestCases = 0;
	
	public static void main(String[] args) {
		new TextMessaging().processInput();
	}

	void processInput() {
		Scanner scan = new Scanner(System.in);

		numberOfTestCases = scan.nextInt();
		for (int testCase = 1; testCase <= numberOfTestCases; testCase++) {
			int lettersPerKey = scan.nextInt();
			int numberOfKeys = scan.nextInt();
			int lettersInAlphabet = scan.nextInt();
			
			int[] frequencyTable = new int[lettersInAlphabet];
			for (int letterIndex = 0; letterIndex < lettersInAlphabet; letterIndex++) {
				frequencyTable[letterIndex] = scan.nextInt();
			}
			Arrays.sort(frequencyTable);
			for (int x = 0; x < lettersInAlphabet; x++) {
				System.err.println (frequencyTable[x] + " ");
			}
			int letterIndex = lettersInAlphabet;
			long numberOfStrokes = 0;
			for (int positionOnKey = 1; positionOnKey <= lettersPerKey; positionOnKey++) {
				for (int keyNumber = 1; keyNumber <= numberOfKeys; keyNumber++) {
					if (--letterIndex >= 0) {
						numberOfStrokes += (positionOnKey * frequencyTable[letterIndex]);
					}
				}
			}
			System.out.print("Case #" + testCase + ": " + numberOfStrokes + "\n");
		}
		scan.close();
	}	
}
