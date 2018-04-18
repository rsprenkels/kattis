package cokolada;

import java.io.BufferedInputStream;
import java.util.Scanner;

public class Cokolada {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		int K = Integer.parseInt(scan.nextLine());
		int smallestBar=0, numberOfBreaks=0;
		int mostSignificantBit = 0;
		
		for (int bit = 31; bit >=0; bit--) {
			if (((1<<bit) & K) != 0) {
				if (((1<<bit) & K) == K) {
					mostSignificantBit = bit;
				} else {
					mostSignificantBit = bit+1;					
				}
				smallestBar = (1<<mostSignificantBit); 
				break;
			}
		}
		for (int bit = 0; bit <=31; bit++) {
			if (((1<<bit) & K) != 0) {
				numberOfBreaks = mostSignificantBit - bit;
				break;
			}
		}
		
		System.out.printf("%d %d\n", smallestBar, numberOfBreaks);
		scan.close();
	}
}