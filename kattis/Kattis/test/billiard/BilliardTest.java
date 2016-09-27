package billiard;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class BilliardTest {

	@Test
	public void test() {
		String result = new Billiard(100,100,1,1,1).calculate();
		
		assertEquals("45.00 141.42", result);
		
	}
	
	@Test
	public void testFromFile() throws IOException {
		System.setIn(BilliardTest.class.getResourceAsStream("billiard.in"));
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		Billiard b = new Billiard();
		b.processInput();
		
		String expected = IOUtils.toString(BilliardTest.class.getResourceAsStream("billiard.ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
	}
}
