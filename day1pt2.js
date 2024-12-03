import * as locations from './locations.js'

// console.log(locations)
const lists = locations.lists

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
const similarityTotalSum = splitLists.reduce((acc, item) => {

    const itemSplt = item.split("   ")
    // console.log(acc, itemSplt)
    
    const split1 = parseInt(itemSplt[0])

    if (frequencyObj.hasOwnProperty(split1))
        acc += split1 * frequencyObj[split1]

    return acc
},0,)

console.log(similarityTotalSum)