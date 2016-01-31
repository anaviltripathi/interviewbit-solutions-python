/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
void Solution::connect(TreeLinkNode* root) {
    TreeLinkNode *tail = new TreeLinkNode(0);
    TreeLinkNode *dummy = tail;
    TreeLinkNode *node = root;
    
    
    while(node != NULL)
    {
        tail->next = node->left;
        if(tail->next != NULL)
            tail = tail->next;
        tail->next = node->right;
        if(tail->next != NULL)
            tail = tail->next;
        node = node->next;
        if(node == NULL)
        {
            tail = dummy;
            node = dummy->next;
        }
    }

}

