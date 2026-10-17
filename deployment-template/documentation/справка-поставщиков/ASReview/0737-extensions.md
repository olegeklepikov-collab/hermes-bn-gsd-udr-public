> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ASReview: extensions

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# Developing Extensions

ASReview extensions enable you to integrate your programs with the ASReview framework seamlessly by using the Python API. These extensions fall into three different categories and interact with the API in different ways.

1.  [Model extensions](#model-extensions)
2.  [Subcommand extensions](#subcommand-extensions)
3.  [Dataset extensions](#dataset-extensions)

The extensibility of the framework is provided by the entry points of setuptools. You will need to create a package and install it (for example, with pip).

Did you develop a useful extension to ASReview and want to list it on [the Discussion platform](https://github.com/asreview/asreview/discussions/1140)? Leave a message there, and we will add it to the list of extensions.

For more information on the ASReview API for creating an extension, a technical reference for development is found under the `reference/asreview`. This technical reference contains functions for use in your extension and an overview of all classes to extend.

## Model Extensions

Model extensions extend the ASReview software with new classifiers, query strategies, balance strategies, or feature extraction techniques. Model extensions are Python packages that can be installed in the ASReview environment. Model extensions typically inherit from the `sklearn.base.BaseEstimator` class in Scikit-learn or have a similar interface. The model extensions can be used in the ASReview LAB and via the Command Line Interface (CLI).

The easiest way to extend ASReview with a model is by using the <a href="https://github.com/asreview/template-extension-new-model"
target="_blank"> template for extending ASReview</a>. Create a copy of the template and add the new algorithm to a new model file. It is advised to use the following structure of the package:

``` bash
├── README.md
├── asreviewcontrib
│   └── models
│       ├── classifiers.py
│       ├── feature_extractors.py
│       ├── balancers.py
│       └── queriers.py
└── tests
```

The next step is to add metadata to the `pyproject.toml` file. Edit the `name` of the package and point the `entry-points` to the models.

``` toml
[project]

name = "asreviewcontrib-yourmodel"

[project.entry-points."asreview.models.classifiers"]

example = "asreviewcontrib.models.classifiers.example_model:ExampleClassifier"

[project.entry-points."asreview.models.feature_extractors"]

# define feature_extraction algorithms

[project.entry-points."asreview.models.balancers"]

# define balance_strategy algorithms

[project.entry-points."asreview.models.queriers"]

# define query_strategy algorithms
```

This code registers the model with name `example`.

## Subcommand Extensions

Subcommand extensions are programs that create a new entry point for ASReview. From this entry point the Python API can be used in many ways (like `plot` or `simulate`).

Extensions in ASReview are Python packages and can extend the subcommands of asreview (see `asreview -h`). An example of a subcommand extension is [ASReview Insights](https://github.com/asreview/asreview-insights).

The easiest way to create a new subcommand is by defining a function or class with <span class="title-ref">execute</span> method that can be used as a new entry point for ASReview.

``` python
class ExampleEntryPoint:

    def execute(self, argv):
        pass  # Implement your functionality here.
```

The class method `execute` accepts a positional argument (`argv` in this example). The argument `argv` are the command line arguments for your subcommand.

It is advised to place the newly defined entry point in the following package structure: `asreviewcontrib.{extension_name}.{your_modules}`. For example:

``` bash
├── README.md
├── asreviewcontrib
│   └── example
│       ├── __init__.py
│       ├── entrypoint.py
│       └── example_utils.py
├── pyproject.toml
└── tests
```

Create a `pyproject.toml` in the root of the package, and define the entry points under `[project.entry-points."asreview.entry_points"]`, for example:

``` toml
[project] name = "asreviewcontrib-example"

# ...other metadata...

[project.entry-points."asreview.entry_points"]

example = "asreviewcontrib.example.entrypoint:ExampleEntryPoint"
```

After installing this package, ASReview is extended with the `asreview example` subcommand. See `asreview -h` for this option.

## Dataset Extensions

An extension of the `asreview.datasets.BaseDataSet` class.

Dataset extensions integrate new datasets for use in ASReview. Adding datasets via extension provides quick access to the dataset via Command Line Interface or in ASReview LAB.

It is advised to place the new dataset `your_dataset` in the following package structure:

``` bash
├── README.md
├── asreviewcontrib
│   └── dataset_name
│       ├── __init__.py
│       └── your_dataset.py
├── data
│   └── your_dataset.csv
├── pyproject.toml
└── tests
```

For minimal functionality, `your_dataset.py` should extend `asreview.datasets.BaseDataSet` and `asreview.datasets.BaseDataGroup`.

A working template to clone and use can be found at [Template for extending ASReview with a new dataset](https://github.com/asreview/template-extension-new-dataset).

Further functionality can be extensions of any other class in `asreview.datasets`.
