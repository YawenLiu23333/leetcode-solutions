class Solution {
    public int longestConsecutive(int[] nums) {
        // o(n) time, o(1) auxiliary space;

        HashSet <Integer> check = new HashSet<>();
        for(int n:nums){
            check.add(n);
        }

        int res = 0;
        for(int n:check){
            //update length while n + long in set
            int len = 1;
            while(!check.contains(n -1) && check.contains(len + n)){
                len += 1;
            }
            res = Math.max(res, len);
        }
        return res;
    }
}