#include <iostream>

bool divisibleTest(int number){
    for (size_t i{1}; i <= 20; ++i){
        if (number % i != 0){
            return false;
        }
    }
    return true;
}

int main(){
    int value{0};

    while (true){
        ++value;
        if (divisibleTest(value)){
            break;
        }
    }

    std::cout << value << std::endl;

    return 0;
}
