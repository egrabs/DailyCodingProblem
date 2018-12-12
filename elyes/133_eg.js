/*
* Given a node in a binary tree, return the next bigger element, also known as the inorder successor
*/

      //     10
      //   /    \
      // 5      30
      //       /  \
      //     22   35
      //       \
      //       28
      //      /  \
      //     24  29

      // in-order successor of 5 is 10
      // in-order successor of 22 is 24
      // in-order successor of 35 is null

/*
* Assuming that the nodes look something like:
* {
*   val,
*   left,
*   right,
*   parent   
* }
*
*/

function inOrderSuccessor(node) {
    if (!node) return null;

    function helper(n) {
        if (n === null) return null;
        if (n.left) return helper(n.val);
        return n.val;
    }

    let valBelow = helper(node.right);

    if (node.parent && valBelow !== null) return Math.min(node.parent.val, valBelow);
    if (node.parent) return node.parent.val;
    if (valBelow !== null) return valBelow;
    return null;
}
