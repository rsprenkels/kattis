package busySchedule;

import java.io.BufferedInputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class BusySchedule {
	
	private class Time implements Comparable<Time> {
		int minutes;
		
		public Time(int hours, int minutes, char amPm) {
			System.err.printf("constructing Time %d %d %c ",hours, minutes, amPm);
			if (hours == 12) hours = 0;
			this.minutes = hours*60 + minutes + (amPm == 'A' ? 0 : 12*60);
		}
		
		@Override
		public String toString() {
			int hours = (minutes/60);
			if (hours == 0) hours = 12;
			if (hours > 12) hours -= 12;
			return String.format("%d:%02d %s", hours, minutes%60, minutes < 12*60 ? "a.m." : "p.m.", minutes);
		}

		@Override
		public int compareTo(Time o) {
			return minutes - o.minutes;
		}
	}
	
	public static void main(String [] args) {
		Scanner scan = new Scanner(new BufferedInputStream(System.in));
		PrintStream ps = new PrintStream(System.out);
		BusySchedule bs = new BusySchedule();

		int numOfAppointments = Integer.parseInt(scan.nextLine());
		Pattern pattern = Pattern.compile("(\\d+):(\\d+)\\s+(a.m.|p.m.)");
		while (numOfAppointments > 0) {
			ArrayList<Time> schedule = new ArrayList<Time>();
			for (int appointmentIndex=0; appointmentIndex<numOfAppointments; appointmentIndex++) {
				String nextLine = scan.nextLine();
				System.err.printf("%s ", nextLine);
				Matcher m = pattern.matcher(nextLine);
				if (m.find()) {
					for (int x = 0; x <= 3; x++) { System.err.printf("g:%d[%s] ",x, m.group(x)); }
					Time time = bs.new Time(Integer.parseInt(m.group(1)), Integer.parseInt(m.group(2)), m.group(3).equals("a.m.") ? 'A' : 'P');
					System.err.println(time);
					schedule.add(time);
				}
			}
			Collections.sort(schedule);
			for (Time t : schedule) {
				ps.printf("%s\n", t);
				System.err.printf("%s\n", t);
			}
			// schedule.clear();
			numOfAppointments = Integer.parseInt(scan.nextLine());
			if (numOfAppointments > 0) {
				ps.printf("\n");				
			}
		}
		ps.flush();
		scan.close();
	}
}