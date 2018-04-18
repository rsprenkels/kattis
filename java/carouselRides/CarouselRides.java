package carouselRides;

import java.util.Scanner;

public class CarouselRides {

	int firstInt, secondInt;
	
	public static void main(String[] args) {
		new CarouselRides().processInput();
	}

	void processInput() {
		Scanner scan = new Scanner(System.in);
		
		while (readNumbers(scan))  {
			int bestNumberOfTickets = 0;
			int bestTotalAmount = 0;
			double bestTicketPrice = 0.0;
			for (int line = 0; line < firstInt; line++) {
				int numberOfTickets = scan.nextInt();
				int totalAmount = scan.nextInt();
				if (numberOfTickets <= secondInt) {
					double ticketPrice = (double) totalAmount / (double) numberOfTickets  ;
					if (bestTotalAmount == 0 ||
						Double.compare(ticketPrice, bestTicketPrice) < 0 || 
						Double.compare(ticketPrice, bestTicketPrice) == 0 && numberOfTickets > bestNumberOfTickets)
					{
						bestTicketPrice = ticketPrice;
						bestNumberOfTickets = numberOfTickets;
						bestTotalAmount = totalAmount;							
					}
				}
			}
			if (bestNumberOfTickets == 0) {
				System.out.print("No suitable tickets offered\n");
			} else {
				System.out.print("Buy " + bestNumberOfTickets + " tickets for $" + bestTotalAmount + "\n");
			}
		}
	}
	
	boolean readNumbers(Scanner scan) {
		firstInt = scan.nextInt();
		secondInt = scan.nextInt();
		scan.nextLine();
		return firstInt != 0 || secondInt != 0;
	}
}
