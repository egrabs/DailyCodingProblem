// Given an array of numbers representing the stock prices of a company in chronological order and an integer k,
// return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

// For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

function maxProfit(prices, numTrades) {
    const profit = (new Array(numTrades+1)).fill(new Array(prices.length).fill(0, 0, prices.length), 0, numTrades+1);

    for (let k=1; k<numTrades+1; k++) {
        for (let i=1; i<prices.length; i++) {
            for (let j=0; j<i; j++) {
                profit[k][i] = Math.max(profit[k][i-1], prices[i] - prices[j] + profit[k-1][j]);
            }
        }
    }
    return Math.max(...profit[numTrades]);
}

console.log(maxProfit([5,2,4,0,1], 2));