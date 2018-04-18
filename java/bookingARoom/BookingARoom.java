package bookingARoom;

import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class BookingARoom {
	
	public static void main(String[] args) {
		new BookingARoom().processInput();
	}

	void processInput() {
		Scanner scan = new Scanner(System.in);
		int roomsInHotel = scan.nextInt();
		int roomsBooked = scan.nextInt();
		Set<Integer> bookedRooms = new TreeSet<Integer>();
		
		for (int index = 0; index < roomsBooked; index++) {
			bookedRooms.add(scan.nextInt());
		}
		
		boolean foundFreeRoom = false;
		for (int roomNumber = 1; roomNumber <= roomsInHotel; roomNumber++) {
			if (!bookedRooms.contains(roomNumber)) {
				foundFreeRoom = true;
				System.out.print(roomNumber + "\n");
				break;
			}
		}
		if (!foundFreeRoom) {
			System.out.print("too late\n");			
		}
//		System.out.print("Case #" + testCase + ": " + numberOfStrokes + "\n");
		scan.close();
	}	
}
