/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(!head || !head->next)    return false;
        ListNode* ptr = head->next;
        while(ptr->next){
            if(ptr >= ptr->next )    return true;
            ptr = ptr->next; 
        }
        return false;
    }
};