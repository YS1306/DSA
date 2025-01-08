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

    ListNode* findMid(ListNode* head){
        if(!head || !head->next)    return head;
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
        temp->next = NULL;
        return one;
    }

    ListNode* merge(ListNode* first, ListNode* second) {
        ListNode* head = nullptr;
        ListNode* tail = nullptr;
        if (!first) return second;
        if (!second) return first;

        if (first->val <= second->val) {
            head = first;
            first = first->next;
        } else {
            head = second;
            second = second->next;
        }
        tail = head;  // Now 'tail' points to the first node of the merged list.

        while (first && second) {
            if (first->val <= second->val) {
                tail->next = first;  // Link the node from the first list
                first = first->next; // Move to the next node in the first list
            } else {
                tail->next = second; // Link the node from the second list
                second = second->next; // Move to the next node in the second list
            }
            tail = tail->next; // Move the tail pointer forward
        }

        if (first) {
            tail->next = first;
        }
        if (second) {
            tail->next = second;
        }

        return head;
    }

    ListNode* sortList(ListNode* head) {
        if(!head || !head->next)    return head;

        if(!head->next->next){
            if(head->next->val < head->val){
                ListNode* temp = head->next;
                head->next = nullptr;
                temp->next = head; 
                head = temp;
            }
            return head;
        }
        else{
            ListNode* mid = findMid(head);
            head = sortList(head);
            mid = sortList(mid);
            head = merge(head, mid);
        }

        return head;
    }
};