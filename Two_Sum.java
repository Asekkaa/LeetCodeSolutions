class Solution {
  public int[] twoSum(int[] nums, int target) {
    // Initialize a hash map that maps each number in the array to its index.
    Map<Integer, Integer> seen = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      // Check if the target minus the current number is in the hash map.
      if (seen.containsKey(target - nums[i])) {
        return new int[] {i, seen.get(target - nums[i])};
      } else {
        // Otherwise, add the current number to the hash map.
        seen.put(nums[i], i);
      }
    }

    // If we reach this point, then there are no two numbers in the array that add up to the target.
    return new int[] {};
  }
}
