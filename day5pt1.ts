const input = await Deno.readTextFile('./day5input.txt')

const inputData = input.split(/\n{2}/g)
// const inputData = `47|53
// 97|13
// 97|61
// 97|47
// 75|29
// 61|13
// 75|53
// 29|13
// 97|29
// 53|29
// 61|53
// 97|53
// 61|29
// 47|13
// 75|47
// 97|75
// 47|61
// 75|61
// 47|29
// 75|13
// 53|13

// 75,47,61,53,29
// 97,61,53,29,13
// 75,29,13
// 75,97,47,61,53
// 61,13,29
// 97,13,75,29,47`.split(/\n{2}/g)

const pageOrderingRules = inputData[0].split(/\n/g)

const pagesToProduce = inputData[1].split(/\n/g)
console.log(pageOrderingRules, pagesToProduce)

const updatesSplitted = pagesToProduce.map((item) => item.split(','))

console.log(updatesSplitted)

const correctUpdates = updatesSplitted.reduce((acc, item: array) => {
	// console.log(splittedItems)
	//
	const pagesDict = item.reduce( (acc, item, i) => { return {...acc, [item]: i} }, {} )

	const corretlyOrdered = pageOrderingRules.every(orderRule => {
		const rule = orderRule.split('|')

		if(pagesDict[rule[0]] === undefined || pagesDict[rule[1]] === undefined) return true

		return pagesDict[rule[0]] < pagesDict[rule[1]]

	})

	console.log('Is correctly ordered: ', corretlyOrdered)

	if(corretlyOrdered) {
		const medianIndex = parseInt(Number(item.length) / 2)
		console.log(item, medianIndex, item[medianIndex])

		return acc + Number(item[medianIndex])
	}

	return acc

}, 0)

console.log(correctUpdates)
console.log('Correct response:', 4959)
