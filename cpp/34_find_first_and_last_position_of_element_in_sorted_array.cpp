class Solution {
    vector<int> nums;
    int target;
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        this->nums = nums;
        this->target = target;
        if(nums.empty())
            return {-1, -1};
        int index = this->binSearch(0, nums.size() - 1);
        if(index == -1)
            return {-1, -1};
        int i, j;
        i = j = index;
        while(-1 < i && nums[i] == target)
            --i;
        while(j < nums.size() && nums[j] == target)
            ++j;
        return {i + 1, j - 1};
    }
private:
    int binSearch(int left, int right){
        if(left > right)
            return -1;
        int mid = left + ((right - left) / 2);
        if(this->nums[mid] == this->target)
            return mid;
        if(this->nums[mid] > this->target)
            return binSearch(left, mid - 1);
        return binSearch(mid + 1, right);
    }
};