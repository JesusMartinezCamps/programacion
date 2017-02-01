package test;

import static org.junit.Assert.*;

import org.junit.Test;

import game.ScoreCard;

public class test{
	

//	@Test
//	public void getSimbolValueTest(){
//		
//		String symbols = "-123456789X/";
//		
//		for(int index=0; index<symbols.length(); index++){
//			assertEquals(index , ScoreCard.getSimbolValue(symbols.charAt(index)));			
//		}		
//	}
	@Test
	public void TotalScoreHittingPins(){
		
		// Hitting pins total = 60
		String pins = "12345123451234512345";
		int total = 60;
		
		ScoreCard scoreCard = new ScoreCard(pins);
		
		scoreCard.calculateScore();
		
		assertEquals(total, scoreCard.getTotalScore());			
	}
	
}