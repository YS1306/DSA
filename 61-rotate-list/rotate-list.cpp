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
    ListNode* rotateRight(ListNode* head, int k) {
        int count = 1;
        ListNode* ptr_n = head;
        if(!head || !head->next || (k==0))
            return head;
        
        while(ptr_n->next){
            count += 1;
            ptr_n = ptr_n->next;
        }

        k = k%count;
        if(k==0)   
            return head;
        ListNode* ptr_k = head;

        for(int i =1; i<(count-k); i++){
            ptr_k = ptr_k->next;
        }

        ListNode* temp = ptr_k->next;
        ptr_n->next = head;
        ptr_k->next = NULL;
        return temp;

    }
};