// Given a list of points, a central point, and an integer k,
// find the nearest k points from the central point.

// For example, given the list of points [(0, 0), (5, 4), (3, 1)],
// the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].

const { performance } = require('perf_hooks');

function timeMe(test, times) {
    const start = performance.now();
    const retVal = test();
    times.push(performance.now() - start);
    return retVal;
}

function kNearest(points, center, k) {
    if (points.length <= k) return points;

    function dist(point) {
        return Math.sqrt(
            Math.pow(point[0] - center[0], 2) + Math.pow(point[1] - center[1], 2)
        );
    }

    const distances = new Map();
    points.forEach((p) => {
        distances.set(p, dist(p));
    });

    const kPts = [];
    while (kPts.length < k) {
        let min = Infinity;
        let minP = null;
        distances.forEach((val, key) => {
            if (val < min) {
                min = val;
                minP = key;
            }
        });
        kPts.push(minP);
        distances.set(minP, Infinity);
    }

    return kPts;
}

// O(n*log(n))
function kNearestOptimized(points, center, k) {
    if (points.length <= k) return points;

    function dist(point) {
        return Math.sqrt(
            Math.pow(point[0] - center[0], 2) + Math.pow(point[1] - center[1], 2)
        );
    }

    points.sort((a, b) => dist(a) - dist(b));
    return points.slice(0, k);
}


function kNearestSuperOptimized(points, center, k) {
    if (points.length <= k) return points;

    // O(1)
    function dist(point) {
        return Math.sqrt(
            Math.pow(point[0] - center[0], 2) + Math.pow(point[1] - center[1], 2)
        );
    }

    // I know there's array.unshift but I wanna do it myself
    // O(k)
    function shift(arr, i) {
        // unlike array.unshift's behavior of increasing the length of the array
        // here letting the last element in the array drop off is intentional
        for (let idx=k-1; idx>i; idx--) {
            arr[idx] = arr[idx-1];
        }
    }

    // initialize with one Infinity value
    // so the inner loop below doesn't have to have some ugly
    // "are we on the first value" condition
    // kPtsAndDists = [[point, dist] . . .]
    const kPts = [[[null, null], Infinity]];

    for (let i=0; i<points.length; i++) {
        let pt = points[i];
        let dst = dist(pt);
        for (let j=0; j<kPts.length; j++) {
            if (dst < kPts[j][1]) {
                shift(kPts, j);
                kPts[j] = [pt, dst];
                break;
            }
        }
    }

    return kPts.map(pair => pair[0])
}


console.log(kNearest([[0,0], [5,4], [3,1]], [1,2], 2));
console.log(kNearestOptimized([[0,0], [5,4], [3,1]], [1,2], 2));
console.log(kNearestSuperOptimized([[0,0], [5,4], [3,1]], [1,2], 2));

console.log(kNearest([[0,0], [5,4], [3,1], [1,2], [1,3], [16,15]], [1,2], 3));
console.log(kNearestOptimized([[0,0], [5,4], [3,1], [1,2], [1,3], [16,15]], [1,2], 3));
console.log(kNearestSuperOptimized([[0,0], [5,4], [3,1], [1,2], [1,3], [16,15]], [1,2], 3));

console.log('\n\n\n');

function* range(end) {
    let i = 0;
    while (i < end) yield i++;
}

const times = [];
const optimizedTimes = [];
const superOptimizedTimes = [];

let samples = 0;
// repeat generation of test data 3 times to smooth out any flukes from random date
while (samples < 3) {
    // for timing comparison, test many times on a biiiiig array of points
    // otherwise our results might not really be representative
    const testPoints = [...range(4000)].map(() => [Math.random(), Math.random()]);
    const testCenter = [Math.random(), Math.random()];
    const testK = 200;

    let tests = 0;

    while (tests < 1000) {
        timeMe(() => kNearest(testPoints, testCenter, testK), times);
        timeMe(() => kNearestOptimized(testPoints, testCenter, testK), optimizedTimes);
        timeMe(() => kNearestSuperOptimized(testPoints, testCenter, testK), superOptimizedTimes);
        tests++;
    }

    samples++;
}


const avgTime = times.reduce((a,b) => a+b) / times.length;
const avgOptimizedTime = optimizedTimes.reduce((a,b) => a+b) / optimizedTimes.length;
const avgSuperOptimizedTime = superOptimizedTimes.reduce((a,b) => a+b) / superOptimizedTimes.length;

console.log(`k nearest took an average of ${avgTime}s`);
console.log(`k nearest optimized took an average of ${avgOptimizedTime}s`);
// hmmmm sometimes optimized inches ahead of SUPER OPTIMIZED in terms of performance . . . 
// the .sort() builtin must have some horsepower!
console.log(`k nearest SUPER OPTIMIZED took an average of ${avgSuperOptimizedTime}s`);


