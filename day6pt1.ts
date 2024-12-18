let input = await Deno.readTextFile('./day6input.txt')

// input = `....#.....
// .........#
// ..........
// ..#.......
// .......#..
// ..........
// .#..^.....
// ........#.
// #.........
// ......#...`

const parsedInput = input.split(/\n/)
// console.log(parsedInput)

const dirs = {
  up: [ -1, 0 ],
  down: [ 1, 0 ],
  left: [ 0, -1 ],
  right: [ 0, 1 ]
}

const guardChars = new Map([['^', 'up'], ['>', 'right'], ['v', 'down'], ['<', 'left']])


const rows = parsedInput.length
const cols = parsedInput[0].length

console.log(rows, cols, rows*cols)

function getGuardInfo(){
	let guardPos = []
	let guardDirChar
	// let obstacles = new Map()

	parsedInput.forEach((row, i) => {
		row.split('').forEach((cell, j) => {
			if (guardChars.has(cell)){
				// console.log(cell, i, j)
				guardDirChar = cell
				guardPos = [i, j]
			}

			// if (cell == '#')
			// 	if(obstacles.get[i])
			// 		obstacles.set(i, obstacles.get[i].push(j))
			// 	else
			// 		obstacles.set(i, [j])
		})

	})
	// console.log(obstacles)

	return [guardPos, guardChars.get(guardDirChar)]
}

function getNextPosition(position = [0, 0], direction='up'){
	let nextRowCoord = position[0] + dirs[direction][0]
	let nextColCoord = position[1] + dirs[direction][1]

	return [nextRowCoord, nextColCoord]
}

function isBlocked(nextpos){
	return parsedInput[nextpos[0]][nextpos[1]] === '#' || 
		parsedInput[nextpos[0]][nextpos[1]] === 'O'
}


function isOutbounds(nextpos){
	return !parsedInput[nextpos[0]] || !parsedInput[nextpos[0]][nextpos[1]]
}


function getNewDirection(position, direction) {
	const guardDirsOrder = ['up','right', 'down', 'left']
	let dirIndex = guardDirsOrder.indexOf(direction)

	dirIndex = dirIndex + 1
	if(dirIndex == guardDirsOrder.length)
		dirIndex = 0
	
	return guardDirsOrder[dirIndex]
}


function getDirection(position = [0, 0], direction='down'){
	let nextpos = getNextPosition(position, direction)
	if (!isOutbounds(nextpos) && isBlocked(nextpos)) {
		const newDir = getNewDirection(position, direction)
		return [getNextPosition(position, newDir), newDir]
	}

	return [nextpos, direction]
}

function simulateWalkingPath(guardPos, guardDir){
	let direction = guardDir
	let position = guardPos
	let visitedSpotsHash = new Map()
	let visitedSpots = []
	console.log(position, direction, isBlocked(getNextPosition(position, direction)))

	// simulate guard's path
	while (true) {
		[position, direction] = getDirection(position, direction)

		// console.log(position)
		if(isOutbounds(position)) break

		visitedSpots.push(position)
		const hashKey = position[0]+','+position[1]
		if (!visitedSpotsHash.has(hashKey)){
			visitedSpotsHash.set(hashKey, 1)
		}

	}

	console.log(position, visitedSpotsHash.size)
	console.assert(visitedSpotsHash.size === 5269, 'Value should be 5269')
	return [position, visitedSpotsHash]
}

// get guard dir and pos
// check if there is any obstacle in front of guard
// mark the unique visited spots
// if its blocked, then turn right

let [guardPos, guardDir] = getGuardInfo()


simulateWalkingPath(guardPos, guardDir)
