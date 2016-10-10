package primes;

import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Primes {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));

		int numberOfPrimes = Integer.parseInt(scan.nextLine());
		int origTestValue;
		
		while (numberOfPrimes > 0) {
			int [] peculiarPrimes = new int[numberOfPrimes];
			for (int primeIndex=0; primeIndex<numberOfPrimes; primeIndex++) {
				peculiarPrimes[primeIndex] = scan.nextInt();
			}
			int minValue = scan.nextInt();
			int maxValue = scan.nextInt();
			scan.nextLine();
			boolean printedAValue = false;
			int tstPrime;
			if (minValue == 1) {
				System.out.print("1");
				printedAValue = true;				
			}
			for (origTestValue = Math.max(2,minValue) - 1; ++origTestValue <= maxValue; ) {
				int testValue = origTestValue;
				int onePrime;
				decompose: while (testValue > 1) {
					for (tstPrime = numberOfPrimes; --tstPrime >= 0; ) {
						onePrime = peculiarPrimes[tstPrime];
						if (testValue % onePrime == 0) {
							testValue /=  onePrime;
							continue decompose;
						}
					}
					break decompose;
				}
				if (testValue == 1) {
					if (printedAValue) {
						System.out.print(",");
					}
					System.out.print(origTestValue);
					printedAValue = true;
				}
			}
			if (!printedAValue) {
				System.out.print("none");
			}
			System.out.print("\n");
			numberOfPrimes = Integer.parseInt(scan.nextLine());
		}
		scan.close();
	}	
}
