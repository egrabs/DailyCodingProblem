// Given a binary tree, find a minimum path sum from root to a leaf.

// For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

//   10
//  /  \
// 5    5
//  \     \
//    2    1
//        /
//      -1

// node = {
//     val,
//     left,
//     right,
// }

function minPath(rootNode) {
    const paths = [];
    function recurse(node, path) {
        const newPath = path.concat([node.val]);
        if (node.left) {
            recurse(node.left, newPath);
        }
        if (node.right) {
            recurse(node.right, newPath)
        }
        if (!node.left && !node.right) {
            paths.push(newPath);
        }
    }
    recurse(rootNode, []);
    const pathLengths = paths.map(p => p.reduce((a,b) => a+b, 0));
    return paths[pathLengths.indexOf(Math.min(...pathLengths))];
}

const two = { val: 2 };
const leftFive = { val: 5, right: two };
const negativeOne = { val: -1 };
const one = { val: 1, right: negativeOne };
const rightFive = { val: 5, right: one };
const ten = { val: 10, left: leftFive, right: rightFive };

console.log(minPath(ten));
