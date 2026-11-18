class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue <Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int res = 0;

        for(int n:nums){
            pq.offer(n);
        }

        while( k > 0){
            res = pq.poll();
            k --; 
        }

        return res;

    }
}