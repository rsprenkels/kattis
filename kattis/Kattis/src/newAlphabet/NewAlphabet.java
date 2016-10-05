package newAlphabet;

import java.io.BufferedInputStream;
import java.util.Map;
import java.util.Scanner;

import com.google.common.collect.ImmutableMap;

public class NewAlphabet {

	static final Map<Character, String> MY_MAP = ImmutableMap.<Character, String>builder()
		    .put('a', "@")
		    .put('b', "8")
		    .put('c', "(")
		    .put('d', "|)")
		    .put('e', "3")
		    .put('f', "#")
		    .put('g', "6")
		    .put('h', "[-]")
		    .put('i', "|")
		    .put('j', "_|")
		    .put('k', "|<")
		    .put('l', "1")
		    .put('m', "[]\\/[]")
		    .put('n', "[]\\[]")
		    .put('o', "0")
		    .put('p', "|D")
		    .put('q', "(,)")
		    .put('r', "|Z")
		    .put('s', "$")
		    .put('t', "']['")
		    .put('u', "|_|")
		    .put('v', "\\/")
		    .put('w', "\\/\\/")
		    .put('x', "}{")
		    .put('y', "`/")
		    .put('z', "2")
		    .build();
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		
		String plaintext = scan.nextLine();
		StringBuffer result = new StringBuffer();
		
		for (char c : plaintext.toCharArray()) {
			if (Character.isAlphabetic(c)) {
				result.append(MY_MAP.get(Character.toLowerCase(c)));
			} else {
				result.append(c);
			}
		}
		
		System.out.print (result + "\n");
		scan.close();
	}
}
