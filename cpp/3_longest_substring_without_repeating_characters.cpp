#include <unordered_map>
#include <algorithm> 

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_map<char, int> memo;
        int i, cnt, longest;
        i = cnt = longest = 0;
        while(i < s.length()){
            if(memo.find(s[i]) == memo.end()){
                memo[s[i]] = i;
                cnt++;
            }
            else{
                i = memo[s[i]];
                memo.clear();
                longest = std::max(longest, cnt);
                cnt = 0;
            }
        i++;
        }
        return std::max(longest, cnt);
    }
};