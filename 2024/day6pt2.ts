
const dirs = {
  up: [ -1, 0 ],
  down: [ 1, 0 ],
  left: [ 0, -1 ],
  right: [ 0, 1 ]
}

const guardChars = new Map([['^', 'up'], ['>', 'right'], ['v', 'down'], ['<', 'left']])

function getGuardInfo(){
	let guardPos = []
	let guardDirChar
	// let obstacles = new Map()

	parsedInput.forEach((row, i) => {
		row.forEach((cell, j) => {
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
	return !isOutbounds(nextpos) && (parsedInput[nextpos[0]][nextpos[1]] === '#' || 
		parsedInput[nextpos[0]][nextpos[1]] === 'O')
}


function isOutbounds(nextpos){
	return !parsedInput[nextpos[0]] || !parsedInput[nextpos[0]][nextpos[1]]
}


function getNewDirection(position, direction) {
	const guardDirsOrder = ['up','right', 'down', 'left']
	let dirIndex = ( guardDirsOrder.indexOf(direction) + 1) % 4
	return guardDirsOrder[dirIndex]
}


function getDirection(position = [0, 0], direction='down'){
	let nextpos = getNextPosition(position, direction)
	if ( isBlocked(nextpos)) {
		const nextposhashKey = nextpos[0]+','+nextpos[1]
		const newDir = getNewDirection(position, direction)
		return [getNextPosition(position, newDir), newDir, nextposhashKey]
	}

	return [nextpos, direction, '']
}
//

function simulateWalkingPath(guardPos, guardDir){
	let direction = guardDir
	let position = guardPos
	let prevpos = ''
	let blockPos = ''
	let visitedSpotsHash = new Map()
	let visitedBlocks = new Map()

	console.log(`Initial position:`, position, 'Initial direction: ', direction)

	const hashKey = position[0]+','+position[1]
	visitedSpotsHash.set(hashKey, 1)

	// simulate guard's path
	while (true) {

		prevpos = position

		const newInfo = getDirection(position, direction)
		
		if(newInfo[2]){
			blockPos = newInfo[2].split(',')
			direction = newInfo[1]
			const blockHash = blockPos[0]+','+blockPos[1]+','+direction

			if (visitedBlocks.has(blockHash)) break
			visitedBlocks.set(blockHash, 1)
				
		}	else {

			position = newInfo[0]
			// console.log(position)
			if(isOutbounds(position)) break

			const hashKey = position[0]+','+position[1]
			visitedSpotsHash.set(hashKey, 1)
		}
	}

	console.log(`Final position:`, position, 'Value: ', visitedSpotsHash.size)
	
	return [position, visitedSpotsHash]
}

function checkMazes() {
	// For each step
	const loopedMazes = []
	mazesList.forEach((input) => {
		parsedInput = input

		const [finalPos, ..._ ] = simulateWalkingPath(guardPos, guardDir)

		if(!isOutbounds(finalPos)){

			console.log(finalPos, 'isLoop: ', !isOutbounds(finalPos) )
			loopedMazes.push(input)
		}

	})

	console.log(loopedMazes.length)
}

async function generateMazes() {
	const [finalPos, uniquevisitedSpotsHash ] = simulateWalkingPath(guardPos, guardDir)
	console.log(finalPos, 'isLoop: ', !isOutbounds(finalPos) )
	console.assert(uniquevisitedSpotsHash.size === 5269, 'Value should be 5269')
	// add a # char for each uniquevisitedSpotsHash item
	// console.log("uniquevisitedSpotsHash", uniquevisitedSpotsHash)
	uniquevisitedSpotsHash.keys().forEach((spot) => {
		let mazeIn = input.split(/\n/).map(row => row.split(''))
		// check
		const newBlockPosition = spot.split(',').map(Number)
		if(guardPos[0] !== newBlockPosition[0] || guardPos[1] !== newBlockPosition[1]){
			// console.log("newBlockPosition", guardPos, newBlockPosition)
			mazeIn[newBlockPosition[0]][newBlockPosition[1]] = 'O'
		}
		// console.log("mazeInput", mazeIn.map(row => row.join('')))
		mazesList.push(mazeIn)

	})

	const fileContent = `\n\nday6input_mazes = ` + JSON.stringify(
	mazesList.map(mazeIn=>mazeIn.map(row => row.join(''))), null, 2)
	await Deno.writeTextFile("day6input_mazes.py", fileContent, { append: true });
}


let input = `....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...`

input = await Deno.readTextFile('./day6input.txt')

let parsedInput = input.split(/\n/).map(row => row.split(''))
// console.log(parsedInput)

// const rows = parsedInput.length
// const cols = parsedInput[0].length
// console.log(rows, cols, rows*cols)

let mazesList = []

// mazesList = [
// `....#.....
// ....+---+#
// ....|...|.
// ..#.|...|.
// ....|..#|.
// ....|...|.
// .#.O^---+.
// ........#.
// #.........
// ......#...`,
// `....#.....
// ....+---+#
// ....|...|.
// ..#.|...|.
// ..+-+-+#|.
// ..|.|.|.|.
// .#+-^-+-+.
// ......O.#.
// #.........
// ......#...`,
// `....#.....
// ....+---+#
// ....|...|.
// ..#.|...|.
// ..+-+-+#|.
// ..|.|.|.|.
// .#+-^-+-+.
// .+----+O#.
// #+----+...
// ......#...`,
// `....#.....
// ....+---+#
// ....|...|.
// ..#.|...|.
// ..+-+-+#|.
// ..|.|.|.|.
// .#+-^-+-+.
// ..|...|.#.
// #O+---+...
// ......#...`,
// `....#.....
// ....+---+#
// ....|...|.
// ..#.|...|.
// ..+-+-+#|.
// ..|.|.|.|.
// .#+-^-+-+.
// ....|.|.#.
// #..O+-+...
// ......#...`,
// `....#.....
// ....+---+#
// ....|...|.
// ..#.|...|.
// ..+-+-+#|.
// ..|.|.|.|.
// .#+-^-+-+.
// .+----++#.
// #+----++..
// ......#O..`
// ].map(_ => _.split(/\n/).map(row => row.split('')))


let [guardPos, guardDir] = getGuardInfo()

generateMazes()
// checkMazes()

