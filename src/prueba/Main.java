package prueba;

import java.io.File;
import java.util.Scanner;

import backtracking.Backtracking;

public class Main {

	
	public static void main(String[] args) throws Exception{
		Pizza pizza = leerFichero(args[0]);
		
		System.out.println(Backtracking.solve(pizza));
	}
	
	public static Pizza leerFichero(String ruta) throws Exception{
		Scanner fichero = new Scanner(new File(ruta));
		int rows = fichero.nextInt(), cols = fichero.nextInt(), min = fichero.nextInt(),
				max = fichero.nextInt();
		Celda[][] celdas = new Celda[rows][cols];
		fichero.nextLine();
		
		for(int i = 0; i < rows; i++){
			for(int z = 0; z < rows; z++){
				Celda celda = new Celda(fichero.next());
				celdas[i][z] = celda;
			}
			fichero.nextLine();
		}
		
		Pizza pizza = new Pizza(celdas, min, max);
		fichero.close();
		
		return pizza;
	}
}
