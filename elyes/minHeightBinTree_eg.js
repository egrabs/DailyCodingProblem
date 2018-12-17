// given a sorted array of integers, build the minimum height binary tree from them

class BinTree {
	constructor() {
		this.root = null;
	}

	add(val) {
		if (!this.root) {
			this.root = { val: val };
		} else {
			this._add(val, this.root);
		}
	}

	_add(val, node) {
		if (val < node.val) {
			if (!node.left) node.left = { val };
			else this._add(val, node.left);
		} else if (val > node.val) {
			if (!node.right) node.right = { val };
			else this._add(val, node.right);
		}
	}

}

function minHeightBinTree(lst, bt) {
	if (lst.length === 0) return;
	if (lst.length === 1) {
		bt.add(lst[0]);
		return;
	}

	const idx = Math.floor(lst.length / 2);
	bt.add(lst[idx]);

	// left subtree
	minHeightBinTree(lst.slice(0, idx), bt);

	// right subtree
	minHeightBinTree(lst.slice(idx+1), bt);
}

const bt1 = new BinTree();

minHeightBinTree([1,2,3,4,5,6,7,8,9], bt1);

const bt2 = new BinTree();

minHeightBinTree([1,2,3,4], bt2);
