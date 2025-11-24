#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <sstream>

using namespace std;

class TimePriorityQueue {
private:
    vector<pair<time_t, string>> q;

public:
    void bubbleup(int i) {
        while (i > 0) {
            int parent = (i - 1) / 2;
            if (q[i].first > q[parent].first) { 
                swap(q[i], q[parent]);
                i = parent;
            } 
            else break;
        }
    }

    void heapify(int i) {
        int n = q.size();
        while (true) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int largest = i; 

            if (left < n && q[left].first > q[largest].first) largest = left;
            if (right < n && q[right].first > q[largest].first) largest = right;

            if (largest != i) {
                swap(q[i], q[largest]);
                i = largest;
            } else break;
        }
    }

    void push(time_t timestamp, const string& value) {
        q.push_back({timestamp, value});
        bubbleup(q.size() - 1);
    }

    void pop() {
        if (q.empty()) return;
        q[0] = q.back();
        q.pop_back();
        if (!q.empty()) heapify(0);
    }

    pair<time_t, string> top() const {
        if (q.empty()) throw runtime_error("queue is empty");
        return q[0];
    }

    bool empty() const { return q.empty(); }
    int size() const { return q.size(); }
};


class IntPriorityQueue {
private:
    vector<pair<int, string>> q;

public:
    void bubbleup(int i) {
        while (i > 0) {
            int parent = (i - 1) / 2;
            if (q[i].first > q[parent].first) {  
                swap(q[i], q[parent]);
                i = parent;
            } 
            else break;
        }
    }

    void heapify(int i) {
        int n = q.size();
        while (true) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int largest = i;

            if (left < n && q[left].first > q[largest].first) largest = left;
            if (right < n && q[right].first > q[largest].first) largest = right;

            if (largest != i) {
                swap(q[i], q[largest]);
                i = largest;
            } else break;
        }
    }

    void push(int priority, const string& value) {
        q.push_back({priority, value});
        bubbleup(q.size() - 1);
    }

    void pop() {
        if (q.empty()) return;
        q[0] = q.back();
        q.pop_back();
        if (!q.empty()) heapify(0);
    }

    pair<int, string> top() const {
        if (q.empty()) throw runtime_error("Empty queue");
        return q[0];
    }

    bool empty() const { return q.empty(); }
    int size() const { return q.size(); }
};


struct TreeNode{ 
    int version_id; 
    string content; 
    string message = ""; // Empty if not a snapshot 
    time_t created_timestamp; 
    time_t snapshot_timestamp = 0; // Null if not a snapshot
    time_t last_modified_timestamp; 
    TreeNode* parent; 
    vector<TreeNode*> children;

    TreeNode(){
        version_id = 0;
        content = "";
        created_timestamp = time(0);
        parent = nullptr;
        last_modified_timestamp = time(0);
    }
};


class IntMap {
private:
    vector<pair<int, TreeNode*>> v;

    int find_index(int key) {
        for (int i = 0; i < v.size(); i++) {
            if (v[i].first == key) return i;
        }
        return -1;
    }

public:
    TreeNode*& return_TreeNode(int key ) {
        int idx = find_index(key);
        if (idx == -1) {
            v.push_back({key, nullptr});
            return v.back().second;
        }
        return v[idx].second;
    }

    TreeNode*& operator[](int key) {
        return return_TreeNode(key);
    }

    pair<int, TreeNode*>* find(int key) {
        int idx = find_index(key);
        if (idx == -1) return nullptr;
        return &v[idx];
    }

    pair<int, TreeNode*>* end() {
        return nullptr;
    }
};


class Files{
    private:
    // File Structure
    TreeNode* root; // Your implementation of the tree
    TreeNode* active_version;
    IntMap version_map; // Your implementation of the HashMap
    int total_versions;

    public:
    void create_file(){
        root = new TreeNode();
        root->message = "initial snapshot message";
        root->snapshot_timestamp = time(0);
        version_map.return_TreeNode(root->version_id) = root;
        total_versions = 0;
        active_version = root;
    }

