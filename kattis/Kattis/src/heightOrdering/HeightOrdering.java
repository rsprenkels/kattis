package heightOrdering;

import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.BitSet;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class HeightOrdering {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		final int numOfKids = 20;
		int numberOfDatasets = Integer.parseInt(scan.nextLine());
		
		for (int dataSet = 1; dataSet <= numberOfDatasets; dataSet++) {
			int [] heights = new int[numOfKids];
			int dataSetId = scan.nextInt();
			for (int kid = 0; kid < numOfKids; kid++) {
				heights[kid] = scan.nextInt();
			}
			int swaps = 0;
			for (int outer = numOfKids-1; outer >= 0; outer--) {
				for(int inner = 0; inner < outer; inner++) {
					if (heights[inner+1] < heights[inner]) {
						int tmpHeight = heights[inner];
						heights[inner] = heights[inner+1];
						heights[inner+1] = tmpHeight;
						swaps++;
					}
				}
			}
			System.out.printf("%d %d\n", dataSetId, swaps);
		}
		scan.close();
	}
}