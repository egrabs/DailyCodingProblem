// Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

// For example, given the following tree and K of 20

//     10
//    /   \
//  5      15
//        /  \
//      11    15
// Return the nodes 5 and 15.

function findSummandNodes(rootNode, k) {    
    function traverse(node) {
        const curVal = node.val;
        const remaining = k - curVal;
        const findNode = findNodeWithValue(rootNode, remaining);
        if (findNode && findNode !== node) {
            return [node, findNode];
        }
        if (node.left) {
            return traverse(node.left);
        }
        if (node.right) {
            return traverse(node.right);
        }
        return [null, null]
    }

    return traverse(rootNode);
}

function findNodeWithValue(node, val) {
    if (node === null) return null;
    if (node.val === val) return node;
    if (val > node.val) return findNodeWithValue(node.right, val);
    if (val < node.val) return findNodeWithValue(node.left, val);
}

eleven = { val: 11 };
fifteen = { val: 15 };
otherFifteen = { val: 15, left: eleven, right: fifteen };
five = { val: 5 };
ten = { val: 10, left: five, right: otherFifteen };

console.log(findSummandNodes(ten, 20));