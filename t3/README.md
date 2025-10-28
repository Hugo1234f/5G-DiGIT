# Prerequisites

## Libraries

To run these scripts you need to install the following libraries:
    
1. numpy (v1.x)
2. scikit-learn
3. matplotlib
4. pandas

You can install them like this:

```
pip install "numpy<2"
pip install scikit-learn
pip install matplotlib
pip install pandas
```

## Data

The experiemnt evalues the **5G - Passive Measurements.csv** (2.2GB) dataset available [here](https://zenodo.org/records/8224890). This file should be placed into the `./data/` directory and renamed to `RawData.csv`.
It is possible to change the required filename in [**isolate_campaign.py**](https://github.com/Hugo1234f/5G-DiGIT/blob/main/t3/isolate_campain.py)

# Running the experiment

The experiment is run in this order:

1. isolate_campaign.py
2. scale_cont.py
3. train.py
    * plot.py
    * anomaly_desc.py