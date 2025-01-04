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
    ListNode* reverse(ListNode* prev, ListNode* ptr){
        if(!ptr->next){
            ptr->next = prev;
            return ptr;
        }
        ListNode* temp = ptr->next;
        ptr->next = prev;
        if(temp)    return reverse(ptr, temp);
        else    return ptr;
    }
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next)    return head;
        ListNode* temp = head->next;
        head->next = NULL;
        return reverse(head, temp);
    }
};