package whatDoesTheFoxSay;

import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class WhatDoesTheFoxSay {
	
	static HashMap<Character, Character> convert;
	static {
		convert = new HashMap<Character, Character>(5);
		convert.put(' ', ' ');
		convert.put('+', '+');
		convert.put('-', '|');
		convert.put('|', '-');
	}
		
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));

		int numberOfTestcases = Integer.parseInt(scan.nextLine());
		while (numberOfTestcases-- > 0) {
			String recordedLine = scan.nextLine();
			List<String> recording = new ArrayList<String>(100);
			for (String sound : recordedLine.split("\\s")) {
				recording.add(sound);
			}
			String soundInformation = scan.nextLine();
			List<String> knownSounds = new ArrayList<String>(100);
			while (!soundInformation.equals("what does the fox say?")) {
				Scanner oneLine = new Scanner(soundInformation);
				oneLine.next();
				oneLine.next();
				knownSounds.add(oneLine.next());
				soundInformation = scan.nextLine();
			}
			recording.removeAll(knownSounds);
			boolean firstSound = true;
			for (String foxSound : recording) {
				if (!firstSound) {
					System.out.print(" ");
				}
				firstSound = false;
				System.out.print(foxSound);
			}
			System.out.print("\n");
			
		}
		scan.close();
	}
	
	public static String trimTrailing(String str) {
	    if (str != null) {
	        for (int i = str.length() - 1; i >= 0; --i) {
	            if (str.charAt(i) != ' ') {
	                return str.substring(0, i + 1);
	            }
	        }
	    }
	    return str;
	}
}
