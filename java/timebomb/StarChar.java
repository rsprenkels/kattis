package timebomb;


public class StarChar {
	private String [] chunck;
	static StarChar definedChars[];
	int charValue = -1;

	static {
		definedChars = new StarChar[10];
		String [] digit0 = {
				"***",
				"* *",
				"* *",
				"* *",
				"***"};
		definedChars[0] = new StarChar(digit0);

		String [] digit1 = {
				"  *",
				"  *",
				"  *",
				"  *",
				"  *"};
		definedChars[1] = new StarChar(digit1);

		String [] digit2 = {
				"***",
				"  *",
				"***",
				"*  ",
				"***"};
		definedChars[2] = new StarChar(digit2);

		String [] digit3 = {
				"***",
				"  *",
				"***",
				"  *",
				"***"};
		definedChars[3] = new StarChar(digit3);
	
		String [] digit4 = {
				"* *",
				"* *",
				"***",
				"  *",
				"  *"};
		definedChars[4] = new StarChar(digit4);
	
		String [] digit5 = {
				"***",
				"*  ",
				"***",
				"  *",
				"***"};
		definedChars[5] = new StarChar(digit5);
	
		String [] digit6 = {
				"***",
				"*  ",
				"***",
				"* *",
				"***"};
		definedChars[6] = new StarChar(digit6);
	
		String [] digit7 = {
				"***",
				"  *",
				"  *",
				"  *",
				"  *"};
		definedChars[7] = new StarChar(digit7);
	
		String [] digit8 = {
				"***",
				"* *",
				"***",
				"* *",
				"***"};
		definedChars[8] = new StarChar(digit8);
	
		String [] digit9 = {
				"***",
				"* *",
				"***",
				"  *",
				"***"};
		definedChars[9] = new StarChar(digit9);
	}
	
	StarChar() {
		chunck = new String [5];		
	}

	StarChar(String [] chuncks) {
		this();
		for(int x = 0; x < 5; x++) {
			this.chunck[x] = chuncks[x];
		}
	}
	
	boolean isValidDigit() {
		for (int charNo = 0; charNo <= 9; charNo++) {
			boolean foundDiff = false;
			int line = -1;
			while (!foundDiff && ++line < 5) {
				String left = chunck[line];
				String right = definedChars[charNo].chunck[line];
				foundDiff = !(left.equals(right));
			}
			if (!foundDiff) {
				charValue = charNo;
				return true;
			}
		}
		return false;
	}

	public String toString() {
		String res = "\n";
		for(int line = 0; line < 5; line++) {
			res += chunck[line] + "\n";
		}		
		return res;
	}
	
	void setChunck (int line, String chunck) {
		this.chunck[line] = chunck;
	}
}
