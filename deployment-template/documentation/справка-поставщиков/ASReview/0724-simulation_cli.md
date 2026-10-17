> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ASReview: simulation_cli

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Simulation via command line

ASReview LAB comes with a command line interface for simulating the performance of ASReview algorithm.

## Getting started

The simulation command line tool can be accessed directly like:

``` bash
asreview simulate MY_DATASET.csv -o MY_SIMULATION.asreview
```

This performs a simulation with the default active learning model, where `MY_DATASET.csv` is the path to the `lab/data_labeled:Fully labeled data` you want to simulate. The result of the simulation is stored, after a successful simulation, at `MY_SIMULATION.asreview` where `MY_SIMULATION` is the filename you prefer and the extension is `.asreview` (ASReview project file extension).

## Simulation progress

The progress of the simulation is given with two progress bars. The top one is used to count the number of relevant records found. The bottom one monitors the number of records labeled. By default (see `--n-stop`), the simulation stops once the the top progress bar reaches 100%.

``` bash
Relevant records found: 100%|█████████████████████████████████████████████████████████| 38/38 [00:04<00:00,  7.83it/s]
Records labeled       :   7%|███▊                                                  | 322/4544 [00:04<01:03, 66.37it/s]

Loss: 0.021
NDCG: 0.530
```

## Command line arguments for simulating

The command `asreview simulate --help` provides an overview of available arguments for the simulation. Each of the sections below describe the available arguments. The example below shows how you can set the command line arguments.

``` bash
asreview simulate MY_DATASET.csv -o MY_SIMULATION.asreview -q max_random
```

### Dataset

<div class="option">

dataset

Required. File path or URL to the dataset or one of the SYNERGY datasets.

</div>

You can also use one of the `SYNERGY dataset <lab/data_labeled:fully
labeled data>`. Use the following command and replace `DATASET_ID` by the dataset ID.

``` bash
asreview simulate synergy:DATASET_ID
```

For example:

``` bash
asreview simulate synergy:van_de_schoot_2018 -o myreview.asreview
```

### Active learning

<div class="option">

`--ai AI`  

The AI to simulate with. Default is `elas_u4`.

</div>

<div class="option">

`-c, --classifier CLASSIFIER`  

The classifier for active learning. Default is Naive Bayes (`nb`).

</div>

<div class="option">

`-q, --querier QUERIER`  

The querier for active learning. Default is Maximum (`max`).

</div>

<div class="option">

`-b, --balancer BALANCER`  

Data rebalancing strategy mainly for RNN methods. Helps against imbalanced datasets with few inclusions and many exclusions. Default is `balanced`.

</div>

<div class="option">

`-e, --feature-extractor FEATURE_EXTRACTOR`  

Feature extraction algorithm. Some combinations of feature extractors and classifiers are not supported or feasible. Default is TF-IDF (`tfidf`).

</div>

<div class="option">

`--seed SEED`  

Seed for the model (classifiers, balance strategies, feature extraction techniques, and query strategies).

</div>

<div class="option">

`--prior-seed PRIOR_SEED`  

Seed for selecting prior records if the `--prior-idx` option is not used. If the option `--prior-idx` is used with one or more indices, this option is ignored.

</div>

<div class="option">

`--embedding EMBEDDING_FP`  

File path of embedding matrix. Required for LSTM models.

</div>

### Prior knowledge

By default, the model initializes with no prior included or excluded records. You can set the number of priors by `--n-prior-included` and `--n-prior-excluded`. Alternatively, you can initialize your model with a specific set of starting papers using `--prior-idx` or `--prior-record-id` to select the indices or record IDs of the papers you want to start the simulation with.

The following options can be used to label prior knowledge:

<div class="option">

`--n-prior-included N_PRIOR_INCLUDED`  

Sample n prior included records. Only used when `--prior-idx` is not given. Default 0.

</div>

<div class="option">

`--n-prior-excluded N_PRIOR_EXCLUDED`  

Sample n prior excluded records. Only used when `--prior-idx` is not given. Default 0.

</div>

<div class="option">

--prior-idx \[PRIOR_IDX \[PRIOR_IDX ...\]\]

Prior indices by row number (row numbers start at 0).

</div>

<div class="option">

--prior-record-id \[PRIOR_RECORD_ID \[PRIOR_RECORD_ID ...\]\]

Prior indices by record ID.

</div>

### Simulation setup

<div class="option">

`--n-query N_QUERY`  

Number of records queried each query. Default 1.

</div>

<div class="option">

`--n-stop N_STOP`  

The number of label actions to simulate. If not set, simulation stops after the last relevant record is found. Use -1 to simulate all label actions.

</div>

<div class="option">

`--config-file CONFIG_FILE`  

Configuration file for the learning cycle.

</div>

### Results

<div class="option">

`--output OUTPUT, -o OUTPUT`  

Location to ASReview project file of simulation.

</div>

<div class="option">

`--verbose VERBOSE, -v VERBOSE`  

Verbosity level.

</div>

## Algorithms

The command line interface provides an easy way to get an overview of all available active learning model elements (classifiers, query strategies, balance strategies, and feature extraction algorithms) and their names for command line usage in ASReview LAB. The following command lists the available models:

``` bash
asreview algorithms
```

The command includes models added via `../technical/extensions`. See `../technical/extensions` for more information on developing new models and install them via extensions.

Use `pip install asreview-dory` to get access to all Dory models. The Dory extension contains a collection of New and Exciting MOdels.
