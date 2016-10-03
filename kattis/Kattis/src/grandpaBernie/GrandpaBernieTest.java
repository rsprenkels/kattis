package grandpaBernie;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class GrandpaBernieTest {

	@Test
	public void testAllSets() throws IOException {
		for (int test = 1; test <= 2; test++) {
			System.err.println("running test " + test);
			test("" + test);
		}
	}
	
	public void test(String testFile) throws IOException {
		System.setIn(GrandpaBernie.class.getResourceAsStream(testFile + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		GrandpaBernie testObject= new GrandpaBernie();
		testObject.processInput();
		
		String expected = IOUtils.toString(GrandpaBernie.class.getResourceAsStream(testFile + ".ans"), "UTF-8"); 
		String result = baos.toString();
		System.err.print(result); 
		assertEquals(expected, result);
	}
}
