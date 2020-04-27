# La Cage Noire

Student project Sorbonne Paris 1 2020 objects intéractifs

## Installation

To install with [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/install/):

```bash
conda create --name cage python=3.7
conda activate cage
conda install -c conda-forge --file requirements-conda.txt
```

## Run

You will need three things:

* a microphone
* a separate (bluetooth) speaker
* a headset
* the files with the testimonies (do not rename them, put them in same folder as script.py)

You have to set:

* the headset as the main output in Preferences -> Sound -> Output (not the speaker)
* the microphone as main input in Preferences -> Sound -> Input

To run the project (after running installation instructions above):

```bash
conda activate cage
python script.py
```
