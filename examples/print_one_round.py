"""Use the `whist_backend` module to make 5 simple bots play a round of whist."""

from __future__ import annotations

from typing import TYPE_CHECKING

from example_strategy import NoThinkingStrategy
from printing_event_listener import PrinterEventListener

from whist_backend import RoundSimulator

if TYPE_CHECKING:
    from whist_backend.player_strategy_protocol import PlayerStrategy

if __name__ == "__main__":
    strategies: list[PlayerStrategy] = [
        NoThinkingStrategy("Player 1"),
        NoThinkingStrategy("Player 2"),
        NoThinkingStrategy("Player 3"),
        NoThinkingStrategy("Player 4"),
        NoThinkingStrategy("Player 5"),
    ]
    round_simulator = RoundSimulator(
        strategies, event_listeners=[PrinterEventListener()]
    )
    results = round_simulator.play_round()
    for result in results:
        print(f"{result[0].name} won {result[1]} points.")
