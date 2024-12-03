
import * as reports from './reports.js'



// const resportslist = reports.lists
const resportslist = `7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9`.split('\n')
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
	// for each report
	for (let i=0; i < item.length-1; i++){
		console.log(item[i], item[i+1])
		const adjDiff = (item[i] - item[i+1])

		if(Math.abs(adjDiff) < 1 || Math.abs(adjDiff) > 3 )
			return false

		const diffLTZero = adjDiff < 0
		
		if (crescent === null) {
			crescent = diffLTZero
		} else {
			if (crescent !== diffLTZero){
				return false
			}
		}
	}
	return true
})

console.log(isSafeByOrderAndDiff)
const totalSafeSum = isSafeByOrderAndDiff.reduce((acc, item) => {
	return item ? acc+=1 : acc
}, 0)

console.log(totalSafeSum)




