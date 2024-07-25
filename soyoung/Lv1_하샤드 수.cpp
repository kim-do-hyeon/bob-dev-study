#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    int sum = 0;
    int origin = x;
    while (x / 10 != 0){
        sum = sum + x %10;
        x = x/10;
    }
    sum = sum + x;
    // x를 x의 각 자리수의 합으로 나눴을 때, 나누어 떨어지면 하샤드 수 
    return (origin%sum) == 0;

}
