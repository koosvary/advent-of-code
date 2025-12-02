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

		maxPatternLength := len(id) / 2

		for j := 1; j <= maxPatternLength; j++ {
			possiblePattern := id[0:j]

			// Get the times a pattern repeats in the ID
			// If the length of the pattern * the repeat count == length of the ID, we're good
			repeatedOccurrences := strings.Count(id, possiblePattern)
			if repeatedOccurrences*len(possiblePattern) == len(id) {
				invalidValues++
				sumOfInvalidValues += i
				break
			}
		}
	}
}
