package towering;

import java.util.ArrayList;
import java.util.Collections;

public class Towering {
		
	public static void main(String [] args) {
		Kattio io = new Kattio(System.in, System.out);
		
		ArrayList<Integer> blocks = new ArrayList<Integer>();
		int big = 0;
		int small = 100;
		for (int b = 0; b<6; b++) {
			int oneBlock = io.getInt(); 
			blocks.add(oneBlock);
			big = Math.max(big, oneBlock);
			small = Math.min(small, oneBlock);
		}
		Collections.sort(blocks, Collections.reverseOrder());
		int h1 = io.getInt();
		int b1=0, b2=0;
		outer: for (int outer = 0; outer < blocks.size()-2; outer++) {
			for (int middle = outer+1; middle < blocks.size()-1; middle++) {
				for (int inner = middle+1; inner < blocks.size(); inner++) {
					if (blocks.get(outer) + blocks.get(middle) + blocks.get(inner) == h1) {
						big = blocks.get(outer);
						b1 = blocks.get(middle);
						b2 = blocks.get(inner);
						blocks.remove((Integer) big);
						blocks.remove((Integer) b1);
						blocks.remove((Integer) b2);
						break outer;
					}
				}
			}
		}
		System.out.printf("%d %d %d %d %d %d\n", big, b1, b2, blocks.get(0), blocks.get(1), blocks.get(2));							
		io.close();
	}
}
