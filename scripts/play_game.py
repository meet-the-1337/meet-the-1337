#!/usr/bin/env python3
"""
Interactive Game Engine for GitHub Profile README (Connect Four / Tic-Tac-Toe).
Executes player moves from GitHub Issues, computes AI minimax response,
and updates the README.md game board.
"""

import os
import sys
import json
import random

README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")
STATE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "game_state.json")

def load_state():
    if os.path.exists(STATE_PATH):
        try:
            with open(STATE_PATH, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "board": [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        "turn": "human",
        "human_symbol": "⚔️", # Cross / Sword
        "ai_symbol": "🤖",    # Bot
        "last_player": "None",
        "status": "in_progress",
        "wins_human": 14,
        "wins_ai": 22,
        "draws": 8
    }

def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def check_winner(board):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] != " " and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    if " " not in board:
        return "draw"
    return None

def minimax(board, depth, is_maximizing, ai_sym, human_sym):
    winner = check_winner(board)
    if winner == ai_sym:
        return 10 - depth
    elif winner == human_sym:
        return depth - 10
    elif winner == "draw":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = ai_sym
                score = minimax(board, depth + 1, False, ai_sym, human_sym)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = human_sym
                score = minimax(board, depth + 1, True, ai_sym, human_sym)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def find_best_move(board, ai_sym, human_sym):
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = ai_sym
            score = minimax(board, 0, False, ai_sym, human_sym)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def render_board_markdown(state, username="GITHUB_USERNAME"):
    board = state["board"]
    h_sym = state["human_symbol"]
    a_sym = state["ai_symbol"]
    winner = check_winner(board)

    # Base URL for moves
    def cell_link(idx):
        val = board[idx]
        if val != " ":
            return f"&nbsp;{val}&nbsp;"
        if winner is not None:
            return "&nbsp;⬜&nbsp;"
        issue_url = f"https://github.com/{username}/{username}/issues/new?title=game%7Cmove%7C{idx}&body=Just+click+%27Submit+new+issue%27+to+play+your+move+at+position+{idx}+against+the+AI+bot!"
        return f'<a href="{issue_url}"><b>[🟢 Play]</b></a>'

    status_msg = ""
    if winner == h_sym:
        status_msg = f"🏆 **YOU WON!** 🎉 The AI was outsmarted! (<a href='https://github.com/{username}/{username}/issues/new?title=game%7Creset&body=Submit+to+reset+the+board!'>Click to Restart</a>)"
    elif winner == a_sym:
        status_msg = f"💀 **AI WINS!** 🤖 The neural net calculated your defeat! (<a href='https://github.com/{username}/{username}/issues/new?title=game%7Creset&body=Submit+to+reset+the+board!'>Click to Rematch</a>)"
    elif winner == "draw":
        status_msg = f"🤝 **DRAW GAME!** Stalemate reached. (<a href='https://github.com/{username}/{username}/issues/new?title=game%7Creset&body=Submit+to+reset+the+board!'>Click to Play Again</a>)"
    else:
        status_msg = f"⚔️ **YOUR TURN** • Click any empty cell below to make a move against the AI! (Last player: `{state['last_player']}`)"

    table_md = f"""<!-- GAME_BOARD:START -->
<div align="center">

### 🎮 Battle The AI • Live Tic-Tac-Toe

{status_msg}

| Column 1 | Column 2 | Column 3 |
| :---: | :---: | :---: |
| {cell_link(0)} | {cell_link(1)} | {cell_link(2)} |
| {cell_link(3)} | {cell_link(4)} | {cell_link(5)} |
| {cell_link(6)} | {cell_link(7)} | {cell_link(8)} |

```
📊 LEADERBOARD: Human Wins: {state['wins_human']}  |  AI Bot Wins: {state['wins_ai']}  |  Draws: {state['draws']}
```
<p>
  <a href="https://github.com/{username}/{username}/issues/new?title=game%7Creset&body=Submit+to+start+a+fresh+game!"><b>[ 🔄 Reset Board ]</b></a>
</p>

</div>
<!-- GAME_BOARD:END -->"""
    return table_md

def update_readme_game(username="GITHUB_USERNAME"):
    state = load_state()
    board_md = render_board_markdown(state, username)

    if not os.path.exists(README_PATH):
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = "<!-- GAME_BOARD:START -->"
    end_tag = "<!-- GAME_BOARD:END -->"

    if start_tag in content and end_tag in content:
        before = content.split(start_tag)[0]
        after = content.split(end_tag)[1]
        new_content = before + board_md + after
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ README.md game board updated successfully.")

def handle_issue_move(issue_title, player_name, username="GITHUB_USERNAME"):
    state = load_state()
    tokens = issue_title.strip().split("|")

    if len(tokens) >= 2 and tokens[1] == "reset":
        state["board"] = [" "] * 9
        state["status"] = "in_progress"
        state["last_player"] = player_name
        save_state(state)
        update_readme_game(username)
        return "Game reset! Your move."

    if len(tokens) >= 3 and tokens[1] == "move":
        try:
            pos = int(tokens[2])
        except ValueError:
            return "Invalid position."

        if check_winner(state["board"]) is not None:
            return "Game is already finished! Please reset."

        if 0 <= pos <= 8 and state["board"][pos] == " ":
            # Player move
            state["board"][pos] = state["human_symbol"]
            state["last_player"] = player_name

            # Check if human won
            winner = check_winner(state["board"])
            if winner == state["human_symbol"]:
                state["wins_human"] += 1
                state["status"] = "human_won"
            elif winner == "draw":
                state["draws"] += 1
                state["status"] = "draw"
            else:
                # AI move
                ai_move = find_best_move(state["board"], state["ai_symbol"], state["human_symbol"])
                if ai_move is not None:
                    state["board"][ai_move] = state["ai_symbol"]
                    ai_winner = check_winner(state["board"])
                    if ai_winner == state["ai_symbol"]:
                        state["wins_ai"] += 1
                        state["status"] = "ai_won"
                    elif ai_winner == "draw":
                        state["draws"] += 1
                        state["status"] = "draw"

            save_state(state)
            update_readme_game(username)
            return f"Move registered at position {pos}! Check README."
    return "Ignored."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "render":
            user = sys.argv[2] if len(sys.argv) > 2 else "GITHUB_USERNAME"
            update_readme_game(user)
        elif cmd == "issue":
            title = sys.argv[2]
            player = sys.argv[3] if len(sys.argv) > 3 else "Visitor"
            user = sys.argv[4] if len(sys.argv) > 4 else "GITHUB_USERNAME"
            res = handle_issue_move(title, player, user)
            print(res)
    else:
        update_readme_game()
