class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] answer = new int[temperatures.length];
        Arrays.fill(answer, 0);
        for (int i = 0; i < temperatures.length; i ++){
            
            while(!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]){
                    int idx = stack.pop();
                    answer[idx] = i - idx;
                }
                stack.push(i);
            }
            return answer;

        }
        
    }
