package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type PointTest struct {
	point    string
	dacFound bool
	fftFound bool
}

type CacheValues struct {
	cached     bool
	traversals int
}

var connections = make(map[string][]string)
var cache = make(map[PointTest]CacheValues)

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

	fmt.Println(traverse(PointTest{"svr", false, false}))
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

func traverse(point PointTest) int {
	if cache[point].cached {
		return cache[point].traversals
	}
	traversals := 0

	nextPoints := connections[point.point]

	if point.point == "dac" {
		point.dacFound = true
	}

	if point.point == "fft" {
		point.fftFound = true
	}

	if point.point == "out" {
		if point.dacFound && point.fftFound {
			cache[point] = CacheValues{true, 1}
			return 1
		}
		// Don't get caught out by the default missing key being value 0 - set it
		cache[point] = CacheValues{true, 0}
		return 0
	}

	for _, nextPoint := range nextPoints {
		traversals += traverse(PointTest{nextPoint, point.dacFound, point.fftFound})
	}

	cache[point] = CacheValues{true, traversals}
	return traversals
}
