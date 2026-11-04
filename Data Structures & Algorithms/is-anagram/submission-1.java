class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);

            if (hashmap.get(c) == null) {
                hashmap.put(c, 1);
            } else {
                hashmap.put(c, hashmap.get(c) + 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            Character c = t.charAt(i);

            Integer count = hashmap.get(c);
            if (count == null) {
                return false;
            } else if (count == 1) {
                hashmap.remove(c);
            } else {
                hashmap.put(c, count - 1);
            }
        }

        if (hashmap.isEmpty()) {
            return true;
        }

        return false;
    }
}
