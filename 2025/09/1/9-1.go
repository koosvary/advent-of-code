package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

type Coord struct {
	x int
	y int
}

var points = []Coord{}

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

	fmt.Println(getBiggestArea())

}

func readLine(line string) {

	tile := strings.Split(line, ",")

	x, _ := strconv.Atoi(tile[0])
	y, _ := strconv.Atoi(tile[1])

	points = append(points, Coord{x, y})
}

func getBiggestArea() int {
	biggestArea := 0
	for i := 0; i < len(points); i++ {
		left := points[i]
		lx, ly := left.x, left.y
		for j := i + 1; j < len(points); j++ {
			right := points[j]

			rx, ry := right.x, right.y

			xDist := int(math.Abs(float64(lx-rx))) + 1 // Include the first row!
			yDist := int(math.Abs(float64(ly-ry))) + 1

			area := xDist * yDist

			if area > biggestArea {
				biggestArea = area
			}
		}
	}

	return biggestArea
}
