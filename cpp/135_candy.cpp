#include <numeric>

class Solution {
public:
    int candy(vector<int>& ratings) {
        int i;
        vector<int> ret(ratings.size(), 1);
        for(i = 0; i < ratings.size() - 1; ++i)
            if(ratings[i] < ratings[i + 1] && ret[i] >= ret[i + 1])
                ret[i + 1] = ret[i] + 1;
        for(i = ratings.size() - 1; i != -1; --i)
            if(ratings[i] < ratings[i - 1] && ret[i] >= ret[i - 1])
                ret[i - 1] = ret[i] + 1;
        return std::accumulate(ret.begin(), ret.end(), 0);
    }
};