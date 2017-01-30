package org.foobarspam.bowlingGame.Game;

public class Frame {

	private int firstThrow = 0;
	private int secondThrow = 0;
	
	private int frame = firstThrow + secondThrow;
	
	
	/*Constructor*/
	public Frame(int frame){
		this.frame = frame;
	}
	
	/*Metodo getter de frame*/
	public int getScore(){
		return this.frame;
	}
	
	
	public int getFirst(){
		return this.firstThrow;
	}
	public int getSecond(){
		return this.secondThrow;
	}
}
