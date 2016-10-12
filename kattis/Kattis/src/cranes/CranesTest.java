package cranes;

import static org.junit.Assert.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;


import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class CranesTest {
	
	@Test
	public void test() throws IOException {
		System.setIn(Cranes.class.getResourceAsStream("A.in"));
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		Cranes testObject = new Cranes();
		testObject.processInput();
		
		String expected = IOUtils.toString(Cranes.class.getResourceAsStream("A.ans"), "UTF-8"); 
		String result = baos.toString();
		System.err.println(result);
		assertEquals(expected, result);
	}
}
