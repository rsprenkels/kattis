package mosquitoMultiplication;

import java.io.BufferedInputStream;
import java.util.Scanner;

public class MosquitoMultiplication {
		
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		
		while (scan.hasNextInt()) {
			int curM = scan.nextInt();
			int curP = scan.nextInt();
			int curL = scan.nextInt();
			int nextM, nextP, nextL;
			int Erate = scan.nextInt();
			int Rrate = scan.nextInt();
			int Srate = scan.nextInt();
			int N = scan.nextInt();
			for (int week = 0; week < N; week++) {
				nextL = curM * Erate;
				nextP = curL / Rrate;
				nextM = curP / Srate;
				curL = nextL;
				curP = nextP;
				curM = nextM;
			}
			System.out.print(curM + "\n");			
		}
		scan.close();
	}
}
