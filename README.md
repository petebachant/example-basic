# Basic Calkit example

## How this was setup

1. Created a repo on GitHub.
2. Imported into [Calkit](https://calkit.io).
3. Ran `dvc init` and committed changes.
4. Ran `calkit new question "Can we make reproducibility simple?" --commit`.
5. `dvc stage add -n collect-data -o data/raw/data.csv -d scripts/collect-data.py`
