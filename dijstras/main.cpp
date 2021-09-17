#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <fstream>
#include <unordered_map>


class Game {
    public:
        int id;
        float Home;
        float Draw;
        float Away;
}; 

class Node {
    public:
        int m_id;
        Node* m_parent_node;
        Game* m_game;
        int m_action_from_parent;
        float m_current_cost;
        float m_tripples_left;
        float m_doubles_left;
        float m_singles_left;

        // Create constructor
        Node(int id, Node* parent_node, Game* game, int action_from_parent, float current_cost, float tripples_left, float doubles_left, float singles_left){
            m_id = id;
            m_parent_node = parent_node;
            m_game = game;
            m_action_from_parent = action_from_parent;
            m_current_cost = current_cost;
            m_tripples_left = tripples_left;
            m_doubles_left = doubles_left;
            m_singles_left = singles_left;
        }
};

// this is an structure which implements the
// operator overloading
struct CompareCurrentCost {
    bool operator()(Node* const& p1, Node* const& p2){
        return p1->m_current_cost <= p2->m_current_cost;
    };
};

// Read in games.json
std::vector<Game*> read_games(std::string file_name) {
    std::vector<Game*> games;
    std::vector<std::string> lines;

    std::ifstream file(file_name);
    if (file.is_open()) {
        std::string line;
        int curr_line = 0;
        int num_of_lines = 0;
        while (std::getline(file, line))
            lines.push_back(line);
        file.close();
    }

    int parameters_per_game = std::stoi(lines[0])+1;
    lines.erase(lines.begin());
    for (int i = 0; i < lines.size(); i+=parameters_per_game) {
        Game* game = new Game();
        game->id = std::stoi(lines[i]);
        game->Home = std::stof(lines[i+1]);
        game->Draw = std::stof(lines[i+2]);
        game->Away = std::stof(lines[i+3]);
        games.push_back(game);
    }
    games.push_back(new Game{(int)games.size() + 1, 1, 1, 1});

    return games;
}

void print_game(Game* a)
{
    std::cout << "Game_ID: " << a->id << "\n";
    std::cout << "HOME: " << a->Home << "\n";
    std::cout << "DRAW: " << a->Draw << "\n";
    std::cout << "AWAY: " << a->Away << "\n";
}

std::string decode(int a)
{
    if (a == 0)
        return "start";
    else if (a == 1)
        return "1X2";
    else if (a == 20)
        return "1X";
    else if (a == 21)
        return "12";
    else if (a == 22)
        return "X2";
    else if (a == 30)
        return "1";
    else if (a == 31)
        return "X";
    else if (a == 32)
        return "2";
    return "end";
}

void print_node(const Node* a)
{
    std::cout << "Node_ID: " << a->m_id << "\n";
    if (a->m_parent_node != nullptr) {
        std::cout << "Node_PARENT_ID: " << a->m_parent_node->m_id << "\n";
    } else {
        std::cout << "Node_PARENT_ID: " << "NULL" << "\n";
    }
    std::cout << decode(a->m_action_from_parent) << "\n";
    std::cout << "Node_CURRENT_COST: " << a->m_current_cost << "\n";
    std::cout << "Node_HEL_LEFT: " << a->m_tripples_left << "\n";
    std::cout << "Node_HALV_LEFT: " << a->m_doubles_left << "\n";
    std::cout << "Node_SPIK_LEFT: " << a->m_singles_left << "\n";
    print_game(a->m_game);
}


int main(){
    std::vector<Game*> games = read_games("out.txt");

    for (int i = 0; i < games.size()-1; i++) {
        print_game(games[i]);
        std::cout << "\n";
    }

    int curr_id = 0;
    float cost = 0;
    Node* curr_node = new Node(curr_id, nullptr, games[0], 0, 1, 1, 6, 6);
    std::priority_queue<Node*, std::vector<Node*>, CompareCurrentCost> pq;
    pq.push(curr_node);

    std::cout << "Running num of games: " << games.size()-1 << std::endl;
    while (!pq.empty()) {
        curr_node = pq.top(); pq.pop();

        // Are we at the end?
        if (curr_node->m_game->id == games.size()) break;

        // Add next nodes
        if (curr_node->m_tripples_left > 0) {
            cost = curr_node->m_game->Home + curr_node->m_game->Draw + curr_node->m_game->Away;
            pq.push(new Node(++curr_id, curr_node, games[curr_node->m_game->id], 1, curr_node->m_current_cost * cost, curr_node->m_tripples_left - 1, curr_node->m_doubles_left, curr_node->m_singles_left));
        }

        // Add all combinations of halvs
        if (curr_node->m_doubles_left > 0)
            for (int i = 0; i <= 2; i++)
            {
                if (i == 0) cost = curr_node->m_game->Home + curr_node->m_game->Draw;
                else if (i == 1) cost = curr_node->m_game->Home + curr_node->m_game->Away;
                else cost = curr_node->m_game->Draw + curr_node->m_game->Away;
                pq.push(new Node(++curr_id, curr_node, games[curr_node->m_game->id], 20+i, curr_node->m_current_cost * cost, curr_node->m_tripples_left, curr_node->m_doubles_left - 1, curr_node->m_singles_left));
            }

        // Add all combinations of spiks
        if (curr_node->m_singles_left > 0)
            for (int i = 0; i <= 2; i++)
            {
                if (i == 0) cost = curr_node->m_game->Home;
                else if (i == 1) cost = curr_node->m_game->Draw;
                else cost = curr_node->m_game->Away;
                pq.push(new Node(++curr_id, curr_node, games[curr_node->m_game->id], 30+i, curr_node->m_current_cost * cost, curr_node->m_tripples_left, curr_node->m_doubles_left, curr_node->m_singles_left - 1));
            }
    }

    std::vector<Node*> done;
    while (true) {
        done.push_back(curr_node);
        if (!curr_node->m_parent_node) break;
        curr_node = curr_node->m_parent_node;
    }
    
    // Write to 'out.txt' file
    std::ofstream out("out.txt");
    for (int i = done.size()-2; i >= 0; i--) {
        out << done[i]->m_game->id - 1 << ":";
        out <<decode(done[i]->m_action_from_parent) << "\n";
    }
}