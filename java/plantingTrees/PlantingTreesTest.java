package plantingTrees;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class PlantingTreesTest {

	
	@Test
	public void testAllSets() throws IOException {
		String [] tests = {"trees.1","trees.2"};
		for (String test : tests) {
			System.err.println("running test " + test);
			test("" + test);
		}
	}	
	
	public void test(String testFile) throws IOException {
		System.setIn(PlantingTrees.class.getResourceAsStream(testFile + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		PlantingTrees.main(null);
		
		String expected = IOUtils.toString(PlantingTrees.class.getResourceAsStream(testFile + ".ans"), "UTF-8"); 
		String result = baos.toString();
		System.err.print(result); 
		assertEquals(expected, result);
	}
}
