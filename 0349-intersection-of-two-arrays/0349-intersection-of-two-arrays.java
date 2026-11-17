class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet <Integer> check1 = new HashSet<>();
        for(int n:nums1){
            check1.add(n);
        }

        HashSet <Integer> list = new HashSet<>();
        for(int n:nums2){
            if(check1.contains(n)){
                list.add(n);
            }
            
        }

        int[] res = new int[list.size()];
        int i = 0;
        for(Integer val: list){
            res[i++] = val;
        }
        return res;
    }
}