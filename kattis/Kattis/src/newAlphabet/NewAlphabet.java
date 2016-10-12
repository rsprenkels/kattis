package newAlphabet;

import java.io.BufferedInputStream;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class NewAlphabet {

	static Map<Character, String> myMap;
	static {
		myMap = new HashMap<Character, String>();
		myMap.put('a', "@");
	    myMap.put('b', "8");
	    myMap.put('c', "(");
	    myMap.put('d', "|)");
	    myMap.put('e', "3");
	    myMap.put('f', "#");
	    myMap.put('g', "6");
	    myMap.put('h', "[-]");
	    myMap.put('i', "|");
	    myMap.put('j', "_|");
	    myMap.put('k', "|<");
	    myMap.put('l', "1");
	    myMap.put('m', "[]\\/[]");
	    myMap.put('n', "[]\\[]");
	    myMap.put('o', "0");
	    myMap.put('p', "|D");
	    myMap.put('q', "(,)");
	    myMap.put('r', "|Z");
	    myMap.put('s', "$");
	    myMap.put('t', "']['");
	    myMap.put('u', "|_|");
	    myMap.put('v', "\\/");
	    myMap.put('w', "\\/\\/");
	    myMap.put('x', "}{");
	    myMap.put('y', "`/");
	    myMap.put('z', "2");
	}
		
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		
		String plaintext = scan.nextLine();
		StringBuffer result = new StringBuffer();
		
		for (char c : plaintext.toCharArray()) {
			if (Character.isAlphabetic(c)) {
				result.append(myMap.get(Character.toLowerCase(c)));
			} else {
				result.append(c);
			}
		}
		
		System.out.print (result + "\n");
		scan.close();
	}
}
