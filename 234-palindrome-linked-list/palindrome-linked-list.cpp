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
    bool isPalindrome(ListNode* head) {
        if(!head || !head->next)    return true;
        ListNode* mid = head;
        ListNode* back = head;
        while(back->next){
            back = back->next;
            mid = mid->next;
            if(back->next){
                back = back->next;
            }
        }
        if(mid == back)     return mid->val == head->val;
        back = mid->next;
        mid->next = NULL;
        while(back->next){
            ListNode* temp = back->next;
            back->next = mid;
            mid = back;
            back = temp;
        }
        back->next = mid;
        mid = head;
        while(mid != back && mid->next != back){
            if(mid->val != back->val)     return false;
            mid = mid->next;
            back = back->next;
        }
        if(mid != back)     return mid->val == back->val;
        return true;
    }
};