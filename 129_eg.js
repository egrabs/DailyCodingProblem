// Given a real number n, find the square root of n. For example, given n = 9, return 3.

function sqrt(n) {
    let estimate = n / 2;
    const _sqrtTest = x => x*x - n;
    const _sqrtTestDeriv = x => 2*x;
    const iterate = guess => guess - _sqrtTest(guess) / _sqrtTestDeriv(guess);
    const delta = 0.000000000000001;
    for (let i=0; i<1000; i++) {
        let prevEstimate = estimate;
        estimate = iterate(estimate);
        if (Math.abs(prevEstimate - estimate) < delta)
            break;
    }
    return estimate;
}

console.log(sqrt(9.5));