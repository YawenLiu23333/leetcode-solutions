class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];

        //calc prefix
        int prefix = 1;
        for(int i = 0; i < res.length; i ++){
            res[i] = prefix;
            prefix *= nums[i];
        }

        //calc postfix
        int postfix = 1;
        for(int i = res.length - 1; i >= 0; i --){
            res[i] *= postfix;
            postfix *= nums[i];
        }

        return res;
    }
}