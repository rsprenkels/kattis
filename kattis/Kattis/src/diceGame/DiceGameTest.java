package diceGame;

import static org.junit.Assert.*;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

public class DiceGameTest {

	@Test
	public void testAllSets() throws IOException {
		for (int test = 1; test <= 3; test++) {
			System.err.println("running test " + test);
			test("" + test);
		}
	}
	
	public void test(String testNo) throws IOException {
		System.setIn(DiceGame.class.getResourceAsStream(testNo + ".in"));
	
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setOut(new PrintStream(baos));
		
		DiceGame testObject= new DiceGame();
		testObject.processInput();
		
		String expected = IOUtils.toString(DiceGame.class.getResourceAsStream(testNo + ".ans"), "UTF-8"); 
		String result = baos.toString();
		assertEquals(expected, result);
		System.err.print(result);
	}
}
