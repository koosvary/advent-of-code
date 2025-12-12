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

type GridDimensionsAndPresents struct {
	grid     string
	presents []int
}

var shapes = [][]string{}
var newShape = []string{}
var testCases = []GridDimensionsAndPresents{}

var totalGoodGrids = 0

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
		startNewShape := readLine(scanner.Text())
		if startNewShape {
			shapes = append(shapes, newShape)
			newShape = []string{}
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	rudimentarySpaceFillingTest()
	fmt.Println(totalGoodGrids)
}

func readLine(line string) bool {
	if line == "" {
		return true
	}

	re := regexp.MustCompile(`\dx\d`)
	match := re.FindAllString(line, -1)
	if len(match) > 0 {
		// It's the test cases
		getProblemSet(line)
		return false
	}

	re = regexp.MustCompile(`\d:`)
	match = re.FindAllString(line, -1)

	if len(match) > 0 {
		return false // It's a throwaway line
	}

	// Part of the actual shape/present
	newShape = append(newShape, line)
	return false
}

func getProblemSet(line string) {
	split := strings.Split(line, ": ")
	dimensions := split[0]
	presentStrings := strings.Split(split[1], " ")

	presents := []int{}
	for _, presentString := range presentStrings {
		count, _ := strconv.Atoi(presentString)
		presents = append(presents, count)
	}

	testCases = append(testCases, GridDimensionsAndPresents{dimensions, presents})
}

// Find all the areas that can just fit the shapes without any packing (ie just next to each other)
// We can skip these later on when doing the packing algorithm since they already work
func rudimentarySpaceFillingTest() {
	gridsLeftToTest := []GridDimensionsAndPresents{}
	for _, testCase := range testCases {
		dimensions, presents := testCase.grid, testCase.presents

		split := strings.Split(dimensions, "x")
		width, _ := strconv.Atoi(split[0])
		height, _ := strconv.Atoi(split[1])

		totalPresents := 0
		for _, count := range presents {
			totalPresents += count
		}

		// All presents in the input are 3x3 in their space usage (not necessarily fully filling this space)
		// If we can prove the total number of shapes fill the space (i.e can all fit in the width/3 and height/3 dropping remainder)
		// Then we're chill and this one is good
		maxPresentsInRow := width / 3
		maxPresentsInCol := height / 3

		maxPossiblePresents := maxPresentsInRow * maxPresentsInCol

		if totalPresents <= maxPossiblePresents {
			// This grid is good and fits every present without packing
			totalGoodGrids++
			continue
		}

		gridsLeftToTest = append(gridsLeftToTest, testCase)
	}

	testCases = gridsLeftToTest
}
