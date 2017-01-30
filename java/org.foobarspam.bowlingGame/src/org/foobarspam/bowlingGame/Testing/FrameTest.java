package org.foobarspam.bowlingGame.Testing;

import static org.junit.Assert.*;

import java.util.ArrayList;

import org.foobarspam.bowlingGame.Game.*;

import org.junit.Test;

public class FrameTest {


	@Test
	public void test_frame() {
		/*Test que comprueba un Frame (una tirada), sumando su puntuacion*/
		Frame first = new Frame(3);
		Frame second = new Frame(6);
		assertEquals("Test que suma una tirada simple", 9, first.getScore());
		
	}
}
