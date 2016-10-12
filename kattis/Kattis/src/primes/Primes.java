package primes;

import java.io.BufferedInputStream;
import java.util.Arrays;
import java.util.Scanner;

public class Primes {

	private class Sieve {
		byte [] store;
		private long offset;
		private long maxValue;
		
		Sieve (long offset, long maxNumberOfBits) {
			long capacity = maxNumberOfBits - offset;
			store = new byte [(int) (capacity / 8)+1];
			Arrays.fill(store, (byte) 0x00);
			this.offset = offset;
			this.maxValue = maxNumberOfBits;
		}
		
		void set(int bitIndex) {
			if (bitIndex >= offset && bitIndex < maxValue) {
				store[(int)((bitIndex - offset) / 8)] |= (1 << ((bitIndex - offset) % 8));
			}
		}
		
		boolean get(int bitIndex) {
			return (store[(int)((bitIndex - offset) / 8)] & (1 << ((bitIndex - offset) % 8))) != 0;
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

//			BitSet sieve = new BitSet(maxValue);
//			sieve.clear();
			Sieve sieve = new Primes().new Sieve(minValue, maxValue + 1);
			int longestProduct = Math.max(1,(int) Math.ceil(Math.log10(maxValue) / Math.log10(peculiarPrimes[0])));
			for (int prodLen = 1; prodLen <= longestProduct; prodLen++) {
				sieveProducts(prodLen, 1, sieve, peculiarPrimes, maxValue);
			}
			
			if (minValue == 1) {
				System.out.print("1");
				printedAValue = true;
			}
			for (int valIndex = Math.max(2,minValue); valIndex <= maxValue; valIndex++) {
				if (sieve.get(valIndex)) {
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

	private static void sieveProducts(int prodLen, long partialProduct, Sieve sieve, int[] peculiarPrimes, int maxValue) {
		if (prodLen == 1) {
			for (int p = 0; p < peculiarPrimes.length; p++) {
				long sieveThisValue = partialProduct * peculiarPrimes[p];
				if (sieveThisValue > maxValue) { break; }
				// System.out.printf("sieving value %d\n", sieveThisValue);
				sieve.set((int) sieveThisValue);
			}
		} else {
			for (int p = 0; p < peculiarPrimes.length; p++) {
				long nextPartial = partialProduct * peculiarPrimes[p];
				if (nextPartial <= maxValue) {
					sieveProducts(prodLen-1, nextPartial, sieve, peculiarPrimes, maxValue);
				}
			}
		}
		
	}	
}