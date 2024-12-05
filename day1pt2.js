import * as day1input from './day1input.js'

const lists = day1input.lists
// `40094   37480
// 52117   14510`

// a hashtable containing each number frequency
const frequencyObj = lists.reduce((acc, item) => {
    const itemSplt = item.split("   ")
    // console.log(acc, itemSplt)
    const split2 = parseInt(itemSplt[1])


    if (acc.hasOwnProperty(split2))
    	acc[split2] += 1
    else
    	acc[split2] = 1

	return acc
  },{},)

console.log(frequencyObj)

// 
const similarityTotalSum = lists.reduce((acc, item) => {

    const itemSplt = item.split("   ")
    // console.log(acc, itemSplt)
    
    const split1 = parseInt(itemSplt[0])

    if (frequencyObj.hasOwnProperty(split1))
        acc += split1 * frequencyObj[split1]

    return acc
},0,)

console.log(similarityTotalSum)

console.assert(similarityTotalSum === '28786472')