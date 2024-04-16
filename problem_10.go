package main

import (
	"fmt"
	"sync"
)

var mutex sync.Mutex
var wg sync.WaitGroup

var primes[]int
var sum int = 2 + 3 + 5 + 7

func isPrime(value int){
	for _, prime := range(primes){
		if value % prime == 0{
			wg.Done()
			return;
		}
	}

	mutex.Lock()
	primes = append(primes, value);
	sum += value;
	mutex.Unlock()
	wg.Done()
}

func main(){
	primes = append(primes, 2)
	primes = append(primes, 3)
	primes = append(primes, 5)
	primes = append(primes, 7)

	for i:= 11; i < 2000000; i += 2 {
		wg.Add(1)
		go isPrime(i);
	}
	wg.Wait()

	fmt.Println(sum)
}
