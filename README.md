# Exhaustive Search for Independent Set

This repository contains a Python implementation of exhaustive search algorithms for finding independent sets in graphs.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

An **independent set** in a graph is a set of vertices with no two adjacent. Finding the largest independent set is a classic problem in combinatorial optimization and graph theory, known to be NP-hard.

This project provides a Python implementation to enumerate all independent sets or find the maximum independent set using exhaustive (brute-force) search methods. It is intended for educational and experimental purposes.

## Features

- Enumerate all independent sets in a given graph
- Find the maximum (largest) independent set
- Simple API for custom graphs
- Pure Python implementation for easy understanding and modification

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/davidetoniatti/exhaustive-search-independent-set.git
   cd exhaustive-search-independent-set
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
   > If there is no `requirements.txt`, all dependencies are included in the standard library.

## Usage

You can use the main script to find independent sets in a graph. Example usage:

```python
from <your_module> import find_maximum_independent_set

# Define your graph (adjacency list or edge list)
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

max_set = find_maximum_independent_set(graph)
print("Maximum Independent Set:", max_set)
```

Replace `<your_module>` with the actual module name from the repository.

Alternatively, you can run the script directly:

```bash
python main.py
```

Check the code comments and function docstrings for more details.

## Project Structure

```
exhaustive-search-independent-set/
├── main.py
├── utils.py
├── README.md
└── (other source files)
```

- `main.py`: Entry point, example usage
- `utils.py`: Utility functions for graph handling

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
