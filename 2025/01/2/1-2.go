package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
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

	var newDialPoint = 0

	if dir == "L" {
		newDialPoint = (dialPoint - clicks)
		if newDialPoint < 0 {
			var timesPassed = math.Abs(float64(newDialPoint / 100))

			if dialPoint != 0 {
				// Make sure not to add an extra instance of passing 0 when starting there
				// i.e. an L1 move from 0 to -99 shouldn't trigger a passing of 0
				timesPassed++
			}
			password += int(timesPassed)
		} else if newDialPoint == 0 {
			password++
		}

		newDialPoint = newDialPoint % 100

		if newDialPoint < 0 {
			newDialPoint += 100 // Why does Go do negative mods wrong?
		}

	} else {
		newDialPoint = (dialPoint + clicks)

		if newDialPoint > 99 {
			var timesPassed = math.Abs(float64(newDialPoint / 100))
			password += int(timesPassed)
		}

		newDialPoint = newDialPoint % 100
	}

	dialPoint = newDialPoint
}
