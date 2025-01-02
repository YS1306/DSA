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
    ListNode* middleNode(ListNode* head) {
        ListNode* second = head;
        ListNode* first = head;
        while(second->next){
            first = first->next;
            second = second->next;
            if(second->next)  second = second->next;
            cout<<second->val;
        }
        return first;
    }
};