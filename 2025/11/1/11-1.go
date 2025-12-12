package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var connections = make(map[string][]string)

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

	fmt.Println(traverse("you"))
}

func readLine(line string) {
	split := strings.Split(line, ": ")
	startPoint := split[0]

	nextPoints := []string{}

	for _, point := range strings.Split(split[1], " ") {
		nextPoints = append(nextPoints, point)
	}

	connections[startPoint] = nextPoints
}

func traverse(startPoint string) int {
	traversals := 0

	nextPoints := connections[startPoint]

	for _, point := range nextPoints {
		if point == "out" {
			return 1
		}

		traversals += traverse(point)
	}

	return traversals
}
