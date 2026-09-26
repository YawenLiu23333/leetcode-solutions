class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                ind, temp = stack.pop()
                answer[ind] = i - ind
            stack.append((i, t))
        return answer 
