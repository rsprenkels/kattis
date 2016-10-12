package leftBeehind;

public class LeftBeehind {
		
	public static void main(String [] args) {
		Kattio io = new Kattio(System.in, System.out);
		System.setProperty("line.separator", "\n");
		int sweet = io.getInt();
		int sour = io.getInt();
		while (sweet != 0 || sour != 0) {
			if (sweet + sour == 13) {
				io.print("Never speak again.\n");
			} else {
				if (sweet > sour) {
					io.print("To the convention.\n");					
				} else if (sour > sweet) {
					io.print("Left beehind.\n");					
				} else {
					io.print("Undecided.\n");					
				}
			}
			sweet = io.getInt();
			sour = io.getInt();			
		}
		io.close();
	}
}
