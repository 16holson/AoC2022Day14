sandCount = 0

def readFile():
    file = open("InputData.txt", "r")
    return file


def drawRocks(cave, rocks):
    for i in range(len(rocks)):
        if(i+1 < len(rocks)):
            first = list(map(int, rocks[i].split(",")))
            second = list(map(int, rocks[i+1].split(",")))
            # Line of rocks on y axis
            if(first[0] == second[0]):
                # Up line
                if(first[1] > second[1]):
                    for y in range((first[1] - second[1])+1):
                        cave[second[1]+y][first[0]] = 1
                # Down line
                else:
                    for y in range((second[1] - first[1])+1):
                        cave[first[1]+y][first[0]] = 1
            # Line of rocks on x axis
            else:
                # Left line
                if (first[0] > second[0]):
                    for x in range((first[0] - second[0])+1):
                        cave[first[1]][second[0]+x] = 1
                # Right line
                else:
                    for x in range((second[0] - first[0])+1):
                        cave[first[1]][first[0]+x] = 1


def simSand(cave, start):
    global sandCount
    currPosition = start
    while(True):
        # Check if next position is out of bounds
        if(currPosition[0]+1 > len(cave[0]) < currPosition[0]+1 or currPosition[1]+1 > len(cave)-1):
            return False
        # Check below current position
        elif(cave[currPosition[1]+1][currPosition[0]] == 0):
            currPosition[1] = currPosition[1] + 1
            continue
        # Check left and down one
        elif(cave[currPosition[1] + 1][currPosition[0] - 1] == 0):
            currPosition[0] = currPosition[0] - 1
            currPosition[1] = currPosition[1] + 1
            continue
        # Check right and down one
        elif (cave[currPosition[1] + 1][currPosition[0] + 1] == 0):
            currPosition[0] = currPosition[0] + 1
            currPosition[1] = currPosition[1] + 1
            continue
        else:

            cave[currPosition[1]][currPosition[0]] = 9
            sandCount += 1
            return True




def main():
    file = readFile()
    cave = [[0 for i in range(1000)] for j in range(200)]
    for line in file:
        rocks = line.strip().split(" -> ")
        if(len(rocks) > 0):
            drawRocks(cave, rocks)
    while(True):
        if(not simSand(cave, [500, 0])):
            break
    # for i in range(len(cave)):
    #    print(cave[i])
    print(f"Total sand: {sandCount}")
    file.close()


if (__name__ == "__main__"):
    main()