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
        cout<<head-head->next;
        while(head->next){
            if(head-head->next >= 0)    return true;
            head = head->next; 
        }
        return false;
    }
};