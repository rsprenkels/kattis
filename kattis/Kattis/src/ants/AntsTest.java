package ants;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

import bookingARoom.BookingARoom;

public class AntsTest {

	@Test
	public void test() throws IOException {
		System.setIn(Ants.class.getResourceAsStream("ants.in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		Ants testObject= new Ants();
		testObject.processInput();
		
		String expected = IOUtils.toString(Ants.class.getResourceAsStream("ants.ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
	}
}
