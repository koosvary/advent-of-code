package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

var dialPoint = 50
var password = 0

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

	fmt.Println(password)
}

func readLine(dialMove string) {
	var dir = dialMove[0:1]

	var clicks, _ = strconv.Atoi(dialMove[1:])

	if dir == "L" {
		dialPoint = (dialPoint - clicks) % 100
	} else {
		dialPoint = (dialPoint + clicks) % 100
	}

	if dialPoint == 0 {
		password++
	}
}
