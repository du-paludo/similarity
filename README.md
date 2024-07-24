# Graph Similarity Estimation

This project implementsa two different methods, one approximate and another precise, to calculate the similarity between nodes in a graph using the NetworkX library. The similarities are calculated based on the common neighbors of each pair of nodes.

## Files

- `similarity_estimation.py`: Contains the implementation of the `similarity_estimation` function and an example using a random graph.
- `similarity.py`: Contains the implementation of the `similarity` function and an example using a random graph.

## Functions

### `similarity_estimation(G)`

Estimates the similarity between pairs of nodes in the graph `G` using a probabilistic approach.

- **Parameters:**
  - `G`: A NetworkX graph.

- **Returns:**
  - `S`: A dictionary where the keys are frozensets representing pairs of nodes and the values are the estimated similarities.

#### Explanation

1. **Initialization:**
   - Create a dictionary `S` to store similarity scores for each pair of nodes.
   - Create a dictionary `signal_array` to keep track of sampled pairs.

2. **Main Loop:**
   - For each node in the graph, iterate through its neighbors.
   - For each neighbor, randomly sample a subset of nodes and check for common and total neighbors.
   - Update the similarity scores in `S` based on the common neighbors.

3. **Final Calculation:**
   - Calculate the final similarity scores by dividing the number of common neighbors by the total neighbors for each pair of nodes.

### `similarity(G)`

Estimates the similarity between pairs of nodes in the graph `G` using a deterministic approach.

- **Parameters:**
  - `G`: A NetworkX graph.

- **Returns:**
  - `S`: A dictionary where the keys are tuples representing pairs of nodes and the values are the similarities.

#### Explanation

1. **Initialization:**
   - Create a dictionary `S` to store similarity scores for each pair of nodes.

2. **Main Loop:**
   - For each pair of nodes, calculate the number of common neighbors.
   - Calculate the similarity score based on the number of common neighbors divided by the total number of neighbors.

## Usage

### Prerequisites

- Python 3.x
- NetworkX library

### Installation

Install the NetworkX library using pip:

`pip install networkx`

### Execution

Run the code using python3:

`python3 clustering-coefficient.py`
