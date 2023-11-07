from __future__ import annotations

from typing import TYPE_CHECKING, Iterator

from whist_backend import WhistEventListener

if TYPE_CHECKING:
    from whist_backend import Bet, Card, Suit
    from whist_backend.round_simulator import _Player


class PrinterEventListener(WhistEventListener):
    """A simple example WhistEventListener that prints information about game events."""

    def notify_round_start(
        self,
        revealed_card: Card,
        trump_suit: Suit,
        hand_size: int,
        players: list[_Player],
    ) -> None:
        print(
            f"REVEALED CARD: {revealed_card} "
            + f"(trump suit {trump_suit}, hand size {hand_size})"
        )
        print("PLAYERS:")
        for player in players:
            print(player)
        print()

    def notify_card_played(self, player: _Player, played_card: Card) -> None:
        print(
            f"{player.strategy.name} played {played_card} "
            f"(remaining cards {','.join(map(str, player.hand))})."
        )

    def notify_trick_won(self, player: _Player) -> None:
        print(f"{player.strategy.name} won the trick!")
        print()

    def notify_bets_made(self, bets: Iterator[tuple[_Player, Bet]]) -> None:
        print("BETS:")
        for player, bet in bets:
            print(f"{player.strategy.name}: {bet}")
        print()

    def notify_new_trick(self, player_id: int) -> None:
        print(f"A new trick is starting with {player_id}")
