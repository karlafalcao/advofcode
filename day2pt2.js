import * as reports from './reports.js'


const resportslist = reports.lists
// const resportslist = `7 6 4 2 1
// 1 2 7 8 9
// 9 7 6 2 1
// 1 3 2 4 5
// 8 6 4 4 1
// 1 3 6 7 9`.split('\n')
// console.log(resportslist)

const splittedItems = resportslist
	.map(_ => _.split(' '))
	.map(_ => _.map(_ => parseInt(_)))

// console.log(splittedItems)

const isSafeByOrderAndDiff = splittedItems.map(item => {

// 7 6 4 2 1
// 7 - 6 = 1
// for each report
// crescent=null
// for i=0 ate i=n-2
//  i e i+1
// 	diff = item[i] - item[i+1]
// 	if crescent is null
// 		if diff > 0: crescent=false
//  	else: crescent=true
	console.log("array item", item)

	let crescent = null
	let error = 0
	let errorIdx = null
	// for each report
	for (let i=0; i < item.length-1; i++){
		// if current index is equal to errorIdx
		// if next index is equal to errorIdx
		let currIdx = i, nextIdx = i+1

		if (currIdx === errorIdx && currIdx !== 0) currIdx -= 1
		if (nextIdx === errorIdx && nextIdx !== item.length-1) nextIdx += 1

		if (currIdx === errorIdx && currIdx === 0) {
			currIdx += 1
			nextIdx += 1
		}
		if (nextIdx === errorIdx && nextIdx === item.length-1) {
			currIdx -= 1
			nextIdx -= 1
		}

		console.log(item[currIdx], item[nextIdx])
		const adjDiff = (item[currIdx] - item[nextIdx])

		if(Math.abs(adjDiff) < 1 || Math.abs(adjDiff) > 3){
			console.log("Not Safe: diff limit")
			error += 1
			if (error >1) break
			// mark current index and test i -1 and i+1
			if (errorIdx === null){
				errorIdx = currIdx
			} else {
				errorIdx = nextIdx
			}
			if (currIdx === 0)
				i += 1
			if (nextIdx === item.length-1)
				i = i - 2
			continue
		}

		// 
		const diffLTZero = adjDiff < 0
		// console.log("Order check", adjDiff, diffLTZero)
		if (crescent === null) {
			crescent = diffLTZero
		} else {
			if (crescent !== diffLTZero){
				console.log("Not Safe: order change")
				error += 1
				if (error >1) break
				// mark current index and test i -1 and i+1
				if (errorIdx === null){
					errorIdx = currIdx
				} else {
					errorIdx = nextIdx
				}
				i = i - 1
				continue
			}
		}
	}

	console.log("Error Count: ", error)

	return error <= 1
})
console.log(isSafeByOrderAndDiff)

const totalSafeSum = isSafeByOrderAndDiff.reduce((acc, item) => {
	return item ? acc+=1 : acc
}, 0)

console.log(totalSafeSum)




