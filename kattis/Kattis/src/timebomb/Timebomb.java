package timebomb;

import java.util.Scanner;
import java.util.regex.Pattern;

public class Timebomb {

	public static void main(String[] args) {
		new Timebomb().processInput();
	}

	public void processInput() {
		Scanner scan = new Scanner(System.in);
		String [] lines = new String [5];
				
		while (scan.hasNextLine()) {
			String oneLine = scan.nextLine();
			System.err.println("[" + oneLine + "]");
			int digit = 0;
			while (oneLine.length() >= 3) {
				String chunck = oneLine.substring(0, 3);
				oneLine = oneLine.substring(4);
				System.err.println("chunck["+ chunck + "]");
			}
		}
		
		scan.close();
	}
}


