package cokolada;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class CokoladaTest {

	
	@Test
	public void testAllSets() throws IOException {
		String [] tests = {"cokolada.1","cokolada.2","cokolada.3","cokolada.4","cokolada.5"};
		for (String test : tests) {
			System.err.println("running test " + test);
			test("" + test);
		}
	}	
	
	public void test(String testFile) throws IOException {
		System.setIn(Cokolada.class.getResourceAsStream(testFile + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		Cokolada.main(null);
		
		String expected = IOUtils.toString(Cokolada.class.getResourceAsStream(testFile + ".ans"), "UTF-8"); 
		String result = baos.toString();
		System.err.print(result); 
		assertEquals(expected, result);
	}
}
