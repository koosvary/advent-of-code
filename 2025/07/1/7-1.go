package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

var grid = [][]string{}
var splitters = 0

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
	goDown(1, startIndex)

	countSplitters()
	fmt.Println(splitters)
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

func goDown(row int, col int) {
	if row == len(grid) {
		return
	}

	if grid[row][col] == "|" {
		// Already been done
		return
	}

	if grid[row][col] == "^" {
		splitBeam(row, col)
		return
	}

	grid[row][col] = "|"
	goDown((row + 1), col)

}

func splitBeam(row int, col int) {
	// Left
	grid[row][col-1] = "|"
	goDown(row+1, col-1)

	// Right
	grid[row][col+1] = "|"
	goDown(row+1, col+1)
}

func countSplitters() {
	for i := 1; i < len(grid); i++ {
		for index, char := range grid[i] {
			if char == "^" {
				if grid[i-1][index] == "|" {
					// Don't count orphaned splitters
					splitters++
				}
			}
		}
	}
}
