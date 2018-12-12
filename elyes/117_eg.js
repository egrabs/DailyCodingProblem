// Given a binary tree, return the level of the tree with minimum sum.

function minLevel(rootNode) {
    let minDepth = null;
    let minSum = Infinity;
    function recurse(level, depth) {
        let levelSum = 0;
        const nextLevel = [];
        for (let node of level) {
            levelSum += node.val;
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        if (levelSum < minSum) {
            minSum = levelSum;
            minDepth = depth;
        }
        recurse(nextLevel, depth+1);
    }
    recurse([rootNode], 0);
    return minDepth;
}