#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    // 각 자리를 분류
    while (n/10 != 0){
        answer.push_back(n%10);
        n = n/10;
    }
    answer.push_back(n);
    return answer;
}
