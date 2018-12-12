// There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
// Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

// For example, if N is 4, then there are 5 unique ways:

// 1, 1, 1, 1
// 2, 1, 1
// 1, 2, 1
// 1, 1, 2
// 2, 2
// What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
// For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

function chooseBIC(n, k) {
    function muddaFAK(n) {
        if (n == 0 || n == 1)
            return 1;
        return n*muddaFAK(n-1);
    }
    return muddaFAK(n) / (muddaFAK(n-k)*muddaFAK(k))
}

function waysToClimb(n) {

    // all 1's case
    var ways = 1;

    var numTwos = Math.floor(n / 2);
    var numOnes = n%2 === 0 ? 0 : 1;

    while (numTwos > 0) {
        ways += chooseBIC(numTwos+numOnes, numOnes);
        numOnes += 2;
        numTwos--;
    }

    return ways;
}

console.log(waysToClimb(process.argv[2]));


/* vomit */

// function waysToClimbArbitrary(n, stepIntvs) {
//     var ways = 0;
//     if (stepIntvs.contains(n)) ways++;

//     var remaining = n;

//     var validIntvs = [...stepIntvs]
//         .filter(x => x <= n)
//         .sort();

//     var counts = new Map();
        
//     counts.put(biggest, n / biggest);
//     var remain = n % biggest;
//     var offset = 2;
//     while (remain) {
//         if (remain > validIntvs[validIntvs.length-offset]) {
            
//         }
//     }

// }





