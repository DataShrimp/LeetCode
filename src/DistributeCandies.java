// No. 562

import java.util.HashMap;
import java.util.Map;

public class DistributeCandies {

    public int distributeCandies(int[] candies) {
        // HashSet is a better solution
        Map<Integer, Integer> bucket = new HashMap<>();

        for(int x: candies) {
            bucket.put(x, bucket.getOrDefault(x, 0)+1);
        }
        int m = candies.length/2;
        if (m < bucket.size()) {
            return m;
        }
        return bucket.size();
    }

    public static void main(String[] args) {
        int[] candies = {1,1,2,2,3,3,4,5};
        System.out.println(new DistributeCandies().distributeCandies(candies));
    }
}
