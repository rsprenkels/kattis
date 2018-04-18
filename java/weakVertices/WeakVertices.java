package weakVertices;

import java.io.BufferedInputStream;

import java.util.Scanner;

public class WeakVertices {
		
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		
		int n = scan.nextInt();
		while (n > 0) {
			int [][] matrix = new int [n][n];
			boolean [] weakVertices = new boolean [n];
			
			for (int row = 0; row < n; row++) {
				weakVertices[row] = true;
				for (int col = 0; col < n; col++) {
					matrix[row][col] = scan.nextInt();
				}
			}
			
			for (int col = 0; col < n; col++) {
				for (int row = 0; row < n; row++) {
					if (matrix[row][col] == 1) {
						for (int row2 = row + 1; row2 < n; row2++) {
							if (matrix[row2][col] == 1) {
								// System.err.print(col + " zit aan " + row + " en " + row2 + " ");
								if (matrix[row][row2] == 1) {
									// System.err.println(row + " zit ook aan " + row2);
									weakVertices[col] = false;
								} else {
									// System.err.println(row + " zit NIET aan " + row2);								
								}
							}
						}
					}
				}
			}
			
			boolean printedOne = false;
			for (int vertice = 0; vertice < n; vertice++) {
				if (weakVertices[vertice]) {
					if (printedOne) {
						System.out.print(" ");
					}
					System.out.print("" + vertice);
					printedOne = true;
				}
			}		
			System.out.print("\n");
			n = scan.nextInt();
		}
		scan.close();
	}
}
