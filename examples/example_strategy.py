from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from whist_backend import Bet, PlayerStrategy

if TYPE_CHECKING:
    from whist_backend.cards import Card


class NoThinkingStrategy(PlayerStrategy):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_move(self, allowed_cards: list[Card]) -> Card:
        return allowed_cards[0]

    def make_bet(self, disallowed_bet: Optional[int] = None) -> Bet:
        return Bet(disallowed_bet + 1 if disallowed_bet is not None else 0, False)
