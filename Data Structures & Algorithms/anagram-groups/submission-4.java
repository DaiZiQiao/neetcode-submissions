class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<HashMap<Character, Integer>, ArrayList<String>> hashmap = new HashMap<>();

        for (String s : strs) {
            HashMap<Character, Integer> charHashmap = new HashMap<>();

            for (int i = 0; i < s.length(); i++) {
                Character c = s.charAt(i);

                if (charHashmap.get(c) == null) {
                    charHashmap.put(c, 1);
                } else {
                    charHashmap.put(c, charHashmap.get(c) + 1);
                }
            }

            if (hashmap.get(charHashmap) == null) {
                hashmap.put(charHashmap, new ArrayList<>());
                hashmap.get(charHashmap).add(s);
            } else {
                hashmap.get(charHashmap).add(s);
            }
        }

        List<List<String>> result = new ArrayList<>();
        for (List<String> a : hashmap.values()) {
            result.add(a);
        }

        return result;
    }
}
