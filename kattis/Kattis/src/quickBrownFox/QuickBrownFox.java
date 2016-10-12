package quickBrownFox;

import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.Scanner;

public class QuickBrownFox {
		
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		
		int noOfTestcases = Integer.parseInt(scan.nextLine());
		ArrayList<Character> pangram = new ArrayList<Character>();
		
		for (int testCase = 0; testCase < noOfTestcases; testCase++) {
			String line = scan.nextLine().toLowerCase();
			pangram.clear();
			for (int letter = 0; letter < 26; letter++) {
				pangram.add((char) (letter + 'a'));
			}
			for (int pos = 0; pos < line.length(); pos++) {
				pangram.remove((Character) line.charAt(pos));
			}
			if (pangram.size() == 0) {
				System.out.print("pangram\n");							
			}  else {
				System.out.print("missing ");
				for (Character c : pangram) {
					System.out.print(c);
				}
				System.out.print("\n");							
			}
		}
		scan.close();
	}
}
