package grandpaBernie;

import java.io.BufferedInputStream;
import java.util.*;

/**
 * https://open.kattis.com/problems/grandpabernie
 * 
 * credits for this implementation go to maxim-kornienko
 * on my local system, this one takes just as much time as my attempts.
 * wonder if it runs fast enough on the server
 * 
 * it did, by a factor of at least two.
 * Need to look into as why my version is WAAAY slower
 * 
 */
public class GrandpaBernie {

    private Map<String, List<Integer>> memories;
    private Set<String> sorted;

    public GrandpaBernie(int capacity) {
        this.memories = new HashMap<>(capacity);
        this.sorted = new HashSet<>(capacity);
    }

    public void addMemory(String country, Integer year) {
        List<Integer> years = memories.get(country);
        if (years == null) {
            years = new ArrayList<>();
            memories.put(country, years);
        }
        years.add(year);
    }

    public Integer getYear(String country, int order) {
        List<Integer> years = memories.get(country);
        if (!sorted.contains(country)) {
            Collections.sort(years);
            memories.put(country, years);
            sorted.add(country);
        }
        return years.get(order - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(new BufferedInputStream(System.in));
        int n = Integer.parseInt(sc.next());
        GrandpaBernie gb = new GrandpaBernie(n);
        for (int i = 0; i < n; i++) {
            gb.addMemory(sc.next(), sc.nextInt());
        }
        int q = Integer.parseInt(sc.next());
        for (int i = 0; i < q; i++) {
            System.out.print(gb.getYear(sc.next(), sc.nextInt()));
            System.out.print("\n");
        }
        sc.close();
    }
}
