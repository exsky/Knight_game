# Knight Battle Game

## Start Game without Docker
* Run the command below to start the game.
If you don't have the Docker environment, you can run the game directly.

```
cd src
python game.py
```

## Run in Docker
I also provide the Dockerfile that you can run the game directly.
```
make build
make game
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
