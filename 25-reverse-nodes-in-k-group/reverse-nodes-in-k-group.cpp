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
    ListNode* reverseList(ListNode* head, int k){
        cout<<"YESSS";
        int count = 1;
        ListNode* ptr = head;
        ListNode* ptr2 = head->next;
        head->next = NULL;
        while(count <k){
            count += 1;
            ListNode* temp = ptr2->next;
            ptr2->next =  ptr;
            ptr = ptr2;
            ptr2 = temp;
        }

        return NULL;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* temp = head;
        if(!head){
            return head;
        }
        int count = 1;
        while(count < k){
            temp = temp->next;
            count += 1;
            // cout<<temp->val<<"\n";
            if(!temp){
                return head;
            }
        }
        ListNode* next_head = temp->next;
        reverseList(head, k);
        if(next_head)
            head->next = reverseKGroup(next_head, k);
        else
            head->next = NULL;
        return temp;
    }
};