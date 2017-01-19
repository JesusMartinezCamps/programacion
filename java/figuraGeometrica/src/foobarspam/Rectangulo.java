package foobarspam;

public class Rectangulo extends FiguraGeometrica {
	
	
	private double altura = 4;
	private double anchura = 3;
	/*Constructor sin parametros*/
	public Rectangulo(){
		super(); /*se invoca al constructor de la clase superior*/
	}
	
	/*Constructor con los dos paramtros*/
	public Rectangulo(double altura, double anchura){
		super();
		this.altura = altura;
		this.anchura = anchura;
	}
	
	/*Constructor con los dos parametros más el string de nombre*/
	public Rectangulo(String nombre, double altura, double anchura){
		super(nombre);
		this.altura = altura;
		this.anchura = anchura;
	}
	
	public double getAltura(){
		return this.altura;
	}	
	public void setAltura(double altura){
		this.altura = altura; 
	}
	
	public double getAnchura(){
		return this.anchura;
	}
	public void setAnchura(double anchura){
		this.anchura = anchura;
	}
	
	
	@Override
	public double area() {
		return getAltura() * getAnchura();
	}
}
