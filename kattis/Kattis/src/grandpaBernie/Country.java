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
		Country otherCountry = (Country) arg0;
		return  name.compareTo(otherCountry.name);
	}
	
	@Override
    public boolean equals(Object o)
    {
        if(o instanceof Country && ((Country)o).name.equals(this.name))
            return true;
        else
            return false;   
    }
}
