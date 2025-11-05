#include "header.cpp"

#ifndef CODE_CPP
#define CODE_CPP

class SocialNet{
private:
    unordered_map<string, list<string>> friends;
    unordered_map<string, AVL> posts;

    string notcs(string s){
        string s1 = "";
        for (char c : s){
            s1 += tolower(c);
        }
        return s1;
    }

    pair<int,string> inlist( string s, list<pair<int,string>> l){
        for (auto i : l){
            if (i.second == s) return i;
        }
        return {-1, ""};
    }

    
public:
    void add_user(string username){
        string s1 = notcs(username);
        if (friends.find(s1) != friends.end()){
            cout << "user " << username << " exists" << endl;
            return;
        }
        else{
            list<string> l1;
            friends[s1] = l1;
            AVL abc = AVL();
            posts[s1] = abc;
        }

    }

    void add_friend(string u1, string u2){
        string s1 = notcs(u1);
        string s2 = notcs(u2);

        if (friends.find(s1) == friends.end()){
            cout << "user " << u1 << " does not exist" << endl;
            return;
        }
        if (friends.find(s2) == friends.end()){
            cout << "user " << u2 << " does not exist" << endl;
            return;
        }

        if (find(friends[s1].begin(), friends[s1].end(), s2) != friends[s1].end()){
            cout << "already " << s1 << " and " << s2 << " are friends" << endl;
            return;
        }

        friends[s1].push_front(s2);
        friends[s2].push_front(s1);

    }

    void list_friends(string u1){
        string s = notcs(u1);
        
        if (friends.find(s) == friends.end()){
            cout << "user " << u1 << " does not exist" << endl;
            return;
        }

        list<string> l = friends[s];
        l.sort();
        cout << "list of friends of " << s << "are: "<< endl;
        for (string s1 : l){
            cout << s1 << " ";
        }
        cout << endl;

    }

    void suggest_friends(string u, int n) {
        if (n == 0) return;

        string s = notcs(u);

        if (friends.find(s) == friends.end()){
            cout << "user " << u << " does not exist" << endl;
            return;
        }

        list<string> fr_u = friends[s];
        unordered_set<string> fr_set(fr_u.begin(), fr_u.end());
        unordered_map<string, int> suggestion_count;

        for (string s1 : fr_u) {
            for (string x : friends[s1]) {
                suggestion_count[x]++;
            }
        }

        vector<pair<int, string>> v;
        for (auto ele : suggestion_count) {
            if (fr_set.count(ele.first) || ele.first == s) continue;
            v.push_back({ele.second, ele.first});
        }

        sort(v.begin(), v.end(), []( pair<int, string> a,pair<int, string> b) {
            if (a.first != b.first)
                return a.first > b.first; 
            return a.second < b.second;
        });

        int siz = min(n, int(v.size()));
        cout << siz << " suggested friends for " << s << ": ";
        for (int i = 0; i < siz; ++i) {
            cout << v[i].second << (i < siz - 1 ? " " : "");
        }
        cout << endl;
    }


    int degrees_of_separation(string u1, string u2){
        string s1 = notcs(u1);
        string s2 = notcs(u2);

        if (friends.find(s1) == friends.end()){
            cout << "user " << u1 << " does not exist" << endl;
            return -1;
        }
        if (friends.find(s2) == friends.end()){
            cout << "user " << u2 << " does not exist" << endl;
            return -1;
        }

        queue<pair<string, int>> q;
        map<string, bool> visited;
        q.push({s1, 0});
        visited[s1] = true;
        while(!q.empty()){
            pair<string, int> curr = q.front();
            q.pop();
            if (curr.first == s2){
                return curr.second;
            }
            for (string neighbor : friends[curr.first]){
                if (!visited[neighbor]){
                    visited[neighbor] = true;
                    q.push({neighbor, curr.second + 1});
                }
            }
        }
        return -1;
    }

    void add_post( string s, string c){
        string s1 = notcs(s);
        string c1 = notcs(c);

        if (posts.find(s1) == posts.end()){
            cout << "user " << s << " does not exist" << endl;
            return;
        }

        posts[s1].insert(c1);
    }

    void output_posts(string s, int n){
        string s1 = notcs(s);

        if (posts.find(s1) == posts.end()){
            cout << "user " << s << " does not exist" << endl;
            return;
        }

        vector<string> v = posts[s1].inorder_traversal();
        reverse(v.begin(), v.end()); 
        int size = n;
        if (n == -1 || n > v.size()) size = v.size();
        cout << "posts: "<< endl;

        for (int i = 0; i < size; i++){
            cout << v[i] << endl;
        }
        cout << endl;
    }
};

#endif