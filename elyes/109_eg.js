// Given an unsigned 8-bit integer, swap its even and odd bits.
// The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

// For example, 10101010 should be 01010101. 11100010 should be 11010001.

// Bonus: Can you do this in one line?

function swapEvenAndOddBits(num) {
    return ((num << 1) & 0b10101010) | ((num >> 1) & 0b01010101);
}

console.log(swapEvenAndOddBits(0b10101010) === 0b01010101);
console.log(swapEvenAndOddBits(0b11100010) === 0b11010001);