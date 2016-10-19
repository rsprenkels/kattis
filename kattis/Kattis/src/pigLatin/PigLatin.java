package pigLatin;

import java.io.BufferedInputStream;
import java.io.PrintStream;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class PigLatin {
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		PrintStream ps = new PrintStream(System.out);

		while (scan.hasNextLine()) {
			String [] words = scan.nextLine().split("\\s");
			for (int index=0; index<words.length; index++) {
				String word = words[index];
				if ("aeiouy".indexOf(word.charAt(0)) != -1) {
					word += "yay";
				} else {
		            Pattern pattern = Pattern.compile("[aeiouy]");  
		            Matcher matcher = pattern.matcher(word);  
		            if(matcher.find()) {
		            	word = word.substring(matcher.start()) + word.substring(0, matcher.start()) + "ay";
		            }  					
				}
				ps.printf("%s%s", index==0 ? "" : " ", word);
			}
			ps.printf("\n");
		}
		ps.flush();
		scan.close();
	}
}