package billiard;

import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Scanner;

public class Billiard {

	int a,b,s,m,n;
	
	public static void main(String[] args) {

		new Billiard().processInput();
	}

	Billiard(int a, int b, int s, int m, int n) {
		this.a = a;
		this.b = b;
		this.s = s;
		this.m = m;
		this.n = n;
	}
	
	public Billiard() {
	}

	void processInput() {
		Scanner scan = new Scanner(System.in);
		
		while (readNumbers(scan))  {
			System.out.print(calculate() + "\n");
		}
	}

	String calculate() {
		double distX = a * m;
		double distY = b * n;
		double distTotal = Math.sqrt(distX*distX + distY*distY); 
		double speed = distTotal / s;
		double angle = Math.toDegrees(Math.asin(distY / distTotal));
		DecimalFormat myFormat = new DecimalFormat("0.00");
		DecimalFormatSymbols newSymbols = new DecimalFormatSymbols();
		newSymbols.setDecimalSeparator('.');
		myFormat.setDecimalFormatSymbols(newSymbols);;
		String resultLine = String.format("%s %s", myFormat.format(angle), myFormat.format(speed));
		return resultLine;
	}
	
	boolean readNumbers(Scanner scan) {
		a = scan.nextInt();
		b = scan.nextInt();
		s = scan.nextInt();
		m = scan.nextInt();
		n = scan.nextInt();
		return a != 0 || b != 0 || s != 0 || m != 0 || n != 0;
	}

}
