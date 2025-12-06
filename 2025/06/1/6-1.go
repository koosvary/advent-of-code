package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

var columns = [][]int{}
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
		readLine(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(total)
}

func readLine(line string) {
	re := regexp.MustCompile("[0-9]+")
	values := re.FindAllString(line, -1)

	if len(columns) == 0 {
		initializeColumns(len(values))
	}

	if len(values) > 0 {
		for idx, value := range values {
			valueInt, _ := strconv.Atoi(value)
			columns[idx] = append(columns[idx], valueInt)
		}
	} else {
		re = regexp.MustCompile("[+*]")
		operations := re.FindAllString(line, -1)

		for idx, op := range operations {
			doMath(idx, op)
		}
	}
}

func initializeColumns(length int) {
	for i := 0; i < length; i++ {
		array := []int{}
		columns = append(columns, array)
	}
}

func doMath(idx int, op string) {
	colTotal := 0

	if op == "*" {
		colTotal = 1
	}

	for _, val := range columns[idx] {
		if op == "+" {
			colTotal += val
		} else {
			colTotal *= val
		}
	}

	total += colTotal
}
