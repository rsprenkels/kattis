package alienNumbers;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class AlienNumbersTest {

	@Test
	public void testAllSets() throws IOException {
		test("sample");
	}
	
	public void test(String testNo) throws IOException {
		System.setIn(AlienNumbers.class.getResourceAsStream(testNo + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		AlienNumbers testObject= new AlienNumbers();
		testObject.processInput();
		
		String expected = IOUtils.toString(AlienNumbers.class.getResourceAsStream(testNo + ".ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
		System.err.print(result);
	}
}
