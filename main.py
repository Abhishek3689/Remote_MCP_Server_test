from fastmcp import FastMCP
from datetime import datetime
import requests
import random

mcp = FastMCP(name="Play_puzzle")

@ mcp.tool
def generate_puzzle(puzzle_type: str = "random"):
    """
    Generates a random puzzle.
    puzzle_type can be: "word", "number", or "random".
    """

    # ---------------------
    # WORD SCRAMBLE PUZZLE
    # ---------------------
    def word_scramble():
        words = ["machine", "python", "context", "learning", "puzzle", "galaxy"]
        word = random.choice(words)
        scrambled = ''.join(random.sample(word, len(word)))
        return f"🔤 **Word Scramble Puzzle**\nUnscramble this word:\n\n👉 `{scrambled}`"
        

    # ---------------------
    # NUMBER SEQUENCE PUZZLE
    # ---------------------
    def number_sequence():
        sequences = [
            ([2, 4, 6, 8], "Next is 10"),
            ([3, 9, 27, 81], "Next is 243"),
            ([5, 10, 20, 40], "Next is 80"),
        ]
        seq, answer = random.choice(sequences)
        seq_text = ", ".join(map(str, seq)) + ", ?"
        return f"🔢 **Number Sequence Puzzle**\nFind the next number:\n\n👉 `{seq_text}`\n"
        

    # Pick puzzle category
    if puzzle_type == "word":
        return word_scramble()
    elif puzzle_type == "number":
        return number_sequence()
    else:
        return random.choice([word_scramble(), number_sequence()])

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)