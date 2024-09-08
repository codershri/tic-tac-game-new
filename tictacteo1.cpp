#include <iostream>
#include <vector>
#include <string>

using namespace std;

void printBoard(const vector<vector<char>> &board)
{
    for (const auto &row : board)
    {
        for (char cell : row)
        {
            cout << cell << " ";
        }
        cout << endl;
    }
}

bool isBoardFull(const vector<vector<char>> &board)
{
    for (const auto &row : board)
    {
        for (char cell : row)
        {
            if (cell == '.')
                return false;
        }
    }
    return true;
}

int evaluate(const vector<vector<char>> &board)
{
    for (int i = 0; i < 3; ++i)
    {
        if (board[i][0] != '.' && board[i][0] == board[i][1] && board[i][1] == board[i][2])
            return board[i][0] == 'X' ? 10 : -10;
        if (board[0][i] != '.' && board[0][i] == board[1][i] && board[1][i] == board[2][i])
            return board[0][i] == 'X' ? 10 : -10;
    }
    if (board[0][0] != '.' && board[0][0] == board[1][1] && board[1][1] == board[2][2])
        return board[0][0] == 'X' ? 10 : -10;
    if (board[0][2] != '.' && board[0][2] == board[1][1] && board[1][1] == board[2][0])
        return board[0][2] == 'X' ? 10 : -10;

    return 0;
}

bool makeMove(vector<vector<char>> &board, int row, int col, char player)
{
    if (board[row][col] == '.')
    {
        board[row][col] = player;
        return true;
    }
    return false;
}

bool isValidMove(int row, int col)
{
    return row >= 0 && row < 3 && col >= 0 && col < 3;
}

int main()
{
    vector<vector<char>> board(3, vector<char>(3, '.'));
    char currentPlayer = 'X';

    while (true)
    {
        printBoard(board);
        int row, col;
        cout << "Player " << currentPlayer << ", enter your move (row and column): ";
        cin >> row >> col;

        if (!isValidMove(row, col) || !makeMove(board, row, col, currentPlayer))
        {
            cout << "Invalid move. Try again." << endl;
            continue;
        }

        int result = evaluate(board);
        if (result == 10)
        {
            printBoard(board);
            cout << "Player X wins!" << endl;
            break;
        }
        else if (result == -10)
        {
            printBoard(board);
            cout << "Player O wins!" << endl;
            break;
        }
        else if (isBoardFull(board))
        {
            printBoard(board);
            cout << "It's a draw!" << endl;
            break;
        }

        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}
