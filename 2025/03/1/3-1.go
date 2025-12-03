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

	var firstDigit = 0
	var firstDigitIndex = 0
	var secondDigit = 0

	for index, battery := range batteries {
		if index == len(batteries)-1 {
			break
		}

		if battery > firstDigit {
			firstDigit = battery
			firstDigitIndex = index
		}
	}

	batteries = batteries[firstDigitIndex+1:]

	for _, battery := range batteries {
		if battery > secondDigit {
			secondDigit = battery
		}
	}

	return firstDigit*10 + secondDigit
}
