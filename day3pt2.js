import * as day3input from './day3input.js'

// console.log(day3input)
const testInput = day3input.input
// const testInput = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
console.log(testInput)
const pattern = /mul\(\d{1,3}\,\d{1,3}\)|don't\(\)|do\(\)/g


const mullMatchs = testInput.match(pattern)
console.log(mullMatchs)
let multitDisabled = false
const multits = mullMatchs.map(mull => {
	if ( mull === "don't()"){
		multitDisabled = true
		return 0
	}

	if ( mull === "do()"){
		multitDisabled = false
		return 0
	}

	if (multitDisabled) {
		return 0
	}

	const mullPattern = /\d{1,3}/g
	const numbersMatchs = mull.match(mullPattern)
	console.log(numbersMatchs)
	const result = parseInt(numbersMatchs[0]) * parseInt(numbersMatchs[1])
	console.log(result)
	return result

})
console.log(multits)

const multitsTotalSum = multits.reduce((acc, item) => {
	return acc+item
}, 0)

console.log(multitsTotalSum)
