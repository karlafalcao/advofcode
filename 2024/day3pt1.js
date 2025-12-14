import * as day3input from './day3input.js'

// console.log(day3input)
const testInput = day3input.input
// const testInput = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
console.log(testInput)
const pattern = /mul\(\d{1,3}\,\d{1,3}\)/g


const mullMatchs = testInput.match(pattern)
console.log(mullMatchs)

const multits = mullMatchs.map(mull => {

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
