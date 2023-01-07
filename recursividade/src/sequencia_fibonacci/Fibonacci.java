package sequencia_fibonacci;

public class Fibonacci {
	public static void main(String [] args){
		System.out.println("Fibonacci: "+ sequenciaFibonacci(4));
		System.out.println("Fibonacci: "+ fibonacciRecursivo(7));
	}
	// RETORNA A POSIÇÃO NA SEQUÊNCIA DE FIBONNACI
	// 1 1 2 3 5 8 13 
	public static int fibonacciRecursivo(int x){
		if(x <= 1) {
			return 1;			
		}
		return sequenciaFibonacci(x-1) + sequenciaFibonacci(x-2);
	}
	public static int sequenciaFibonacci(int x){
		if(x <= 1){
			return 1;
		}else{
			int n = 1, prox = 1;
			for (int i = 0; i < x-1; i++) {
				int temp = prox;
				prox = prox + n;
				n = temp;
			}
			return n;
		}
	}
}