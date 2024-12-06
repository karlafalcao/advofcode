function parseInput(input) {
    const [rules, updates] = input.split(/\n{2}/g).map(section => section.split('\n'));
    
    const pageOrderRules = rules.map(rule => {
        const [before, after] = rule.split('|').map(Number);
        return { before, after };
    });

    const updatesList = updates.map(update => update.split(',').map(Number));

    return { pageOrderRules, updatesList };
}

// Function to perform topological sort (Kahn's Algorithm)
function topologicalSort(pages, rules) {
    const inDegree = new Map();
    const adjList = new Map();

    // Initialize in-degree and adjacency list
    pages.forEach(page => {
        inDegree.set(page, 0);
        adjList.set(page, []);
    });

    // Build the graph with present pages only
    rules.forEach(rule => {
        if (adjList.get(rule.before) && adjList.get(rule.after)) {
            adjList.get(rule.before).push(rule.after);
            inDegree.set(rule.after, inDegree.get(rule.after) + 1);
        }
    });

    // Queue for pages with no dependencies (in-degree 0)
    const queue = [];
    pages.forEach(page => {
        if (inDegree.get(page) === 0) {
            queue.push(page);
        }
    });


    const result = [];
    while (queue.length > 0) {
        const currentPage = queue.shift();
        result.push(currentPage);

        adjList.get(currentPage).forEach(nextPage => {
            inDegree.set(nextPage, inDegree.get(nextPage) - 1);
            if (inDegree.get(nextPage) === 0) {
                queue.push(nextPage);
            }
        });
    }

    // If the result doesn't include all pages, there was a cycle
    if (result.length !== pages.length) {
        return [];
    }

    return result;
}

// Function to check if the update is in the correct order based on the rules
function isUpdateCorrect(update, rules) {
    const sortedUpdate = topologicalSort(update, rules);
    return JSON.stringify(update) === JSON.stringify(sortedUpdate);
}

// Main function to solve part two
function solvePartTwo(input) {
    const { pageOrderRules, updatesList } = parseInput(input);

    let sumMiddlePages = 0;

    updatesList.forEach(update => {
        // If update is not in the correct order
        if (!isUpdateCorrect(update, pageOrderRules)) {
            // Get the correct order
            const correctOrder = topologicalSort(update, pageOrderRules);

            // Find the middle page
            const middleIndex = Math.floor(correctOrder.length / 2);
            const middlePage = correctOrder[middleIndex];

            sumMiddlePages += middlePage;
        }
    });

    return sumMiddlePages;
}

const input = await Deno.readTextFile('./day5input.txt')
// Example input
// const input = `47|53
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
// 97,13,75,29,47`;

// Run the function and print the result
console.log(solvePartTwo(input)); // Output should be 123 for the provided example
// Correct response: 4655