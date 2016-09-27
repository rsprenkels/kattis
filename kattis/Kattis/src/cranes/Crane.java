package cranes;

public class Crane {
	public int x;
	public int y;
	public int radius;
		
	public Crane(int x, int y, int radius) {
		this.x = x;
		this.y = y;
		this.radius = radius;
	}
	
	@Override
	public String toString() {
		return "Crane [x=" + x + ", y=" + y + ", radius=" + radius + "]";
	}
	
	
}
