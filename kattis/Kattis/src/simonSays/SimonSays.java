package simonSays;

import java.util.Scanner;

public class SimonSays {

	static String prefix = "Simon says ";
	
	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);		
		int aantal = s.nextInt();
		s.nextLine();
		
		for (int i = 1; i <= aantal; i++) {
			String nextLine = s.nextLine();
			if(nextLine.startsWith(prefix)) {
				String result = nextLine.substring(prefix.length());
				System.out.println(result);				
			}
		}
		s.close();
	}
}
