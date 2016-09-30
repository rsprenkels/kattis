package vauvau;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class VauvauTest {

	@Test
	public void test() throws IOException {
		System.setIn(Vauvau.class.getResourceAsStream("sample.2.in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		Vauvau testObject= new Vauvau();
		testObject.processInput();
		
		String expected = IOUtils.toString(Vauvau.class.getResourceAsStream("sample.2.ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
		System.err.print(result);
	}
}
