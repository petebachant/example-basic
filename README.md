# Basic Calkit example

## How this was setup

1. Created a repo on GitHub.
2. Imported into [Calkit](https://calkit.io).
3. Ran `dvc init` and committed changes.
4. Ran `calkit new question "Can we make reproducibility simple?" --commit`.
5. `dvc stage add -n collect-data -o data/raw/data.csv -d scripts/collect-data.py`
6. Ran `dvc repro`, then `git add .` and `git commit -m ...` and `dvc push`
   to get everything up to the cloud.
6. Added a script and DVC stage to create a figure, similar to the two steps
   above.
7. Added the figure to `calkit.yaml` by editing the `figures` section manually.
