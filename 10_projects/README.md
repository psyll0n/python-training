# Projects

Complete projects, games, and GUI applications. This section contains fully functional programs demonstrating multiple Python concepts working together.

## 📂 Contents

### [Simple Games](./simple_games/)
Text-based and simple games for learning and fun.

#### Classic Games
- **rock_paper_scissors.py** - Classic hand game
  - User input, random choices
  - Conditional logic for win/loss/tie
  - Score tracking

- **tick_tack_toe_game.py** - Tic-tac-toe (Noughts and Crosses)
  - 2D list for game board
  - Win condition checking
  - Player turns

- **hangman/** - Word guessing game
  - String manipulation
  - List operations
  - ASCII art display
  - Lives system

#### Card Games
- **blackjack/** - Casino card game (21)
  - Card deck implementation
  - Player and dealer logic
  - Hit/stand decisions
  - Scoring system

#### Dice and Random Games
- **dice_roller.py** - Simulate rolling dice
  - Random number generation
  - Multiple dice support
  - ASCII dice faces

- **coinTossGame.py** - Coin flip simulator
  - Random choice
  - Statistics tracking
  - Probability demonstration

- **random_number_game.py** - Number guessing game
  - Random target number
  - User input validation
  - Guess feedback (higher/lower)
  - Attempt counter

#### Puzzle Games
- **bagels_game.py** - Number deduction game (Pico, Fermi, Bagels)
  - Logic puzzle
  - Clue system
  - Deductive reasoning

- **guessing_game/** - Enhanced guessing game
  - Difficulty levels
  - Hint system
  - High score tracking

- **higher_lower/** - Number comparison game
  - Compare values
  - Social media follower counts
  - Score system

#### Adventure Games
- **treasure_island.py** - Text adventure game
  - Multiple choice paths
  - Branching storyline
  - Conditional outcomes
  - ASCII art

#### Other Games
- **fantasy_game_inventory.py** - RPG inventory system
  - Dictionary for items
  - Add/remove items
  - Display inventory
  - Item management

- **randomQuizGenerator.py** - Auto-generated quizzes
  - Random question selection
  - Answer shuffling
  - File I/O for questions
  - Score calculation

- **zigzag_example.py** - ASCII animation
  - Time delays
  - Pattern generation
  - Animation loops

**Concepts Demonstrated:**
- User input and validation
- Random number generation
- Conditional logic
- Loops and iteration
- Data structures (lists, dictionaries)
- Functions and modular code
- ASCII art and formatting

---

### [Tkinter](./tkinter/)
GUI applications using Python's built-in Tkinter library.

**Tkinter Basics:**
- Windows and frames
- Buttons, labels, entries
- Event handling
- Layout managers (pack, grid, place)
- Canvas for drawing
- Message boxes

**Common Tkinter Widgets:**
- Button, Label, Entry
- Text, Listbox, Canvas
- Menu, Frame, Toplevel
- Checkbutton, Radiobutton
- Scale, Scrollbar

**Example Structure:**
```python
import tkinter as tk

root = tk.Tk()
root.title("My App")

label = tk.Label(root, text="Hello!")
label.pack()

button = tk.Button(root, text="Click", command=callback)
button.pack()

root.mainloop()
```

---

### [Turtle Graphics](./turtle_graphics/)
Graphics and animation projects using the Turtle module.

**Turtle Graphics Basics:**
- Drawing shapes
- Moving the turtle
- Colors and fills
- Screen setup
- Event handling

**Common Turtle Commands:**
```python
import turtle

t = turtle.Turtle()
t.forward(100)  # Move forward
t.right(90)     # Turn right
t.circle(50)    # Draw circle
t.color('red')  # Set color
t.begin_fill()  # Start fill
t.end_fill()    # End fill
```

**Projects:**
- Drawing shapes and patterns
- Animation
- Interactive graphics
- Games using turtle graphics

---

## 🎯 Project Complexity Levels

### Beginner Projects 🟢
- **rock_paper_scissors.py** - Basic conditionals and random
- **dice_roller.py** - Random generation and functions
- **coinTossGame.py** - Simple probability
- **random_number_game.py** - Loops and input validation

### Intermediate Projects 🟡
- **hangman/** - String manipulation, lists, game logic
- **tick_tack_toe_game.py** - 2D arrays, win checking
- **fantasy_game_inventory.py** - Dictionaries, CRUD operations
- **treasure_island.py** - Complex branching logic

### Advanced Projects 🔴
- **blackjack/** - OOP, game state management, multiple players
- **randomQuizGenerator.py** - File I/O, randomization, data processing
- **Tkinter apps** - GUI programming, event handling
- **Turtle games** - Graphics, animation, user interaction

## 💡 Tips for Building Projects

### Planning
1. **Define requirements** - What should the program do?
2. **Break it down** - Divide into smaller tasks
3. **Sketch the flow** - Draw flowcharts or pseudocode
4. **Start simple** - Basic version first, add features later

### Best Practices
```python
# Use functions to organize code
def main():
    """Main game loop"""
    setup_game()
    while playing:
        take_turn()
    end_game()

# Separate concerns
def get_user_input():
    """Handle all input with validation"""
    pass

def update_game_state():
    """Update game logic"""
    pass

def display_output():
    """Handle all output/display"""
    pass
```

### Game Development Pattern
```python
# 1. Initialize game state
score = 0
lives = 3
playing = True

# 2. Game loop
while playing:
    # Display current state
    show_board()
    
    # Get player input
    action = get_input()
    
    # Process action
    result = process_action(action)
    
    # Update state
    update_state(result)
    
    # Check win/loss conditions
    if check_win():
        playing = False
    if check_loss():
        playing = False

# 3. End game
show_final_score()
```

### Input Validation
```python
def get_valid_input(prompt, valid_options):
    """Get input with validation"""
    while True:
        response = input(prompt).lower()
        if response in valid_options:
            return response
        print(f"Invalid input. Choose from {valid_options}")
```

## 🎮 Game Development Concepts

### Core Components
1. **Game State** - Current condition (score, lives, board)
2. **Game Loop** - Main execution cycle
3. **Input Handling** - Process player actions
4. **Game Logic** - Rules and mechanics
5. **Output/Display** - Show game state
6. **Win/Loss Conditions** - Game ending logic

### Common Patterns
- **Turn-based** - Players alternate (chess, tic-tac-toe)
- **Real-time** - Continuous action (snake, pong)
- **Menu-driven** - Selection-based (text adventures)
- **Event-driven** - React to events (GUI games)

## 🛠️ Extending Projects

### Add Features
- **High scores** - Save and load best scores
- **Difficulty levels** - Easy, medium, hard
- **Multiple players** - Turn-based or simultaneous
- **Statistics** - Track wins, losses, averages
- **Sound effects** - Using pygame or winsound
- **Graphics** - Upgrade from text to GUI

### Save/Load System
```python
import json

def save_game(filename, game_state):
    """Save game state to file"""
    with open(filename, 'w') as f:
        json.dump(game_state, f)

def load_game(filename):
    """Load game state from file"""
    with open(filename, 'r') as f:
        return json.load(f)
```

## 📚 Learning Outcomes

By completing these projects, you'll learn:
- ✅ Combining multiple Python concepts
- ✅ User input handling and validation
- ✅ Game logic and state management
- ✅ Error handling and edge cases
- ✅ Code organization and structure
- ✅ Testing and debugging
- ✅ GUI programming (Tkinter)
- ✅ Graphics and animation (Turtle)
- ✅ File I/O for persistence
- ✅ Object-oriented design

## 🚀 Next Steps

1. **Complete existing projects** - Run and modify them
2. **Add features** - Enhance with your own ideas
3. **Create new games** - Apply learned concepts
4. **Share your work** - Get feedback from others
5. **Study game frameworks** - Pygame, Arcade, Godot
