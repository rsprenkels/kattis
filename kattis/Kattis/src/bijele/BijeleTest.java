package bijele;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class BijeleTest {

	@Test
	public void test() throws IOException {
		System.setIn(Bijele.class.getResourceAsStream("1.in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		Bijele testObject= new Bijele();
		testObject.processInput();
		
		String expected = IOUtils.toString(Bijele.class.getResourceAsStream("1.ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
	}
}
