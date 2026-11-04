class Solution {
    public int[] twoSum(int[] nums, int target) {
        // first one is a difference, second one is its pos
        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i< nums.length; i++) {
            int diff = target - nums[i];

            if (hashmap.get(diff) == null) {
                hashmap.put(nums[i], i);
            } else {
                int[] returnArray = {hashmap.get(diff), i};
                return returnArray;
            }
        }
        return new int[0];
    }
}
