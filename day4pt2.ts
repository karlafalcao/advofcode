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
// MXMXAXMASX`

// console.log(input)
const pattern= /\n/g


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
			if (cellItem === 'A') {

				const diags = getDiagonals()

				let surroundWords = []

				for (let diag in diags) {
					// console.log(diag, diags[diag])
					let wordChars = []

					let xC
					let yC

					const directions = diags[diag]

					for (let dir in directions) {

						// console.log(dir, directions[dir])
						xC = rowIdx + directions[dir][0]
						yC = colIdx + directions[dir][1]

						if (xC < 0 || xC > colsCount-1 || yC < 0 || yC > colsCount-1 ) continue
						
						wordChars.push(xmasMatrix[xC][yC])
					}
					
					if (!wordChars.length) continue

					
					surroundWords.push(wordChars)
				}

				console.log(cellItem, xmasMatrix[rowIdx][colIdx])
				let matchedWords = surroundWords.map(_ => _.join('A')).filter(_ => _ === 'MAS' || _ === 'SAM')

				console.log(surroundWords, matchedWords, matchedWords.length)
				if (matchedWords.length === 2)
					totalSum += 1

			}

		})
	})


console.log(totalSum)

function getDiagonals () {
	return [
		{
		  upleft: [ -1, -1 ],
		  downright: [ 1, 1 ]
		},
		{
		  upright: [ -1, 1 ],
		  downleft: [ 1, -1 ]
		}
	]
}
