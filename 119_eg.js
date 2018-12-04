// Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
// If there are multiple smallest sets, return any of them.

// For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.

// assuming all intervals are given as inclusive intervals
function smallestCover(intervals) {
    const reducedSets = [];
    for (let interval of intervals) {
        let foundSet = false;
        for (let i=0; i<reducedSets.length; i++) {
            const updated = updateReducedSet(reducedSets[i], interval);
            if (updated !== null) {
                reducedSets[i] = updated;
                foundSet = true;
            }
        }
        if (!foundSet) {
            reducedSets.push(interval);
        }
    }
    return new Set(reducedSets.map(nums => nums[0]));
}

function updateReducedSet(reducedSet, interval) {
    let [lower, upper] = reducedSet;
    if (
            interval[0] >= lower && interval[0] <= upper
            || interval[1] <= upper && interval[1] >= lower
            || lower >= interval[0] && lower <= interval[1]
            || upper >= interval[0] && upper <= interval[1]
        ) return [Math.max(interval[0], lower), Math.min(interval[1], upper)];
    return null;
}

const intervals = [[0, 3], [2, 6], [3, 4], [6, 9]];
console.log(smallestCover(intervals));

