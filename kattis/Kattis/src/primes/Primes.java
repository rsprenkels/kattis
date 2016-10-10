package primes;

import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Primes {

	private class Sieve {
		byte [] store;
		int offset;
		int maxValue;
		
		Sieve (int offset, int maxValue) {
			int capacity = maxValue - offset;
			store = new byte [(capacity + 8) / 8];
			Arrays.fill(store, (byte) 0xFF);
			this.offset = offset;
			this.maxValue = maxValue;
		}
		
		void clearBit(int bitIndex) {
			if (bitIndex >= offset && bitIndex <= maxValue) {
				store[((bitIndex - offset) / 8)] &= ~(1 << ((bitIndex - offset) % 8));
			}
		}
		
		boolean isSet(int bitIndex) {
			return (store[((bitIndex - offset) / 8)] & (1 << ((bitIndex - offset) % 8))) != 0;
		}
	}
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));

		int numberOfPrimes = Integer.parseInt(scan.nextLine());
		
		while (numberOfPrimes > 0) {
			int [] peculiarPrimes = new int[numberOfPrimes];
			for (int primeIndex=0; primeIndex<numberOfPrimes; primeIndex++) {	
				peculiarPrimes[primeIndex] = scan.nextInt();
			}
			int minValue = scan.nextInt();
			int maxValue = scan.nextInt();
			scan.nextLine();
			boolean printedAValue = false;

			Sieve sieve = new Primes().new Sieve(minValue, maxValue);
			int longestProduct = Math.max(1,(int) Math.ceil(Math.log10(maxValue) / Math.log10(peculiarPrimes[0])));
			for (int prodLen = 1; prodLen <= longestProduct; prodLen++) {
				sieveProducts(prodLen, 1, sieve, peculiarPrimes);
			}
			
			if (minValue == 1) {
				System.out.print("1");
				printedAValue = true;
			}
			for (int valIndex = Math.max(2,minValue); valIndex <= maxValue; valIndex++) {
				if (!sieve.isSet(valIndex)) {
					if (printedAValue) {
						System.out.print("," + valIndex);
					} else {
						System.out.print(valIndex);
						printedAValue = true;
					}
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

	private static void sieveProducts(int prodLen, int partialProduct, Sieve sieve, int[] peculiarPrimes) {
		if (prodLen == 1) {
			for (int p = 0; p < peculiarPrimes.length; p++) {
				long sieveThisValue = partialProduct * peculiarPrimes[p];
				if (sieveThisValue > sieve.maxValue) { break; }
				// System.out.printf("sieving value %d\n", sieveThisValue);
				sieve.clearBit((int) sieveThisValue);
			}
		} else {
			for (int p = 0; p < peculiarPrimes.length; p++) {
				long nextPartial = partialProduct * peculiarPrimes[p];
				if (nextPartial <= sieve.maxValue) {
					sieveProducts(prodLen-1, (int) nextPartial, sieve, peculiarPrimes);
				}
			}
		}
		
	}	
}

