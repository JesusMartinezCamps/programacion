package foobarspam;

public class Main {

	public static void main(String[] args) {
		/*assertEquals(12, Rectangulo.area);*/
		
		Rectangulo rectangulo = new Rectangulo(4, 3);
		
		if(rectangulo.area() == 12){
			System.out.println("Esta bien");
		}

	}

}
