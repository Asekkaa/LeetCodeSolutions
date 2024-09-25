class Solution:
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        max_frequency_tasks = sum(1 for count in task_counts.values() if count == max_frequency)
        
        return max(len(tasks), (max_frequency - 1) * (n + 1) + max_frequency_tasks)
