package wordCloud;

public class Word {
	String word;
	int count;
	
	Word(String word, int count) {
		this.word = word;
		this.count = count;
	}
	
	public String getWord() {
		return word;
	}

	public int getCount() {
		return count;
	}	
}
