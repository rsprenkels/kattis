package alienNumbers;

import java.util.Scanner;

public class AlienNumbers {

	public static void main(String[] args) {
		new AlienNumbers().processInput();
	}

	public void processInput() {
		Scanner scan = new Scanner(System.in);
		int numberOfCases;
		
		numberOfCases = scan.nextInt();

		for (int caseNo = 1; caseNo <= numberOfCases; caseNo++) {
			String alienNumber = scan.next();
			String sourceLanguage = scan.next();
			String destLanguage = scan.next();
			long theValue = decode(alienNumber, sourceLanguage);
			System.err.println("theValue " +  theValue);
			String result = encode(theValue, destLanguage);
			
			System.out.print("Case #" + caseNo + ": " + result + "\n");
		}
		scan.close();
	}

	private String encode(long theValue, String destLanguage) {
		int groundNumber = destLanguage.length();
		String partResult = "";
		while (theValue > 0) {
			int lsd = (int) (theValue % groundNumber);
			partResult = destLanguage.charAt(lsd) + partResult;
			theValue = theValue / groundNumber;
		}
		return partResult;
	}

	private long decode(String alienNumber, String sourceLanguage) {
		long partResult = 0;
		int groundNumber = sourceLanguage.length();
		for (int pos = 0; pos < alienNumber.length(); pos++) {
			partResult = partResult * groundNumber + sourceLanguage.indexOf(alienNumber.charAt(pos));
		}
		return partResult;
	}
}


