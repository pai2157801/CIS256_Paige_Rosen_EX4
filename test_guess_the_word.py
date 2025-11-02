# Paige Rosen
# CIS 256 Fall 2025
# 2 Nov 25
# Ex 4 test - Github
import sys
import importlib
import pytest

MODULE = "guess_the_word"

def load_game(monkeypatch, forced_state: str):
    # Ensure import won't block on input: immediately quit the loop
    monkeypatch.setattr("builtins.input", lambda *_: "q")
    # Make the chosen state deterministic
    monkeypatch.setattr("random.choice", lambda _: forced_state)
    # Fresh import
    if MODULE in sys.modules:
        del sys.modules[MODULE]
    game = importlib.import_module(MODULE)
    return game

def reset_tracking(game):
    game.guessed_right = []
    game.guessed_wrong = []
    if hasattr(game, "matching_letters"):
        game.matching_letters.clear()
    if hasattr(game, "letters_complete"):
        game.letters_complete = False
    if hasattr(game, "game_won"):
        game.game_won = False

def test_selected_word_is_from_list(monkeypatch):
    game = load_game(monkeypatch, "Texas")
    assert game.chosen_state in game.STATES
    assert game.chosen_state == "Texas"

def test_guesses_processed_correct_vs_incorrect(monkeypatch):
    game = load_game(monkeypatch, "Texas")
    reset_tracking(game)

    # Correct guess
    monkeypatch.setattr("builtins.input", lambda *_: "t")
    game.is_a_letter()
    assert "t" in game.guessed_right
    assert "t" not in game.guessed_wrong
    if hasattr(game, "matching_letters"):
        assert "t" in game.matching_letters

    # Incorrect guess
    monkeypatch.setattr("builtins.input", lambda *_: "b")  # not in 'Texas'
    game.is_a_letter()
    assert "b" in game.guessed_wrong
    assert "b" not in game.guessed_right
    if hasattr(game, "matching_letters"):
        assert "b" not in game.matching_letters