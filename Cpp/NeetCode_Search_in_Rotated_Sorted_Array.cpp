#include <iostream>
#include <vector>

using namespace std;

int search(vector<int>& nums, int target) {
  int length = nums.size();
  if (length == 1) {
    return (nums[0] == target) ? 0 : -1;
  }

  int min_index = -1;
  int l = 0, r = nums.size() - 1, m = -1;
  int lVal, mVal, rVal;

  // Find minimum index
  while (l + 1 < r) {
    m = (l + r) / 2;
    lVal = nums[l];
    mVal = nums[m];
    rVal = nums[r];
    if (lVal < mVal) {
      l = m;
    }
    if (mVal < rVal) {
      r = m;
    }
  }
  min_index = (nums[0] < nums[length - 1]) ? 0 : r;

  cout << min_index << endl;


  l = 0;
  r = nums.size() - 1;
  while (l < r) {
    int m = (l + r) / 2;
    lVal = nums[(l + min_index) % length];
    mVal = nums[(m + min_index) % length];
    rVal = nums[(r + min_index) % length];
    if (mVal == target) {
      return (m + min_index) % length;
    } else if (mVal < target) {
      l = m + 1;
    } else /* target < mVal */ {
      r = m - 1;
    }
  }

  return (nums[(l + min_index) % length] == target) ? (l + min_index) % length : -1;
}

int main() {
  vector<int> vec = { 1, 3 };
  cout << search(vec, 1) << endl;;
  return 0;
}
