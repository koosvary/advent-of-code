package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var lines = []string{}
var chunks = [][]string{}
var chunkNumbers = [][]int{}
var operations = []string{}

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
		// do something with a line
		lines = append(lines, scanner.Text())
	}

	re := regexp.MustCompile("[+*]")
	operations = re.FindAllString(lines[len(lines)-1], -1)

	createChunks()

	for idx := range chunks {
		findAllNumbersInChunk(idx)
		doMath(idx)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(total)
}

func createChunks() {
	// Find the second operation symbol,
	// break off previous chunk based on
	// +* char index - 2 (because of the space before)

	for {
		operationsLine := lines[len(lines)-1][1:] //skip the first character

		re := regexp.MustCompile("[+*]")

		opIndexArr := re.FindIndex([]byte(operationsLine))

		if opIndexArr == nil {
			break
		}

		opIndex := opIndexArr[0] + 1

		chunk := []string{}
		for i, line := range lines {
			// cut the left, also skipping the space in between the chunks (hence the -1)
			chunkLine := line[:opIndex-1]

			if i != len(lines)-1 {
				chunk = append(chunk, chunkLine)
			}

			lines[i] = line[opIndex:]
		}

		chunks = append(chunks, chunk)
	}

	// Save the last chunk
	chunk := []string{}
	for i, line := range lines {
		if i != len(lines)-1 {
			chunk = append(chunk, line)
		}
	}
	chunks = append(chunks, chunk)

}

func findAllNumbersInChunk(idx int) {
	chunk := chunks[idx]

	totalNumbers := len(chunk[0])

	numbers := []int{}

	for i := 0; i < totalNumbers; i++ {
		numberString := ""

		for _, chunkLine := range chunk {
			character := chunkLine[i]
			numberString += string(character)
		}

		number, _ := strconv.Atoi(strings.ReplaceAll(numberString, " ", ""))
		numbers = append(numbers, number)
	}

	chunkNumbers = append(chunkNumbers, numbers)
}

func doMath(idx int) {
	op := operations[idx]

	colTotal := 0

	if op == "*" {
		colTotal = 1
	}

	numbers := chunkNumbers[idx]

	for _, val := range numbers {
		if op == "+" {
			colTotal += val
		} else {
			colTotal *= val
		}
	}

	total += colTotal
}
