package friday13;

public class Friday13 {
		
	public static void main(String [] args) {
		Kattio io = new Kattio(System.in, System.out);
		System.setProperty("line.separator", "\n");
		
		int T = io.getInt();
		while (T > 0)  {
			int friday13 = 0;
			int dayOfWeek = 0;
			int D = io.getInt();
			int M = io.getInt();
			for (int month = 0; month < M; ++month) {
				int daysInMonth = io.getInt();
				for (int monthDay = 1; monthDay <= daysInMonth; monthDay++) {
					if (monthDay == 13 && dayOfWeek == 5) {
						friday13++;
					}
					dayOfWeek = ++dayOfWeek % 7;
				}
			}
			io.print("" + friday13 + '\n');
			T--;
		}

		io.close();
	}
}