    void read_version(){
        if (active_version == nullptr) {
            throw out_of_range("No active version");
        }
        if (active_version->content.empty()) {
            cout << "File is empty" << endl;
            return;
        }
        cout << active_version->content << endl;
    }
    
    void insert_content(string content1){
        if (active_version->snapshot_timestamp != 0) {
            TreeNode* new_version = new TreeNode();
            new_version->content = content1;
            new_version->parent = active_version;
            total_versions++;
            new_version->version_id = total_versions;
            new_version->last_modified_timestamp = time(0);
            new_version->created_timestamp = time(0);
            active_version->children.push_back(new_version);
            version_map.return_TreeNode(new_version->version_id) = new_version;
            active_version->last_modified_timestamp = time(0);
            active_version = new_version;

        } 
        else {
            active_version->content += content1;
            active_version->last_modified_timestamp = time(0);
        }
    }


    void update_content(string content1) {
        if (active_version->snapshot_timestamp != 0 || !active_version->message.empty()) {
            TreeNode* new_version = new TreeNode();
            new_version->content = content1;
            new_version->parent = active_version;
            total_versions++;
            new_version->version_id = total_versions;
            new_version->last_modified_timestamp = time(0);
            new_version->created_timestamp = time(0);

            active_version->children.push_back(new_version);
            version_map[new_version->version_id] = new_version;
            active_version->last_modified_timestamp = time(0);
            active_version = new_version;
        } else {
            active_version->content = content1;
            active_version->last_modified_timestamp = time(0);
        }
    }


    void en_snapshot(string message1){
        active_version->message = message1;
        active_version->snapshot_timestamp = time(0) ;
        active_version->last_modified_timestamp = time(0);
    }

    void rollback(int version_id1 = -1) {
        if (version_id1 == -1) {
            if (active_version->parent)
                active_version = active_version->parent;
            else
                cout << "No parent to rollback to." << endl;
        } else {
            if (version_map.find(version_id1) != version_map.end())
                active_version = version_map[version_id1];
            else
                cout << "Invalid version ID." << endl;
        }
    }

    
    void history() {
        TreeNode* temp = active_version;
        while(temp != nullptr) {
            if (temp->snapshot_timestamp != 0) {
                cout << "ID: " << temp->version_id << endl;
                cout << "Timestamp: " << temp->snapshot_timestamp << endl;
                cout << "Message: " << temp->message << endl;
            }
            temp = temp->parent;
        }
    }

    int num_vers() const{
        return total_versions;
    }

    void modify_timestamp(){
        active_version->last_modified_timestamp = time(0);
    }

    time_t get_last_modified_timestamp() const{
        return active_version->last_modified_timestamp;
    }
};


class StringMap {
public:
    struct Element {
        string key;
        Files value;
        Element(const string& k, const Files& v) : key(k), value(v) {}
    };

private:
    vector<vector<Element>> table; // buckets
    size_t count;                  // total number of elements
    size_t capacity;               // number of buckets
    const double load_factor = 0.75;

    // A simple polynomial rolling hash
    size_t hashString(const string& s) const {
        const size_t P = 131;       // base prime
        const size_t MOD = 1000000007ULL; // large mod
        size_t h = 0;
        for (char c : s) {
            h = (h * P + static_cast<unsigned char>(c)) % MOD;
        }
        return h;
    }

    // Resize and rehash when load factor exceeded
    void rehash() {
        size_t new_capacity = capacity * 2;
        vector<vector<Element>> new_table(new_capacity);

        for (auto& bucket : table) {
            for (auto& elem : bucket) {
                size_t idx = hashString(elem.key) % new_capacity;
                new_table[idx].push_back(elem);
            }
        }

        table.swap(new_table);
        capacity = new_capacity;
    }

public:
    class iterator {
        using bucket_iterator = vector<Element>::iterator;
        using table_iterator = vector<vector<Element>>::iterator;

