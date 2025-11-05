#include "code.cpp"

int main(){
    SocialNet sn;
    string line;

    while(getline(cin, line)){
        if (line.empty()) continue;
        stringstream ss(line);
        string command;
        ss >> command;
        if (command == "END"){
            break;
        }
        if (command == "ADD_USER"){
            string username;
            ss >> username;
            sn.add_user(username);
        }
        else if (command == "ADD_FRIEND"){
            string u1, u2;
            ss >> u1 >> u2;
            sn.add_friend(u1, u2);
        }
        else if (command == "LIST_FRIENDS"){
            string u1;
            ss >> u1;
            sn.list_friends(u1);
        }
        else if (command == "SUGGEST_FRIENDS"){
            string u1;
            int n;
            ss >> u1 >> n;
            sn.suggest_friends(u1, n);
        }
        else if (command == "DEGREES_OF_SEPARATION"){
            string u1, u2;
            ss >> u1 >> u2;
            int degrees = sn.degrees_of_separation(u1, u2);
            if (degrees != -1)
                cout << "degrees of separation between " << u1 << " and " << u2 << "is: " << degrees << endl;
            else
                cout << "no connection found." << endl;
        }
        else if (command == "ADD_POST"){
            string user, content;
            ss >> user;
            getline(ss, content);
            sn.add_post(user, content);
        }
        else if (command == "OUTPUT_POSTS"){
            string user;
            int n;
            ss >> user >> n;
            sn.output_posts(user, n);
        }
    }
    return 0;
}