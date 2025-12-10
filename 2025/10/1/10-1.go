package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"reflect"
	"regexp"
	"strconv"
	"strings"
)

var totalPresses = 0

var idealState = []bool{}
var buttons = []string{}

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

	fmt.Println(totalPresses)
}

func readLine(line string) {
	// Make the ideal state
	re := regexp.MustCompile(`\[(.*?)\]`)
	stateLine := re.FindStringSubmatch(line)[1] // The group, not the whole match

	idealState = []bool{}
	for _, char := range stateLine {
		if string(char) == "." {
			idealState = append(idealState, false)
		} else {
			idealState = append(idealState, true)
		}
	}

	// Create the buttons
	re = regexp.MustCompile(`\((.*?)\)`)
	matches := re.FindAllStringSubmatch(line, -1)

	buttons = []string{}
	for _, match := range matches {
		buttons = append(buttons, match[1])
	}

	// Run the simulation for this line
	pressButtons()
}

// Button should only ever be pressed once, as press twice is effectively negating the first press
func pressButtons() {
	fewestPresses := math.MaxInt

	// Use the binary value of 2^(# of buttons) to figure out the best combo
	possibleCombinations := int(math.Pow(2.0, float64(len(buttons))))

	for i := 0; i < possibleCombinations; i++ {
		currentState := []bool{}

		// initialise array of lights that are off
		for range idealState {
			currentState = append(currentState, false)
		}

		// After all the padding, will produce a binary string
		// i.e. 00000010101 - the 0's to the left are the padding
		binary := strconv.FormatInt(int64(i), 2)
		padLength := len(buttons)
		paddedBinary := fmt.Sprintf("%0*s", padLength, binary)

		presses := 0
		// Press each button
		for index, flag := range paddedBinary {
			if string(flag) == "1" {
				// press the button
				presses++

				indexesToFlip := strings.Split(buttons[index], ",")
				for _, val := range indexesToFlip {
					stateToChange, _ := strconv.Atoi(val)
					currentState[stateToChange] = !currentState[stateToChange]
				}
			}
		}

		if reflect.DeepEqual(currentState, idealState) && presses < fewestPresses {
			fewestPresses = presses
		}
	}

	totalPresses += fewestPresses
}
