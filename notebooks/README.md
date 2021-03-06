# SUDS notebooks
This folder contains experimental notebooks for the SUDS projects. Code here may end up as part of the SUDS platform.

## Activating
This project relies on [Poetry](https://python-poetry.org/) for dependency management. 

Make sure Poetry is [installed on your operating system](https://python-poetry.org/docs/#installation) and then run the following command from within this project directory.

```
poetry shell
```

## Installation
After activating the project virtual environment, run the following command to install the dependencies.

```
poetry install
```

### Note on RTREE dependency
If you get an error to the effect of `undefined symbol: Error_GetLastErrorNum` when installing dependencies, make sure that `libspatialindex-dev` is installed on your computer. On Ubuntu Linux, use the following command to install `libspatialindex-dev`

```
sudo apt install libspatialindex-dev
```

## Running
Once the dependencies are installed, you can run the JupyterLab project in order to access these notebooks.

```
jupyter lab
```