package main

import (
	"fmt"
	"sync"
)

var NUMBER = 600851475143
var number = 600851475143 / 1000

var mutex sync.Mutex
var wg sync.WaitGroup

var primes []int

func main(){
	primes = append(primes, 11)

	for number % 2 == 0{
		number /= 2
		fmt.Println(number)
	}
	for number % 3 == 0{
		number /= 3
		fmt.Println(number)
	}
	for number % 5 == 0{
		number /= 5
		fmt.Println(number)
	}
	for number % 7 == 0{
		number /= 7
		fmt.Println(number)
	}

	for num:=13; num <= number; num+=2{
		wg.Add(1)
		go prime(num)
	}
	wg.Wait()

	number = NUMBER
	var value = 0
	for _, prime := range(primes){
		if number % prime == 0{
			value = prime
		}
	}
	fmt.Println(value)
}

func prime(n int){
	for _, prime := range(primes) {
		if n % prime == 0{
			wg.Done()
			return
		}
	}
	mutex.Lock()
	primes = append(primes, n)
	mutex.Unlock()
	wg.Done()
	fmt.Println(n)
}
