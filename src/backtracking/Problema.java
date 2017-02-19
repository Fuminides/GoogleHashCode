package backtracking;

public interface Problema {
	
	/**
	 * Devuelve el valor que da la funcion de costo a este problema.
	 * @return
	 */
	public double evaluar();
	
	/**
	 * Devuelve una copia exacta de este problema. (Copia dura)
	 * @return
	 */
	public Problema clone();
	
	/**
	 * Devuelve un array con los IDs de todas las acciones posibles en el problema.
	 * @return
	 */
	public int[] accionesPosibles();
	
	/**
	 * Ejecuta la accion iesima en el programa.
	 * @param i
	 */
	public void ejecutarAccion(int i);
}
