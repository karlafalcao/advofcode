export const input = await Deno.readTextFile('./day4input.txt')

// const input = `MMMSXXMASM
// MSAMXMSMSA
// AMXSXMAAMM
// MSAMASMSMX
// XMASAMXAMM
// XXAMMXXAMA
// SMSMSASXSS
// SAXAMASAAA
// MAMMMXMMMM
// MXMXAXMASX
// `

// console.log(input)
const pattern= /\n/g
// const rowsCount = input.match(pattern).length
const rowItems = input.split(pattern)
const rowsCount = rowItems.length
console.log(rowsCount)


const colsCount = rowItems[0].length
console.log(colsCount)


let xmasMatrix = rowItems
	.map(rowItem => rowItem.split(''))

let totalSum = 0
xmasMatrix
	.forEach((rowItem, rowIdx) => {
		
		console.log("Row Item List:",  rowItem)

		rowItem.forEach((cellItem, colIdx) => {
			if (cellItem === 'X') {
				const directions = getDirs()

				let surroundWords = []

				for (let dir in directions) {
					// console.log(dir, directions[dir])
					let wordChars = []

					let xC = rowIdx
					let yC = colIdx
					for (let i = 1; i<=3; i++){

						xC += directions[dir][0]
						yC += directions[dir][1]

						if (xC < 0 || xC > colsCount-1 || yC < 0 || yC > colsCount-1 ) continue
						
						wordChars.push(xmasMatrix[xC][yC])
					}

					if (!wordChars.length) continue

					surroundWords.push(wordChars)					
				}

				console.log(cellItem, xmasMatrix[rowIdx][colIdx])
				let matchedWords = surroundWords.map(_ => _.join('')).filter(_ => _ === 'MAS')

				console.log(surroundWords, matchedWords, matchedWords.length)
				totalSum += matchedWords.length

			}

		})
	})


console.log(totalSum)

function getDirs () {
	return {
	  up: [ -1, 0 ],
	  down: [ 1, 0 ],
	  left: [ 0, -1 ],
	  right: [ 0, 1 ],
	  upleft: [ -1, -1 ],
	  upright: [ -1, 1 ],
	  downleft: [ 1, -1 ],
	  downright: [ 1, 1 ]
	}
}
