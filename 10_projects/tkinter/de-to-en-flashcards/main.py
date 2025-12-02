#!/usr/bin/env python3
"""
German-English Flashcard Application

A simple flashcard application built with Tkinter to help users learn German vocabulary.
The application displays German words and their English translations using a flip-card
mechanism, allowing users to track their learning progress.
"""

import random
from tkinter import *
import pandas as pd
import os

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
CARD_FLIP_TIME = 3000  # Time in milliseconds before card flips
FONT_NAME = "Arial"


class FlashcardApp:
    """
    A class to manage the German-English flashcard application.

    Attributes:
        current_card (dict): Currently displayed flashcard data
        flip_timer: Reference to the current timer for card flipping
        words_to_learn (list): List of word pairs to learn
    """

    def __init__(self):
        """Initialize the flashcard application and set up the UI."""
        self.current_card = {}
        self.flip_timer = None
        self.load_word_data()
        self.setup_ui()
        self.next_card()

    def load_word_data(self):
        """
        Load vocabulary data from CSV file.
        First tries to load from words_to_learn.csv, falls back to german_words.csv if not found.

        The method will:
        1. First try to load words_to_learn.csv if it exists
        2. If that fails, try to load german_words.csv
        3. If both fail, initialize an empty list
        4. Print appropriate debug messages
        """
        words_to_learn_path = "./data/words_to_learn.csv"
        german_words_path = "./data/german_words.csv"

        # Debug print to check working directory and file existence
        print(f"Current working directory: {os.getcwd()}")
        print(f"words_to_learn.csv exists: {os.path.exists(words_to_learn_path)}")
        print(f"german_words.csv exists: {os.path.exists(german_words_path)}")

        try:
            # First try to load words_to_learn.csv
            if os.path.exists(words_to_learn_path):
                data = pd.read_csv(words_to_learn_path)
                if not data.empty:
                    print(
                        f"Successfully loaded {len(data)} words from words_to_learn.csv"
                    )
                    self.words_to_learn = data.to_dict(orient="records")
                    return
                else:
                    print("words_to_learn.csv is empty, trying german_words.csv")

            # If words_to_learn.csv doesn't exist or is empty, try german_words.csv
            if os.path.exists(german_words_path):
                data = pd.read_csv(german_words_path)
                if not data.empty:
                    print(
                        f"Successfully loaded {len(data)} words from german_words.csv"
                    )
                    self.words_to_learn = data.to_dict(orient="records")
                    return
                else:
                    print("german_words.csv is empty")

            # If we get here, neither file was successfully loaded
            print("No valid word list files found")
            self.words_to_learn = []

        except pd.errors.EmptyDataError:
            print("Error: CSV file is empty")
            self.words_to_learn = []
        except pd.errors.ParserError as e:
            print(f"Error parsing CSV file: {e}")
            self.words_to_learn = []
        except Exception as e:
            print(f"Unexpected error loading word data: {e}")
            self.words_to_learn = []

    def remove_word(self):
        """
        Remove the current word from the learning list and save the updated list.
        Called when user marks a word as known.
        """
        if not self.words_to_learn:
            print("No words available to remove")
            return

        try:
            self.words_to_learn.remove(self.current_card)
            # Save updated word list to CSV
            df = pd.DataFrame(self.words_to_learn)
            if not df.empty:
                df.to_csv("./data/words_to_learn.csv", index=False)
                print(f"Successfully saved {len(df)} words to words_to_learn.csv")
            self.next_card()
        except ValueError:
            print(f"Warning: Could not remove word from list")
        except Exception as e:
            print(f"Error saving words_to_learn.csv: {e}")

    def next_card(self):
        """
        Display a new random German word and schedule its flip to English.
        Cancels any existing flip timer before showing new card.
        """
        if self.flip_timer:
            self.window.after_cancel(self.flip_timer)

        if not self.words_to_learn:
            self.canvas.itemconfig(self.card_title, text="Status")
            self.canvas.itemconfig(self.card_word, text="No words available")
            print("No words available to display")
            return

        self.current_card = random.choice(self.words_to_learn)
        self.canvas.itemconfig(self.card_title, text="German", fill="black")
        self.canvas.itemconfig(
            self.card_word, text=self.current_card["german"], fill="black"
        )
        self.canvas.itemconfig(self.card_background, image=self.flashcard_front_img)
        self.flip_timer = self.window.after(CARD_FLIP_TIME, self.flip_card)

    def flip_card(self):
        """Flip the card to show the English translation."""
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(
            self.card_word, text=self.current_card["english"], fill="white"
        )
        self.canvas.itemconfig(self.card_background, image=self.flashcard_back_img)

    def setup_ui(self):
        """Set up the user interface components."""
        # Main window configuration
        self.window = Tk()
        self.window.title("German - English Flashcards")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        # Canvas setup
        self.canvas = Canvas(width=800, height=526)
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Load images
        self.flashcard_front_img = PhotoImage(file="./images/card_front.png")
        self.flashcard_back_img = PhotoImage(file="./images/card_back.png")
        self.wrong_img = PhotoImage(file="./images/wrong.png")
        self.right_img = PhotoImage(file="./images/right.png")

        # Create canvas elements
        self.card_background = self.canvas.create_image(
            400, 263, image=self.flashcard_front_img
        )
        self.card_title = self.canvas.create_text(
            400, 150, text="", font=(FONT_NAME, 30, "italic")
        )
        self.card_word = self.canvas.create_text(
            400, 263, text="", font=(FONT_NAME, 60, "bold")
        )

        # Create buttons
        self.unknown_button = Button(
            image=self.wrong_img, highlightthickness=0, command=self.next_card
        )
        self.unknown_button.grid(row=1, column=0)

        self.known_button = Button(
            image=self.right_img,
            highlightthickness=0,
            command=self.remove_word,  # Changed from next_card to remove_word
        )
        self.known_button.grid(row=1, column=1)

    def run(self):
        """Start the application's main event loop."""
        self.window.mainloop()


if __name__ == "__main__":
    app = FlashcardApp()
    app.run()
