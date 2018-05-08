// No. 41

import java.util.ArrayList;

public class FindMissingPositive {
    public int firstMissingPositive(int[] nums) {
        if (nums.length==0)
            return 1;
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0; i<nums.length; i++) {
            list.add(i+1);
        }
        for(int x: nums) {
            System.out.println(list.toString());
            if (x>list.get(list.size()-1))
                continue;
            if (list.contains(x))
                list.remove(Integer.valueOf(x));
        }
        if(list.size()!=0)
            return list.get(0);
        else
            return nums.length+1;
    }

    public static void main(String[] args) {
        //int[] nums = {3,4,-1,1};
        int[] nums = {1,2};
        System.out.println(new FindMissingPositive().firstMissingPositive(nums));
    }
}
