class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        //hashmap key:n, val:frequency
        HashMap <Integer, Integer> map = new HashMap<>();
        
        for(int n:nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        //priorityqueue: frequency, n
        PriorityQueue <int[]> pq = new PriorityQueue<>(
                (a, b) -> Integer.compare(a[0],b[0])
        );

        for(Map.Entry <Integer, Integer> entry : map.entrySet()){
            int freq = entry.getValue();
            int n = entry.getKey();
            pq.offer(new int[] {-freq, n});
        }

        //res array size of k
         int[] res = new int [k];
        for(int i =0; i < k; i ++){
            int[] pair = pq.poll();
            res[i] = pair[1];
        }
        return res;

    }
}