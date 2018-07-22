#include <climits>
#include <unordered_map>
#include <utility>
#include <algorithm>

class Solution {
public:
    int min = INT_MAX;
    vector<vector<int>> triangle;
    std::unordered_map<int, int> memo;
    int minimumTotal(vector<vector<int>>& triangle) {
        this->triangle = triangle;
        return this->findMinPath(0,0);
    }
private:
    int findMinPath(int i, int j){
        if(i + 1 == this->triangle.size())
            return this->triangle[i][j];
        if(this->memo.find(cantorPairingHash(i,j)) != this->memo.end())
            return this->memo[cantorPairingHash(i,j)];
        int tmp = INT_MAX;
        for(int k = j; k < j + 2; ++k)
            tmp = std::min(tmp, this->triangle[i][j] + this->findMinPath(i + 1, k));
        this->memo[cantorPairingHash(i,j)] = tmp;
        return tmp;
    }
    float cantorPairingHash(int a, int b){
        return 0.5 * (a + b) * (a + b + 1) + b;
    }
};