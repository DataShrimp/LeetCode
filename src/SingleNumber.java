// No.136
// 1. HashMap
// 2. 数学方法，集合的和与数列的和的差
// 3. Bit亦或操作性质

import java.util.HashMap;
import java.util.Map;

public class SingleNumber {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> num = new HashMap<Integer, Integer>();
        for(int x: nums) {
            num.put(x, num.getOrDefault(x,0)+1);
        }
        int ret = 0;
        for(int x: num.keySet()) {
            if (num.get(x)==1) {
                ret = x;
                break;
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        int[] nums = {1,1,2,3,2};
        System.out.println(new SingleNumber().singleNumber(nums));

    }
}
