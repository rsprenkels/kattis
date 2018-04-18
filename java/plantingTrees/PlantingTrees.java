package plantingTrees;

import java.io.BufferedInputStream;
import java.util.Arrays;
import java.util.Scanner;

public class PlantingTrees {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		int numOfTrees = Integer.parseInt(scan.nextLine());
		int [] trees = new int [numOfTrees];
		
		for (int treeNum=0; treeNum < numOfTrees; treeNum++) {
			trees[treeNum] = scan.nextInt();
		}
		Arrays.sort(trees);
		int partyTime = 0;
		for (int treeNum = trees.length-1; treeNum >= 0; treeNum--) {
			partyTime = Math.max(partyTime, trees[treeNum] + (trees.length - treeNum + 1));
		}
		System.out.printf("%d\n", partyTime);
		scan.close();
	}
}