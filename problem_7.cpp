#include <iostream>
#include <vector>
#include <thread>
#include <mutex>

std::mutex m;
std::vector<int> primes{2,3,5,7,11,13};

void isPrime(int value){
    for (int& prime : primes){
        if (value % prime == 0){
            return;
        }
    }
    std::lock_guard mu(m);
    primes.push_back(value);
}

int main(){
    int value{15};
    while(primes.size() != 10001){
        std::thread t(isPrime, value);
        value += 2;
        t.join();
    }

    std::cout << primes[10000] << std::endl;

    return 0;
}
