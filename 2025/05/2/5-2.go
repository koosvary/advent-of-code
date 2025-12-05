package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	Start int
	End   int
}

type Overlap struct {
	Overlap    bool
	LowerStart bool
	BiggerEnd  bool
}

var ranges = []Range{}
var allFreshRanges = []Range{}
var freshIngredients = 0

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
		line := scanner.Text()

		if line == "" {
			break
		}

		parseRange(line)
	}

	for _, curr := range ranges {
		findAllFreshRanges(curr)
	}

	mergeRanges()

	findAllPossibleFresh()

	fmt.Println(freshIngredients)
}

func parseRange(idRange string) {
	values := strings.Split(idRange, "-")

	start, _ := strconv.Atoi(values[0])
	end, _ := strconv.Atoi(values[1])

	ranges = append(ranges, Range{start, end})
}

func findAllFreshRanges(curr Range) {
	for idx, testRange := range allFreshRanges {
		changesMade := false
		newRange := Range{testRange.Start, testRange.End}

		if curr.Start == testRange.Start && curr.End == testRange.End {
			// They're the same range
			return
		}

		if curr.Start < testRange.Start && curr.End > testRange.Start {
			newRange.Start = curr.Start
			changesMade = true
		}
		if curr.End > testRange.End && curr.Start < testRange.End {
			newRange.End = curr.End
			changesMade = true
		}

		if changesMade {
			allFreshRanges[idx] = newRange
			break
		}
	}

	// No overlap, is a new range
	allFreshRanges = append(allFreshRanges, curr)
}

func mergeRanges() {
	for currIdx, curr := range allFreshRanges {
		for testIdx, test := range allFreshRanges {
			if testIdx == currIdx {
				continue
			}

			results := testOverlap(curr, test)

			if !results.Overlap {
				continue
			}

			newStart := curr.Start
			newEnd := curr.End
			// We've got new ranges, start again
			if !results.LowerStart {
				newStart = test.Start
			}
			if !results.BiggerEnd {
				newEnd = test.End
			}

			// Delete the curr and test entries, put in the new melded range
			newRange := Range{newStart, newEnd}
			// Delete the higher index first, so we don't jumble the indexes around by accident
			if currIdx < testIdx {
				allFreshRanges = append(allFreshRanges[0:testIdx], allFreshRanges[testIdx+1:]...)
				allFreshRanges = append(allFreshRanges[0:currIdx], allFreshRanges[currIdx+1:]...)
			} else {
				allFreshRanges = append(allFreshRanges[0:currIdx], allFreshRanges[currIdx+1:]...)
				allFreshRanges = append(allFreshRanges[0:testIdx], allFreshRanges[testIdx+1:]...)
			}

			allFreshRanges = append(allFreshRanges, newRange)
			mergeRanges()
			return
		}
	}
}

func testOverlap(curr Range, test Range) Overlap {
	if curr.End < test.Start || curr.Start > test.End {
		return Overlap{false, false, false}
	}

	// overlap, lowerStart, biggerEnd
	return Overlap{true, curr.Start < test.Start, curr.End > test.End}
}

func findAllPossibleFresh() {
	for _, curr := range allFreshRanges {
		diff := curr.End - curr.Start + 1
		freshIngredients += diff
	}
}
