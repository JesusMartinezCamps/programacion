package game;

public class ScoreCard {

	private String scoreCard = "";
	private int totalScore = 0;
	//private String simbols = "-123456789X/";
	
	/*Constructor ScoreCard*/
	public ScoreCard(String scoreCard){
		this.scoreCard = scoreCard;
	}
	
	/*Getter Setters*/
	public void setTotalScore(int totalScore){
		this.totalScore += totalScore;
	}
	public int getTotalScore(){
		return this.totalScore;
	}
	public String getScoreCard(){
		return this.scoreCard;
	}

	public void roll(char pin){
		setTotalScore(scorePin(pin)) ;
	}
	private int scorePin(char pin){
		int newScore = 0;
		newScore = Character.getNumericValue(pin);
		return newScore;
		
	}
	
	private void calculateScore(ScoreCard scoreCard){
		for(int i=0; i < getScoreCard().length(); i++){
			char pin = getScoreCard().charAt(i);
			roll(pin);
		}		
	}
}
