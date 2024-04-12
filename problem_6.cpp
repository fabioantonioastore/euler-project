#include <iostream>
#include <vector>

int square(int& number){
    return number * number;
}

int sumNormal(std::vector<int> numbers){
    int sum{0};
    for (int& value : numbers){
        sum += square(value);
    }

    return sum;
}

int sumAdvanced(std::vector<int> numbers){
    int sum{0};
    for (int& value : numbers){
        sum += value;
    }
    sum = square(sum);

    return sum;
}

int main(){
    std::vector<int> numbers;

    for (int i{1}; i <=100; ++i){
        numbers.push_back(i);
    }

    int sumN{sumNormal(numbers)};
    int sumA{sumAdvanced(numbers)};

    std::cout << sumA - sumN << std::endl;

    return 0;
}
