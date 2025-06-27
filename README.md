# CSINTSY-StateBasedModels

In partial fulfillment of the course CSINTSY, to create a state based model with both informed and uninformed algorithms.


# To Run:

---

(From Executable)

1. Open `main.exe` file.
2. The file will then prompt you to choose from either UCS Search or A* Search (1 or 2)
3. Choose Start State
4. Choose Goal State
5. The program will print the results through the terminal which will include: path found, nodes visited, nodes expanded, time taken for execution, current memory usage, peak memory usage, total distance, (for A*) estimated cost, heuristic cost, and actual cost.
6. The program will also provide a matplotlib visual representation of the path taken by the search algorithm where nodes and edges are highlighted for better visual aid.

---

(From VSCode Terminal)

*Note: This method allows for the user to add new nodes and edges based on the needs by adding onto the `positions` and `edges` data structure. Distance and Heuristic values are calculated automatically provided that we have enough nodes and edges for the graph.*

1. Same procedures as the Executable
2. This also allows the user to see the results on VSCode terminal without it clearing.
