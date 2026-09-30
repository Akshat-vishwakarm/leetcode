class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        string common = strs[0];

        for (int i = 1; i < strs.size(); i++) {

            string temp = "";

            int j = 0;

            while (j < common.length() &&
                   j < strs[i].length() &&
                   common[j] == strs[i][j]) {

                temp += common[j];
                j++;
            }

            common = temp;

            if (common == "") {
                return "";
            }
        }

        return common;
    }
};