package bookingARoom;

import static org.junit.Assert.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;


public class BookingARoomTest {
	
	@Test
	public void test() throws IOException {
		System.setIn(BookingARoomTest.class.getResourceAsStream("1.in"));
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		BookingARoom testObject= new BookingARoom();
		testObject.processInput();
		
		String expected = IOUtils.toString(BookingARoomTest.class.getResourceAsStream("1.ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
	}
}
