package bijele;

import java.util.Scanner;

public class Bijele {

	public static void main(String[] args) {
		new Bijele().processInput();
	}

	public void processInput() {
		Scanner scan = new Scanner(System.in);
		int kings = scan.nextInt();
		int queens = scan.nextInt();
		int rooks = scan.nextInt();
		int bishops = scan.nextInt();
		int knights = scan.nextInt();
		int pawns = scan.nextInt();
		
		System.out.print(1 - kings + " ");
		System.out.print(1 - queens + " ");
		System.out.print(2 - rooks + " ");
		System.out.print(2 - bishops + " ");
		System.out.print(2 - knights + " ");
		System.out.print(8 - pawns + "\n");
		scan.close();
	}
}


