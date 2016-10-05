package newAlphabet;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class NewAlphabetTest {

	@Test
	public void testAllSets() throws IOException {
		String [] tests = {"base","frequency","new"};
		for (String test : tests) {
			System.err.println("running test " + test);
			test("" + test);
		}
	}
	
	public void test(String testFile) throws IOException {
		System.setIn(NewAlphabet.class.getResourceAsStream(testFile + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		NewAlphabet.main(null);
		
		String expected = IOUtils.toString(NewAlphabet.class.getResourceAsStream(testFile + ".ans"), "UTF-8"); 
		String result = baos.toString();
		System.err.print(result); 
		assertEquals(expected, result);
	}
}
