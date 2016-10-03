package grandpaBernie;

public class Country implements Comparable<Object> {
	String name;
	int year;

	public Country(String name, int year) {
		this.name = name;
		this.year = year;
	}

	@Override
	public String toString() {
		return "Country [name=" + name + ", year=" + year + "]";
	}

	@Override
	public int compareTo(Object arg0) {
		return  name.compareTo(((Country) arg0).name);
	}
	
	@Override
    public boolean equals(Object o)
    {
        return ((Country)o).name.equals(this.name);
    }
}
