package hiddenPassword;

import java.io.BufferedInputStream;

import java.util.Scanner;

public class HiddenPassword {
		
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		
		String password = scan.next();
		String message = scan.next();
		
		int positionInMessage = 0;
		int positionInPassword = 0;
		boolean stillValid = true;
		while (stillValid && positionInMessage < message.length() && positionInPassword < password.length()) {
			while(positionInMessage < message.length() && password.substring(positionInPassword).indexOf(message.charAt(positionInMessage)) == -1) {
				positionInMessage++;
			}
			if (positionInMessage < message.length() && positionInPassword < password.length()) {
				stillValid = positionInPassword < password.length() && message.charAt(positionInMessage) == password.charAt(positionInPassword);
				positionInPassword++;
				positionInMessage++;
			} 
		}
		if (stillValid && positionInPassword == password.length()) {		
			System.out.print ("PASS" + "\n");
		} else {
			System.out.print ("FAIL" + "\n");
		}
		scan.close();
	}
}
