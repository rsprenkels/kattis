package wordCloud;

import static org.junit.Assert.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;


public class WordCloudTest {
	
	@Test
	public void test() throws IOException {
		System.setIn(WordCloudTest.class.getResourceAsStream("cloud.in"));
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		WordCloud b = new WordCloud();
		b.processInput();
		
		String expected = IOUtils.toString(WordCloudTest.class.getResourceAsStream("cloud.ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
	}
}
