# Knight Battle Game

## Start Game
* Run the command below to start the game.
```
python game.py
```

## Explaination of the game design
* **Steps**
    1. Generate **Arena** object.
    2. Setup **`Knight`** and **`Item`** chess.
    3. Read instructions from moves.txt
    4. An instruction is a **round**
        * **Move** knight, check **drowned** or alived
        * Knight try to **pickup** a equipment.
        * Knight try to **battle**, winner kill loser.
        * Print map
    5. Generate **`final_state.json`** file.

## Chess, Knight, Item Class
* The **Chess** class is a base class for all kinds of chess.
* **`Knight`** inherited from `Chess`.
