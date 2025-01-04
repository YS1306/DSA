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
        ListNode* ptr = head;
        cout<<ptr-ptr->next<<endl;
        while(ptr->next){
            if(int(ptr-ptr->next) >= 0)    return true;
            ptr = ptr->next; 
        }
        return false;
    }
};