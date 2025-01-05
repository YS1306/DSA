/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if(!head || !head->next)    return NULL;
        ListNode* one = head;
        ListNode* two = head;
        ListNode* temp;
        while(two->next){
            two = two->next;
            temp = one;
            one = one->next;
            if(two->next){
                two = two->next;
            }
        }
        temp->next = temp->next->next;
        return head;
    }
};