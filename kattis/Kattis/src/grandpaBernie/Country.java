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
		int nameDiff = name.compareTo(otherCountry.name);
		return nameDiff != 0 ? nameDiff : year - otherCountry.year;
	}
}
