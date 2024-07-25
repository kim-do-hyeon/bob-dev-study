#include <iostream>
using namespace std;
int solution(int n)
{
    int answer = 0;
    # 10으로 나눈 나머지를 계속해서 더해나가며 확인. 
    while(n>=10){
        answer = answer + n % 10;
        n = n / 10;
    }
    return answer + n;
        
}
