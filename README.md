# Basic Calkit example

This is a basic Calkit example project,
which includes data collection,
figure generation,
and LaTeX article compilation,
all part of a single reproducible DVC pipeline.

You can also view this project on [calkit.io](https://calkit.io/calkit/example-basic).

This project can be reproduced with

```sh
calkit run
```

Note that the data collection stage has some randomness built into it,
so it should run the first time,
but will be cached after that.

## Steps to recreate

1. Create a new project on [calkit.io](https://calkit.io).
1. `calkit new question "Can we make reproducibility simple?"`.
1. Create a Conda environment with 
   `calkit new conda-env -n calkit-example-basic python matplotlib numpy pandas`.
1. Create the data collection stage with:
    ```sh
    dvc stage add -n collect-data \
        -o data/raw/data.csv -d \
        scripts/collect-data.py \
        "calkit runenv -n calkit-example-basic -- python scripts/collect-data.py"
    ```
1. `calkit run && git add . && calkit save -am "Run pipeline"`
1. Add a script and DVC stage to create a figure, similar to the two steps
   above.
1. Add the figure and dataset to `calkit.yaml` by editing the `figures`
   and `datasets` section manually.
1. Create a new LaTeX publication and Docker environment using the 
   `latex/article` template.
   See the 
   [docs](https://github.com/calkit/calkit/blob/main/docs/tutorials/adding-latex-pub-docker.md).
