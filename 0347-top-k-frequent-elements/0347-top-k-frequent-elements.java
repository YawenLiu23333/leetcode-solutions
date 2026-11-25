class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // isnt this the descending order?? whats syntax for ascending
        PriorityQueue <int[]> pq = new PriorityQueue<>(
            (a,b) -> Integer.compare(a[0], b[0])
        );
        Map<Integer, Integer> map = new HashMap<>();

        for(int n:nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        

        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            int num = entry.getKey();
            int freq = entry.getValue();
                pq.offer(new int[] {freq, num});
                while(pq.size() > k){
                    pq.poll();
                }
            }

        return pq.stream().mapToInt(pair -> pair[1]).toArray();
        
    }
}