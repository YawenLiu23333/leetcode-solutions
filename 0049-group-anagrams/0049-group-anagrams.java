class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Map<Character, Integer>, List<String>> res = new HashMap<>();
        for(String s: strs){
            Map<Character, Integer> map = new HashMap<>();
            for(int i =0; i< s.length(); i ++){
                char c = s.charAt(i);
                map.put(c, map.getOrDefault(c, 0) + 1);
            }
            if(!res.containsKey(map)){
                res.put(map, new ArrayList<>());
            }
            res.get(map).add(s);
        }
        List<List<String>> output = new ArrayList<>(res.values());
        return output;
    }
}