package timebomb;


public class StarChar {
	private String [] chunck;
	static StarChar definedChars[];

	static {
		definedChars = new StarChar[10];
		String [] digit0 = {"***", "* *", "* *", "* *", "***"};
		definedChars[0] = new StarChar(digit0);
		String [] digit1 = {"  *", "  *", "  *", "  *", "  *"};
		definedChars[1] = new StarChar(digit1);
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
		for (int charNo = 0; charNo < 2; charNo++) {
			boolean foundDiff = false;
			int line = -1;
			while (!foundDiff && ++line < 5) {
				foundDiff = chunck[line].equals(definedChars[charNo].chunck[line]);
			}
			if (!foundDiff) {
				return true;
			}
		}
		return false;
	}
	
	void setChunck (int line, String chunck) {
		this.chunck[line] = chunck;
	}
}
