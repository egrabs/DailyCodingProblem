// Given  list of possibly overlapping intervals,
// return a new list of intervals where all overlapping intervals have been merged

// eg [[1,3], [5,8], [4,10], [20,25]] -> [[1,3], [4, 10], [20,25]]

function mergeOverlapping(intervals) {
	const merged = [];
	const overlaps = (int1, int2) => {
		const [x1, y1] = int1;
		const [x2, y2] = int2;
		return (x1 >= x2 && x1 <= y2) || (y1 <= y2 && y1 >= x2) || (x2 >= x1 && x2 <= y1) || (y2 <= y1 && y2 >= x1);
	}

	for (let interval of intervals) {
		let didMerge = false;
		for (let i=0; i<merged.length; i++) {
			mergeInt = merged[i];
			if (overlaps(mergeInt, interval)) {
				merged[i] = [Math.min(mergeInt[0], interval[0]), Math.max(mergeInt[1], interval[1])];
				didMerge = true;
			}
		}
		if (!didMerge)
			merged.push(interval);
	}

	return merged;
}

console.log(mergeOverlapping([[1,3], [5,8], [4,10], [20,25]]));
