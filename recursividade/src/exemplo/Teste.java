package exemplo;

public class Teste {
	public static void main(String[] agrs) {
		int valor = 5;
		System.out.print("Fibonacci dos "+valor+" primeiros numeros: ");
		for(int i=0; i<valor; i++) {
			System.out.print(Calculadora.fibonacci(i)+" ");			
		}
	}
}
