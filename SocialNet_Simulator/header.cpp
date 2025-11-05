#ifndef HEADER_CPP
#define HEADER_CPP

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <map>
#include <queue>
#include<list>
#include <ctime>
#include <sstream>

using namespace std;

int global_counter = 0;

struct Node{
    string content;
    time_t key;

    Node* left;
    Node* right;
    Node* parent;
    int height;

    Node(string s) : content(s), key(global_counter), left(nullptr), right(nullptr), parent(nullptr), height(1) {global_counter++;}
    Node(int k) : content(""), key(global_counter), left(nullptr), right(nullptr), parent(nullptr), height(1) {global_counter++;}
    Node() : content(""), key(global_counter), left(nullptr), right(nullptr), parent(nullptr), height(1) {global_counter++;}
};

class AVL {
private:
    Node* root;

    int height(Node* n) {
        return n ? n->height : 0;
    }

    int balance_factor(Node* n) {
        return n ? height(n->left) - height(n->right) : 0;
    }

    void update_height(Node* n) {
        n->height = 1 + max(height(n->left), height(n->right));
    }

    Node* right_rotate(Node* y) {
        Node* x = y->left;
        Node* T2 = x->right;

        // Rotation
        x->right = y;
        y->left = T2;

        if (T2) T2->parent = y;

        // Parent pointers
        x->parent = y->parent;
        y->parent = x;

        if (x->parent && x->parent->left == y) x->parent->left = x;
        else if (x->parent && x->parent->right == y) x->parent->right = x;

        // Update heights
        update_height(y);
        update_height(x);

        return x;
    }

    Node* left_rotate(Node* x) {
        Node* y = x->right;
        Node* T2 = y->left;

        // Rotation
        y->left = x;
        x->right = T2;

        if (T2) T2->parent = x;

        // Parent pointers
        y->parent = x->parent;
        x->parent = y;

        if (y->parent && y->parent->left == x) y->parent->left = y;
        else if (y->parent && y->parent->right == x) y->parent->right = y;

        // Update heights
        update_height(x);
        update_height(y);

        return y;
    }

    Node* insert(Node* node, Node* insert_node, Node* parent) {
        if (!node) {
            node = insert_node;
            return node;
        }


        if (insert_node->key < node->key)
            node->left = insert(node->left, insert_node, node);
        else if (insert_node->key > node->key)
            node->right = insert(node->right, insert_node, node);
        else
            return node; 

        update_height(node);

        int balance = balance_factor(node);

        if (balance > 1 && insert_node->key < node->left->key)
            return right_rotate(node);

        if (balance < -1 && insert_node->key > node->right->key)
            return left_rotate(node);

        if (balance > 1 && insert_node->key > node->left->key) {
            node->left = left_rotate(node->left);
            return right_rotate(node);
        }

        if (balance < -1 && insert_node->key < node->right->key) {
            node->right = right_rotate(node->right);
            return left_rotate(node);
        }

        return node;
    }


    vector<string> inorder(Node* node) {
        vector<string> v;
        if (!node) return v;
        vector<string> v1 = inorder(node->left);
        for (auto i : v1) v.push_back(i);
        v.push_back(node->content);
        vector<string> v2 = inorder(node->right);
        for (auto i : v2) v.push_back(i);
        return v;
    }

public:
    AVL() : root(nullptr) {}

    void insert(string s) {
        Node* temp = new Node(s);
        if (root == nullptr) {
            root = temp;
            return;
        }
        root = insert(root, temp, nullptr);
    }

    vector<string> inorder_traversal() {
        return inorder(root);
    }
};
#endif 