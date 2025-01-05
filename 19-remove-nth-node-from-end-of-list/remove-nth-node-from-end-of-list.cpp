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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(!head || !head->next)    return NULL;
        ListNode* counter = head;
        ListNode* back = head;
        int count = 0;
        while(back->next){
            count++;
            back = back->next;
            if(count > n)   counter = counter->next;
        }   
        if(counter == head && n==count+1)  return head->next; 
        counter->next = counter->next->next;
        return head;
    }
};