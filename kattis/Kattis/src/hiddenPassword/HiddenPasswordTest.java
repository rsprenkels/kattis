package hiddenPassword;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class HiddenPasswordTest {

	@Test
	public void testAllSets() throws IOException {
		for (int test = 1; test <= 5; test++) {
			System.err.println("running test " + test);
			test("" + test);
		}
	}
	
	public void test(String testFile) throws IOException {
		System.setIn(HiddenPassword.class.getResourceAsStream(testFile + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		HiddenPassword.main(null);
		
		String expected = IOUtils.toString(HiddenPassword.class.getResourceAsStream(testFile + ".ans"), "UTF-8"); 
		String result = baos.toString();
		System.err.print(result); 
		assertEquals(expected, result);
	}
}
