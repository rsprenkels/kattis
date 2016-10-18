package t9;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class T9Test {

	
	@Test
	public void testAllSets() throws IOException {
		String [] tests = {"1"};
		for (String test : tests) {
			System.err.println("running test " + test);
			test("" + test);
		}
	}	
	
	public void test(String testFile) throws IOException {
		System.setIn(T9.class.getResourceAsStream(testFile + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		T9.main(null);
		
		String expected = IOUtils.toString(T9.class.getResourceAsStream(testFile + ".ans"), "UTF-8"); 
		String result = baos.toString();
		System.err.print(result); 
		assertEquals(expected, result);
	}
}
