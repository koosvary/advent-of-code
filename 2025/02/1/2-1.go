package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var invalidValues = 0
var sumOfInvalidValues = 0

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
		input := scanner.Text()

		ranges := strings.Split(input, ",")

		for _, element := range ranges {
			checkRange(element)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Bad values", invalidValues)
	fmt.Println("Total", sumOfInvalidValues)
}

func checkRange(idRange string) {
	values := strings.Split(idRange, "-")

	start, _ := strconv.Atoi(values[0])
	end, _ := strconv.Atoi(values[1])

	for i := start; i <= end; i++ {
		id := strconv.Itoa(i)

		if len(id)%2 != 0 {
			// Odd length strings can't be a double sequence
			continue
		}

		// String is even
		// Check it's broken

		midpoint := len(id) / 2

		left := id[0:midpoint]
		right := id[midpoint:]

		if left == right {
			invalidValues++
			sumOfInvalidValues += i
		}
	}
}
