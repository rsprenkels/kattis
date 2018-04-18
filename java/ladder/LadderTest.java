package ladder;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class LadderTest {

	@Test
	public void testAllSets() throws IOException {
		for (int test = 0; test <= 1; test++) {
			System.err.println("running test " + test);
			test("ladder.0" + test);
		}
	}
	
	public void test(String testFile) throws IOException {
		System.setIn(Ladder.class.getResourceAsStream(testFile + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		Ladder.main(null);
		
		String expected = IOUtils.toString(Ladder.class.getResourceAsStream(testFile + ".ans"), "UTF-8"); 
		String result = baos.toString();
		System.err.print(result); 
		assertEquals(expected, result);
	}
}
