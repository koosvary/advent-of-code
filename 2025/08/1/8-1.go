package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Coord struct {
	X int
	Y int
	Z int
}

type Pair struct {
	left  Coord
	right Coord
}

type PointsAndDistances struct {
	points   Pair
	distance float64
}

var junctions = []Coord{}
var circuits = make(map[Coord]int)
var circuitSizes = make(map[int]int)

var distances = make(map[Pair]float64)
var sortedDistances = []PointsAndDistances{}

var totalPairs = 1000
var nextCircuitIndex = 1

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

	getAllDistances()
	sortAllDistances()

	createCircuits()

	getCircuitCounts()
	largestCircuits := findThreeLargestCircuits()
	fmt.Println(largestCircuits[0] * largestCircuits[1] * largestCircuits[2])
}

func readLine(line string) {
	coords := strings.Split(line, ",")
	x, _ := strconv.Atoi(coords[0])
	y, _ := strconv.Atoi(coords[1])
	z, _ := strconv.Atoi(coords[2])
	junctions = append(junctions, Coord{x, y, z})
}

func getAllDistances() {
	for i := 0; i < len(junctions); i++ {
		boxOne := junctions[i]
		for j := i + 1; j < len(junctions); j++ {
			boxTwo := junctions[j]

			setEuclideanDistance(boxOne, boxTwo)
		}
	}
}

func setEuclideanDistance(left, right Coord) {
	x := math.Pow(float64(left.X-right.X), 2)
	y := math.Pow(float64(left.Y-right.Y), 2)
	z := math.Pow(float64(left.Z-right.Z), 2)

	distances[Pair{left, right}] = math.Sqrt(x + y + z)
}

func sortAllDistances() {
	// Add them to an array, then sort the array from lowest to highest distance
	for key, val := range distances {
		sortedDistances = append(sortedDistances, PointsAndDistances{key, val})
	}

	sort.Slice(sortedDistances, func(i, j int) bool {
		return sortedDistances[i].distance < sortedDistances[j].distance
	})
}

func getCircuitCounts() {
	for _, val := range circuits {
		circuitSizes[val] = circuitSizes[val] + 1
	}
}

func createCircuits() {
	pairsFound := 0
	index := 0
	for pairsFound < totalPairs {
		pair := sortedDistances[index].points
		left := pair.left
		right := pair.right
		index++
		pairsFound++

		// Check that it's not 0 - 0 means they're not in a circuit yet
		// so skip if they're both 0
		if circuits[left] != 0 && circuits[left] == circuits[right] {
			continue
		}

		addToCircuit(left, right)
	}
}

func addToCircuit(left, right Coord) {
	// Check if either are in a circuit (circuit map result > 0)
	// If both, make first boxes circuit merge with the second
	// If neither were in a circuit add a new one
	if circuits[left] > 0 && circuits[right] == 0 {
		// Add right to left
		circuits[right] = circuits[left]
	} else if circuits[left] == 0 && circuits[right] > 0 {
		// Add left to right
		circuits[left] = circuits[right]
	} else if circuits[left] > 0 && circuits[right] > 0 {
		mergeCircuits(circuits[right], circuits[left])
	} else {
		// New circuit
		circuits[left] = nextCircuitIndex
		circuits[right] = nextCircuitIndex
		nextCircuitIndex++
	}
}

func mergeCircuits(fromCircuit, toCircuit int) {
	for key, val := range circuits {
		if val == fromCircuit {
			circuits[key] = toCircuit
		}
	}
}

func findThreeLargestCircuits() []int {
	// Create an array to store the three largest values
	largest := []int{-math.MaxInt, -math.MaxInt, -math.MaxInt}

	// Loop through the map
	for _, value := range circuitSizes {
		// If the value is larger than the smallest of the three largest, replace it
		if value > largest[0] {
			largest[2] = largest[1]
			largest[1] = largest[0]
			largest[0] = value
		} else if value > largest[1] {
			largest[2] = largest[1]
			largest[1] = value
		} else if value > largest[2] {
			largest[2] = value
		}
	}

	return largest
}
