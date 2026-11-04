class Node {
    public:
        int value;
        Node* next;
        Node(int value) {
            this->value = value;
            next = nullptr;
        }
};

class LinkedList {
    private:
        Node* head;
        Node* tail;
        int length;

    public:
        LinkedList() {
            head = new Node(-1);
            tail = head;
            length = 0;
        }

        int get(int index) {
            Node* curr = head->next;
            int i = 0;
            while (curr != nullptr) {
                if (i == index) {
                    return curr->value;
                }
                i++;
                curr = curr->next;
            }
            return - 1;
        }

        void insertHead(int val) {
            Node* newNode = new Node(val);
            if (length == 0) {
                head->next = newNode;
                tail = newNode;
            } else {
                newNode->next = head->next;
                head->next = newNode;
            }
            length++;
            
        }
        
        void insertTail(int val) {
            Node* newNode = new Node(val);
            tail->next = newNode;
            tail = newNode;
            length++;

        }

        bool remove(int index) {
            if (index < 0 || index >= length) return false;

            Node* prev = head;
            int i = 0;
            while (i < index) {
                prev = prev->next;
                i++;
            }

            Node* toDelete = prev->next;
            prev->next = toDelete->next;

            if (toDelete == tail) {
                tail = prev;
            }

            delete toDelete;
            length--;
            return true;
        }

        vector<int> getValues() {
            vector<int> res;
            Node* curr = head->next;
            while (curr!= nullptr) {
                res.push_back(curr->value);
                curr = curr->next;
            }
            return res;
        }
};
