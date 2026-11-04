class Solution {

    public String encode(List<String> strs) {
        String result = "";

        for (int i = 0; i < strs.size(); i++) {
            String current = strs.get(i);

            result += current.length() + "#";
            for (int j = 0; j < current.length(); j++) {
                result += current.charAt(j); 
            }
        }

        return result;
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();

        int pos = 0;
        for (pos = 0; pos < str.length(); pos++) {
            String numStrs = "";
            while (true) {
                if (str.charAt(pos) == '#') {
                    pos++;
                    break;
                }
                numStrs += str.charAt(pos);
                pos++;
            }

            int numS = Integer.parseInt(numStrs);

            String current = "";
            for (int i = 0; i < numS; i++) {
                current += str.charAt(pos);
                pos++;
            }

            result.add(current);
            pos--;
        }
        return result;
    }
}
