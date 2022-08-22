// 反转双向链表
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *p_next;
    ListNode *p_prev;
    ListNode(int x) : val(x), p_next(NULL), p_prev(NULL) {};
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL) {
            return NULL;
        }
        ListNode *p_cur = head;
        ListNode *p_prev = NULL;
        while (p_cur != NULL) {
            ListNode *p_next = p_cur->p_next;
            p_cur->p_next = p_prev;
            p_cur->p_prev = p_next;
            p_prev = p_cur;
            p_cur = p_next;
        }
        return p_prev;
    }
};

int main() {
    ListNode *p_head = new ListNode(1);
    p_head->p_next = new ListNode(2);
    p_head->p_next->p_next = new ListNode(3);
    p_head->p_next->p_next->p_next = new ListNode(4);
    p_head->p_next->p_next->p_next->p_next = new ListNode(5);
    
    ListNode *p_tmp = p_head;
    cout << "The origin double link list:\n";
    while (p_head != NULL)
    {
        if (p_head->p_next == NULL)
        {
            cout << p_head->val;
        }
        else
        {
            cout << p_head->val << "<-->";
        }
        p_head = p_head->p_next;
    }
    Solution s;
    ListNode *p_new_head = s.reverseList(p_tmp);
    cout << "\nThe reversed double link list:\n";
    while (p_new_head != NULL) {
        if (p_new_head->p_next == NULL)
        {
            cout << p_new_head->val;
        }
        else
        {
            cout << p_new_head->val << "<-->";
        }
        p_new_head = p_new_head->p_next;
    }
    cout << endl;
    return 0;
}