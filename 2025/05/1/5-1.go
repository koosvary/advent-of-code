package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	Start int
	End   int
}

var ranges = []Range{}
var freshIngredients = 0

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
		line := scanner.Text()

		if line == "" {
			break
		}

		parseRange(line)
	}

	for scanner.Scan() {
		checkValue(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(freshIngredients)
}

func parseRange(idRange string) {
	values := strings.Split(idRange, "-")

	start, _ := strconv.Atoi(values[0])
	end, _ := strconv.Atoi(values[1])

	ranges = append(ranges, Range{start, end})
}

func checkValue(idToTest string) {
	id, _ := strconv.Atoi(idToTest)

	for _, testRange := range ranges {
		if id < testRange.Start {
			continue
		}

		if id > testRange.End {
			continue
		}

		freshIngredients++
		return
	}
}
