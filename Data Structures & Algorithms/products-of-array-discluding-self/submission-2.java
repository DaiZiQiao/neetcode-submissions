class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];

        prefix[0] = 1;
        for (int i = 0; i < prefix.length - 1; i++) {
            prefix[i + 1] = nums[i] * prefix[i];
        }

        int[] suffix = new int[nums.length];

        suffix[nums.length - 1] = 1;
        for (int i = suffix.length - 1; i > 0; i--) {
            suffix[i - 1] = nums[i] * suffix[i];
        }

        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = prefix[i] * suffix[i];
        }

        return result;
    }
}  