        table_iterator tbl_end;
        table_iterator tbl_it;
        bucket_iterator bkt_it;

        void advance_to_valid() {
            while (tbl_it != tbl_end && bkt_it == tbl_it->end()) {
                ++tbl_it;
                if (tbl_it != tbl_end) bkt_it = tbl_it->begin();
            }
        }

    public:
        iterator(table_iterator t_end, table_iterator t_it, bucket_iterator b_it)
            : tbl_end(t_end), tbl_it(t_it), bkt_it(b_it) {
            advance_to_valid();
        }

        Element& operator*() { return *bkt_it; }
        Element* operator->() { return &(*bkt_it); }

        bool operator==(const iterator& other) const {
            return tbl_it == other.tbl_it && (tbl_it == tbl_end || bkt_it == other.bkt_it);
        }
        bool operator!=(const iterator& other) const { return !(*this == other); }

        iterator& operator++() {
            ++bkt_it;
            advance_to_valid();
            return *this;
        }
    };

    // Constructor
    StringMap(size_t initial_capacity = 8)
        : count(0), capacity(initial_capacity) {
        table.resize(capacity);
    }

    iterator begin() {
        return iterator(table.end(), table.begin(),
                        table.empty() ? vector<Element>::iterator() : table[0].begin());
    }

    iterator end() {
        return iterator(table.end(), table.end(), vector<Element>::iterator());
    }

    // Find key, return iterator or end
    iterator find(const string& key) {
        size_t idx = hashString(key) % capacity;
        for (auto it = table[idx].begin(); it != table[idx].end(); ++it) {
            if (it->key == key) {
                return iterator(table.end(), table.begin() + idx, it);
            }
        }
        return end();
    }

    // Insert or update
    void insert(const string& key, const Files& val) {
        size_t idx = hashString(key) % capacity;

        for (auto& elem : table[idx]) {
            if (elem.key == key) {
                elem.value = val; // update
                return;
            }
        }

        table[idx].emplace_back(key, val);
        ++count;

        // Check load factor
        if ((double)count / capacity > load_factor) {
            rehash();
        }
    }

    // Behaves like operator[] in unordered_map
    Files& at(const string& key) {
        size_t idx = hashString(key) % capacity;

        for (auto& elem : table[idx]) {
            if (elem.key == key) return elem.value;
        }

        // Key not found, insert default
        table[idx].emplace_back(key, Files());
        ++count;

        if ((double)count / capacity > load_factor) {
            rehash();
            // recompute index after rehash
            idx = hashString(key) % capacity;
            for (auto& elem : table[idx]) {
                if (elem.key == key) return elem.value;
            }
        }
        return table[idx].back().value;
    }

    size_t size() const { return count; }
    bool empty() const { return count == 0; }
};

