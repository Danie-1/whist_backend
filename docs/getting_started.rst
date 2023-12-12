Getting Started
===============

#. Install the package:

   .. code-block:: bash

      pip install whist-backend

#. Create a sequence of objects that implement the
   :py:class:`~whist_backend.player_strategy_protocol.PlayerStrategy` protocol.

#. Pass the sequence to :py:class:`~whist_backend.round_simulator.RoundSimulator`, and
   call :py:meth:`~whist_backend.round_simulator.RoundSimulator.play_round` on it.

See :ref:`example_usage` for an example of this process.
