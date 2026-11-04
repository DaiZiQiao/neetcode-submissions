class Solution {
    public int removeDuplicates(int[] nums) {
        // keep count of duplicates
        int k = 1;

        // iterate through all elements starting from position 1
        int pos = 1;
        for (int i = 1; i < nums.length; i++) {
            // if the element at position 1 is the same as at position 0, shift left
            if (nums[pos] == nums[pos - 1]) {
                System.arraycopy(nums, pos, nums, pos - 1, nums.length - pos);
            } else {
                pos++;
                k++;
            }
        }

        return k;
    }
}