int main(){
    StringMap files1;
    string line;
    vector<string> time_order;

    while (getline(cin, line)) {
        if (line.empty()) continue;

        stringstream ss(line);
        string command;
        ss >> command;

        if (command == "CREATE") {
            string filename;
            ss >> filename;
            Files new_file;
            new_file.create_file();
            if (files1.find(filename) == files1.end()) {
                files1.insert(filename, new_file);
                cout << "File '" << filename << "' created" << endl;
            }
            else {
                cout << "File '" << filename << "' already exists" << endl;
            }
            time_order.push_back(filename);
        }
        else if (command == "READ")
        {
            string filename;
            ss >> filename;

            if (files1.find(filename) == files1.end()) {
                cout << "File '" << filename << "' not found" << endl;
                continue;
            }
            try {
                files1.at(filename).read_version();
            } catch (const out_of_range& e) {
                cout << "File '" << filename << "' not found" << endl;
            }
        }

        else if (command == "INSERT") {
            string filename;
            ss >> filename;
            string content;
            getline(ss, content);
            if (!content.empty() && content[0] == ' ')
                content = content.substr(1);
            if (files1.find(filename) == files1.end()) {
                cout << "File '" << filename << "' not found" << endl;
                continue;
            }
            try {
                files1.at(filename).insert_content(content);
                files1.at(filename).modify_timestamp();
            } catch (const out_of_range& e) {
                cout << "File '" << filename << "' not found" << endl;
            }
            time_order.push_back(filename);
        }
        else if (command == "UPDATE") {
            string filename;
            ss >> filename;
            string content;
            getline(ss, content);
            if (!content.empty() && content[0] == ' ')
                content = content.substr(1);
            if (files1.find(filename) == files1.end()) {
                cout << "File '" << filename << "' not found" << endl;
                continue;
            }
            try {
                files1.at(filename).update_content(content);
                files1.at(filename).modify_timestamp();
            } catch (const out_of_range& e) {
                cout << "File '" << filename << "' not found" << endl;
            }
            time_order.push_back(filename);
        }
        else if (command == "SNAPSHOT") {
            string filename;
            ss >> filename;
            string message;
            getline(ss, message);
            if (!message.empty() && message[0] == ' ')
                message = message.substr(1);
            if (files1.find(filename) == files1.end()) {
                cout << "File '" << filename << "' not found" << endl;
                continue;
            }
            try {
                files1.at(filename).en_snapshot(message);
                files1.at(filename).modify_timestamp();
            } catch (const out_of_range& e) {
                cout << "File '" << filename << "' not found" << endl;
            }
            time_order.push_back(filename);
        }
        else if (command == "ROLLBACK") {
            string filename;
            ss >> filename;
            int version_id = -1;
            if (!(ss >> version_id)) {
                cout << "Invalid version ID." << endl;
                version_id = -1;
                continue;
            }

            if (files1.find(filename) == files1.end()) {
                cout << "File '" << filename << "' not found" << endl;
                continue;
            }

            try {
                files1.at(filename).rollback(version_id);
            } catch (const out_of_range& e) {
                cout << "File '" << filename << "' not found" << endl;
            }
            time_order.push_back(filename);
        }
        else if (command == "HISTORY") {
            string filename;
            ss >> filename;
            if (files1.find(filename) == files1.end()) {
                cout << "File '" << filename << "' not found" << endl;
                continue;
            }
            try {
                files1.at(filename).history();
            } catch (const out_of_range& e) {
                cout << "File '" << filename << "' not found" << endl;
            }
        }
        //lists files in descending order of their last modification timestamp
        else if (command == "RECENT_FILES") {
            int num;
            ss >> num;
            TimePriorityQueue recent_files;
            vector<string> reversed(time_order.rbegin(), time_order.rend());
            vector<string> seen;
            for (const auto& [filename, file] : files1) {
                for (int i = 0 ; i < reversed.size(); i++) {
                    if (reversed[i] == filename) {
                        recent_files.push(i, filename);
                        break;
                    }
                }
            }
            
            while(!recent_files.empty()) {
                seen.push_back(recent_files.top().second);
                recent_files.pop();
            }
            if (num > seen.size()) {
                cout << "Invalid number" << endl;
                continue;
            }
            for (int i = num-1; i >= 0; i--) {
                cout << seen[i] << " ";
            }
            cout << endl;
        }
        // Lists files in descending order of their total version count.
        else if (command == "BIGGEST_TREES"){
            int num;
            ss >> num;
            IntPriorityQueue biggest_trees;
            for (const auto& [filename, file] : files1) {
                biggest_trees.push(file.num_vers(), filename);
            }
            vector<string> final_list;
            while(!biggest_trees.empty()) {
                final_list.push_back(biggest_trees.top().second);
                biggest_trees.pop();
            }
            if (num > final_list.size()) {
                cout << "Invalid number" << endl;
                continue;
            }
            for (int i = 0; i < num; i++) {
                cout << final_list[i] << " ";
            }
            cout << endl;
        }
        else if (command == "END"){
            break;
        }
        else {
            cout << "Unknown command " << endl;
        }
    }
    return 0;
}


