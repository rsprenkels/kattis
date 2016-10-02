package timebomb;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class TimebombTest {

	@Test
	public void testAllSets() throws IOException {
		for (int test = 1; test <= 5; test++) {
			System.err.println("running test " + test);
			test("" + test);
		}
	}
	
	public void test(String testNo) throws IOException {
		System.setIn(Timebomb.class.getResourceAsStream("timebomb." + testNo + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		Timebomb testObject= new Timebomb();
		testObject.processInput();
		
		String expected = IOUtils.toString(Timebomb.class.getResourceAsStream("timebomb." + testNo + ".ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
		System.err.print(result);
	}
}
