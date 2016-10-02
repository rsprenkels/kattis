package diceGame;

import java.util.Scanner;

public class DiceGame {

	public static void main(String[] args) {
		new DiceGame().processInput();
	}

	public void processInput() {
		Scanner scan = new Scanner(System.in);
		int expectedResultGunnar;
		int expectedResultEmma;
		
		expectedResultGunnar = scan.nextInt() + scan.nextInt() + scan.nextInt() + scan.nextInt();
		expectedResultEmma = scan.nextInt() + scan.nextInt() + scan.nextInt() + scan.nextInt();
		scan.close();
		
		if (expectedResultEmma > expectedResultGunnar) {
			System.out.print("Emma\n");
		} else if (expectedResultEmma < expectedResultGunnar) {
			System.out.print("Gunnar\n");
		} else{
			System.out.print("Tie\n");			
		}
	}
}


