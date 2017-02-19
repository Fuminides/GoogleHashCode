package backtracking;

public class Backtracking {
	
	/**
	 * Resuelve el problema por backtracking.
	 * 
	 * @param problema
	 * @return
	 */
	public static Problema solve(Problema problema){
		int[] acciones = problema.accionesPosibles();
		double max = Double.MIN_VALUE;
		Problema solucion = null;
		
		for(int accion: acciones){
			Problema candidato = problema.clone();
			candidato.ejecutarAccion(accion);
			
			Problema aux = solve(candidato);
			if ( aux != null){
				candidato = aux;
			}
			
			double value = candidato.evaluar();
			if (value > max){
				max = value;
				solucion = candidato;
			}
		}
		
		return solucion;
	}

}
