package main

import (
	"bufio"
	"fmt"
	"os"
)

var grid = [][]string{}
var totalGood = 0
var width = 0
var height = 0

func main() {
	// open file
	f, _ := os.Open("..\\input.txt")

	// remember to close the file at the end of the program
	defer f.Close()

	// read the file line by line using scanner
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		// do something with a line
		makeGridRow(scanner.Text())
	}

	width = len(grid[0])
	height = width

	for i := 0; i < width; i++ {
		for j := 0; j < height; j++ {
			if checkCell(i, j) {
				totalGood++
			}
		}
	}

	fmt.Println("Total", totalGood)
}

func makeGridRow(row string) {
	cells := []string{}
	for _, cell := range row {
		cells = append(cells, string(cell))
	}

	grid = append(grid, cells)
}

func checkCell(x int, y int) bool {
	badNeighbours := 0

	if grid[x][y] == "." {
		return false
	}

	for i := -1; i <= 1; i++ {
		neighbourX := x + i

		for j := -1; j <= 1; j++ {
			neighbourY := y + j

			if outOfBounds(neighbourX, neighbourY) {
				continue
			}

			if y == neighbourY && x == neighbourX {
				continue
			}

			if grid[neighbourX][neighbourY] == "@" {
				badNeighbours++
			}

			if badNeighbours > 3 {
				return false
			}
		}
	}

	return true
}

func outOfBounds(x int, y int) bool {
	if x < 0 || x >= width {
		return true
	}

	if y < 0 || y >= height {
		return true
	}

	return false
}
