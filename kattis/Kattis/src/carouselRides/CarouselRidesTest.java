package carouselRides;

import static org.junit.Assert.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;


public class CarouselRidesTest {
	
	@Test
	public void test() throws IOException {
		System.setIn(CarouselRidesTest.class.getResourceAsStream("test0.in"));
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		CarouselRides rides = new CarouselRides();
		rides.processInput();
		
		String expected = IOUtils.toString(CarouselRidesTest.class.getResourceAsStream("test0.ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
	}

}
