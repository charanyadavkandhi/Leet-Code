class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in mp: mp[parent] = TreeNode(parent)
            if child not in mp: mp[child] = TreeNode(child)

            if isLeft:
                mp[parent].left = mp[child]
            else:
                mp[parent].right = mp[child]

            children.add(child)

        for parent, child, isLeft in descriptions:
            if parent not in children:
                return mp[parent]