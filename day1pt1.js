import * as day1input from './day1input.js'

const lists = day1input.lists
// `40094   37480
// 52117   14510`

//
const result = lists.reduce((acc, item) => {
    const itemSplt = item.split("   ");
    console.log(acc, itemSplt);
    const split1 = (acc[0] || [])
    const split2 = (acc[1] || [])
    split1.push(itemSplt[0])
    split2.push(itemSplt[1])
    
	return [split1, split2]
  },[],)
const sortedLists = [result[0].sort(), result[1].sort()]
console.log(sortedLists)

// 
const diffsList = sortedLists[0].reduce((acc,item, index) => {
	acc.push(Math.abs(item-sortedLists[1][index]))
	return acc
}, [] )
console.log(diffsList)

// 
const totalDiffsSum = diffsList.reduce((acc, item) => acc+parseInt(item), 0)

console.log(totalDiffsSum)
console.assert(totalDiffsSum === '2430334')

