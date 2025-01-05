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
    ListNode *detectCycle(ListNode *head) {
        if(!head || !head->next)    return NULL;
        ListNode* ptr = head->next;
        while(ptr->next){
            if(ptr >= ptr->next)  return ptr->next;
            ptr = ptr->next;
        }        
        return NULL;
    }
};