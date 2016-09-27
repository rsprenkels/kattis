package wordCloud;

// https://open.kattis.com/problems/wordcloud

import java.util.Scanner;

public class WordCloud {

	int w,n;
	
	public static void main(String[] args) {
		new WordCloud().processInput();
	}

	void processInput() {
		Scanner scan = new Scanner(System.in);
		int cloudNumber = 1;
		
		while (readNumbers(scan))  {
			Word[] words = new Word[n];
			int maxCount = 0;
			for (int lineNumber = 0; lineNumber < n; lineNumber++ ) {	
				String word = scan.next("[\\p{Alpha}']+");
				int count = scan.nextInt();
				words[lineNumber] = new Word(word, count);
				if (count > maxCount) { maxCount = count; }
			}
			int lineWidth = 0;
			int lineHeight = 0;
			int cloudHeight = 0;
			boolean firstWord = true;
			for (int wordNumber = 0; wordNumber < n; wordNumber++ ) {
				Word word = words[wordNumber];
				int wordPointsize = 8 + (int) Math.ceil((40.0 * (word.getCount() - 4.0)) / (maxCount - 4.0));
				int wordLength =  (int) Math.ceil((9.0 / 16.0) * word.word.length() * wordPointsize);
				System.err.println ("word: " + word.word + " length: " + wordLength + " pointsize: " + wordPointsize);
				if (lineWidth == 0) {
					lineWidth = wordLength;
					lineHeight = wordPointsize;
				} else {
					if (lineWidth + wordLength + 10 > w) {
						System.err.println ("new line " + lineHeight + " cloudheigt " + cloudHeight);
						cloudHeight += lineHeight;
						lineWidth = wordLength;
						lineHeight = wordPointsize;
					} else {
						lineWidth += (10 + wordLength);
						lineHeight = Math.max(lineHeight, wordPointsize);
					}
				}
			}
			cloudHeight += lineHeight;
			System.out.print("CLOUD " + cloudNumber + ": "+ cloudHeight + "\n");
			cloudNumber++;
		}
	}
	
	boolean readNumbers(Scanner scan) {
		w = scan.nextInt();
		n = scan.nextInt();
		scan.nextLine();
		return w != 0 || n != 0;
	}
}
