class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (hashmap.get(nums[i]) == null) {
                hashmap.put(nums[i], 1);
            } else {
                hashmap.put(nums[i], hashmap.get(nums[1]) + 1);
            }
        }

        for (Integer i : hashmap.values()) {
            if (i != 1) {
                return true;
            }
        }

        return false;
    }
}