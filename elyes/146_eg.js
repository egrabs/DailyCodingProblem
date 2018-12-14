// Given a binary tree where all nodes are either 0 or 1,
// prune the tree so that subtrees containing all 0s are removed.

// For example, given the following tree:

//    0
//   / \
//  1   0
//     / \
//    1   0
//   / \
//  0   0
// should be pruned to:

//    0
//   / \
//  1   0
//     /
//    1
// We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

function pruneTree(node) {
    function recurse(n) {
        if (!n.left && !n.right) {
            return n.val === 0;
        }
        let pruneLeft, pruneRight;
        if (n.left)
            pruneLeft = recurse(n.left);
        if (n.right)
            pruneRight = recurse(n.right);
        let pruneMe = n.val === 0;
        if (!pruneMe) {
            if (pruneRight) n.right = null;
            if (pruneLeft) n.left = null;
            return false;
        }
        return pruneLeft && pruneRight;
    }
    recurse(node);
    return node;
}


const root = {
    val: 0,
    left: {
        val: 1,
    },
    right: {
        val: 0,
        right: {
            val: 0,
        },
        left: {
            val: 1,
            left: {
                val: 0,
            },
            right: {
                val: 0,
            }
        }
    }
}

console.log(pruneTree(root));
