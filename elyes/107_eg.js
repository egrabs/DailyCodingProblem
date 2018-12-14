// Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

//   1
//  / \
// 2   3
//    / \
//   4   5

function printLevels(node) {
    const flat = [];
    function recurse(level) {
        const nextLevel = []
        level.forEach(n => {
            flat.push(n.val);
            if (n.left) nextLevel.push(n.left);
            if (n.right) nextLevel.push(n.right);
        });
        if (nextLevel.length > 0)
            recurse(nextLevel);
    }
    recurse([node]);
    console.log(flat);
}

rootNode = {
    val: 1,
    left: {
        val: 2
    },
    right: {
        val: 3,
        left: {
            val: 4,
        },
        right: {
            val: 5,
        }
    }
};

printLevels(rootNode);
