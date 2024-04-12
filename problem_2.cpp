#include <iostream>

int fib(int n1=0, int n2=1, int max=4000000, int sum=0){
    if(n1 + n2 > max){
        return sum;
    }
    if((n1 + n2) % 2 == 0){
        sum += n1 + n2;
    }
    return fib(n1 + n2, n1, max, sum);
}

int main(){
    std::cout << fib() << std::endl;

    return 0;
}
