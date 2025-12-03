package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

var total = 0

func main() {
	// open file
	f, err := os.Open("..\\input.txt")
	if err != nil {
		log.Fatal(err)
	}
	// remember to close the file at the end of the program
	defer f.Close()

	// read the file line by line using scanner
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		total += findBestJoltage(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Total", total)
}

func findBestJoltage(input string) int {
	var batteries []int
	for _, char := range input {
		battery, _ := strconv.Atoi(string(char))

		batteries = append(batteries, battery)
	}

	var digits []int

	for i := 0; i < 12; i++ {
		var rightmostIndex = len(batteries) - 11 + i
		var bestCandidate = 0
		var bestCandiateIndex = 0

		var usableBatteries = batteries[:rightmostIndex]

		for index, battery := range usableBatteries {
			if battery > bestCandidate {
				bestCandidate = battery
				bestCandiateIndex = index
			}
		}

		batteries = batteries[bestCandiateIndex+1:]

		digits = append(digits, bestCandidate)
	}

	return combineNumbers(digits)
}

func combineNumbers(numbers []int) int {
	var total = 0

	for _, number := range numbers {
		total = total*10 + number
	}

	return total
}
