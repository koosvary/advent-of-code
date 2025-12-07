package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type SplitterCoords struct {
	row int
	col int
}

var grid = [][]string{}

// Memoized map of each timeline made after any splitter - assuming they're not orphaned
var timelinesFromNode = make(map[SplitterCoords]int)

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

	startIndex := findStart()
	total := goDown(1, startIndex)

	fmt.Println(total)
}

func readLine(line string) {
	lineArray := []string{}
	for _, char := range line {
		lineArray = append(lineArray, string(char))
	}

	grid = append(grid, lineArray)
}

func findStart() int {
	line := grid[0]

	for index, char := range line {
		if char == "S" {
			return index
		}
	}

	return -1
}

func goDown(row int, col int) int {
	if row == len(grid) {
		return 1
	}

	if grid[row][col] == "^" {
		return splitBeam(row, col)
	}

	if grid[row][col] == "." {
		// No current timeline has hit here
		// Start a fresh one
		grid[row][col] = "|"
	}

	return goDown((row + 1), col)

}

// For each subsequent splitter along a beam's path,
// it would have the same amount of possible timelines after.
// Store how many beams/timelines get made from the last splitter
// of a beam and bubble it up all the way to the root
func splitBeam(row int, col int) int {
	if (timelinesFromNode[SplitterCoords{row, col}] > 0) {
		return timelinesFromNode[SplitterCoords{row, col}]
	}

	total := 0

	// Left
	grid[row][col-1] = "|"
	total += goDown(row+1, col-1)

	// Right
	grid[row][col+1] = "|"
	total += goDown(row+1, col+1)

	timelinesFromNode[SplitterCoords{row, col}] = total

	return total
}
