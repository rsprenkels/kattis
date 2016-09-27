package textMessaging;

import static org.junit.Assert.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;


public class TextMessagingTest {
	
	@Test
	public void test() throws IOException {
		System.setIn(TextMessagingTest.class.getResourceAsStream("sample.in"));
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		TextMessaging testObject= new TextMessaging();
		testObject.processInput();
		
		String expected = IOUtils.toString(TextMessagingTest.class.getResourceAsStream("sample.ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
	}
}
