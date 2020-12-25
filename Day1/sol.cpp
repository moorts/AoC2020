#include <bits/stdc++.h>

typedef long long ll;

int main() {
    freopen("./input", "r", stdin);
    ll x;
    std::vector<ll> nums;
    while(std::cin >> x) {
        nums.push_back(x);
    }
    std::sort(nums.begin(), nums.end());
    for(int i = 0; i < nums.size()-2; i++) {
        ll a = nums[i];
        ll start = i+1;
        ll end = nums.size()-1;
        while(start < end) {
            ll b = nums[start];
            ll c = nums[end];
            if(a+b+c == 2020) {
                std::cout << a * b * c << std::endl;
                break;
            } else if(a+b+c > 2020) {
                end--;   
            } else {
                start++;
            }

        }
    }
    
    return 0;
}

