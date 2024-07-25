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
    return (origin%sum) == 0;

}