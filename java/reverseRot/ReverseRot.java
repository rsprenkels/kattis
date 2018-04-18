package reverseRot;

public class ReverseRot {
		
	public static void main(String [] args) {
		Kattio io = new Kattio(System.in, System.out);
		System.setProperty("line.separator", "\n");

		String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.";
		
		while (io.hasMoreTokens()) {
			int N = io.getInt();
			if (N==0) break;
			String message = io.getWord();
			
			for (int x = message.length()-1; x >= 0; x--) {
				char c = message.charAt(x);
				io.print(letters.charAt((letters.indexOf(c) + N) % letters.length()));
			}
			io.print('\n');
		}

		io.close();
	}
}
