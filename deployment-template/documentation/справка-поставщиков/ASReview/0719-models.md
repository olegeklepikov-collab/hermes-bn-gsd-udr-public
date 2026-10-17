> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

> Актуальный порядок для слоя 16.10.2026: см. CURRENT-SETUP.md в корне. Подписанные исходные спецификации сохраняют свои исходные версии; локальные переопределения заданы отдельно.

# Справка ASReview: models

Сохранённая внешняя документация. Копия адаптирована для переносимости: локальные пути и демонстрационные реквизиты/объекты заменены параметрами; содержимое не является конфигурацией готового аккаунта. Она описывает продукты, версии и варианты доступа, а не состояние какого-либо аккаунта. Примеры ОС, тарифов, путей и лимитов выбираются по целевой установке; числовые условия проверяются у поставщика перед использованием. Даты и исходная терминология могут относиться к версии справки.

---


# AI Models

AI models in ASReview LAB are the driving force behind efficient and accurate systematic reviews. By learning from your decisions, these models prioritize the most relevant records, significantly reducing the time and effort required for your review process. Whether you're working with single-language datasets, multilingual data, or need advanced semantic understanding, ASReview offers a range of models tailored to your needs.

Each model is built from a combination of components—feature extractors, classifiers, queriers, and balancers—that work together to optimize the review process. You can choose from pre-configured models for simplicity or customize your own for greater flexibility. This guide will help you understand the available models and how to select the best one for your use case.

> [!TIP]
> Not sure where to start? The ELAS u4 model is a great choice for most users. It's fast, efficient, and performs well across a variety of datasets. It's available by default in ASReview LAB.

## ELAS Models

The ELAS models in ASReview LAB are pre-configured AI models designed to cater to a variety of systematic review needs. Whether you need a fast and efficient model, one that handles multilingual datasets, or a model with advanced semantic understanding, the ELAS series has you covered. Each model is built from a combination of components—feature extractors, classifiers, queriers, and balancers—that work together to optimize the review process.

All ELAS models are active learning models. This means they iteratively learn from your labeling decisions and dynamically adjust their predictions to prioritize the most relevant records. Active learning ensures that the review process becomes more efficient over time, focusing on the records that are most likely to be relevant.

<table>
<caption>Model Overview</caption>
<thead>
<tr>
<th>Model</th>
<th>Short name</th>
<th>Description</th>
<th>Requires</th>
</tr>
</thead>
<tbody>
<tr>
<td>ELAS Ultra</td>
<td>u-series</td>
<td>Rapid and excellent-performing model for most use cases.</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td>ELAS Multilingual</td>
<td>l-series</td>
<td>Designed for multilingual datasets.</td>
<td><code class="interpreted-text" role="doc">dory</code>, <code class="interpreted-text" role="ref">Hardware Requirements &lt;lab/models:Hardware Requirements&gt;</code></td>
</tr>
<tr>
<td>ELAS Heavy</td>
<td>h-series</td>
<td>Focuses on semantic understanding of text.</td>
<td><code class="interpreted-text" role="doc">dory</code>, <code class="interpreted-text" role="ref">Hardware Requirements &lt;lab/models:Hardware Requirements&gt;</code></td>
</tr>
</tbody>
</table>

For most users, the pre-configured ELAS models are sufficient. However, if you want more control, you can create custom models by mixing and matching components. This flexibility allows you to tailor the AI model to your specific dataset and research goals. Custom models can combine components from both ASReview and the `dory` extension, offering advanced options for those with more technical expertise.

### ELAS Ultra

The ELAS Ultra AI model in ASReview LAB is the default and most widely used model. It is designed for speed and efficiency, making it ideal for most systematic review tasks. The model leverages "classic" machine learning techniques, which are lightweight and reliable. These techniques are implemented using components from the SciKit-learn library, ensuring robust performance.

Key features of ELAS Ultra:

- **Speed**: Processes data quickly, making it suitable for large datasets.
- **Efficiency**: Balances performance and resource usage, ensuring smooth operation on most systems.
- **Versatility**: Performs well across a wide range of datasets and use cases.

The following table outlines the components of the ELAS Ultra model for its various versions:

| Model   | Feature Extractor     | Classifier  | Querier | Balancer |
|---------|-----------------------|-------------|---------|----------|
| ELAS u4 | TF-IDF (with bigrams) | SVM         | Maximum | Balanced |
| ELAS u3 | TF-IDF                | Naive Bayes | Maximum | Balanced |

ELAS Ultra versions

> [!NOTE]
> While the components of ELAS Ultra models may appear similar across versions, differences in their underlying parameters can significantly impact their performance and behavior. Use the latest version (e.g., ELAS u4) for the best results.

Use ELAS Ultra if you are looking for a reliable, fast, and easy-to-use model that works well for most systematic review scenarios.

### ELAS Multilingual

The ELAS Multilingual models are specifically designed for datasets containing multiple languages. These models leverage advanced multilingual feature extractors. They are ideal for systematic reviews involving multilingual datasets, where other ELAS models may struggle with language-specific texts and nuances.

Key features of ELAS Multilingual:

- **Multilingual Support**: Handles datasets with multiple languages seamlessly, supporting over 100 languages.
- **Advanced Feature Extraction**: Uses state-of-the-art multilingual feature extractors for better understanding of text.
- **Flexibility**: Suitable for a wide range of multilingual systematic review tasks.

Requirements for ELAS Multilingual:

- **Dory extension**: The ELAS Multilingual models require the `dory` extension for feature extraction. Install the extension using the following command: `pip install asreview-dory`.
- **Hardware**: These models are computationally intensive and may require significant CPU or GPU power to perform efficiently, especially with large datasets. See the section on `Hardware Requirements <lab/models:Hardware
  Requirements>` for more details.

The following table outlines the components of the ELAS Multilingual model for its various versions:

| Model   | Feature Extractor     | Classifier | Querier | Balancer |
|---------|-----------------------|------------|---------|----------|
| ELAS l2 | multilingual-e5-large | SVM        | Maximum | Balanced |

ELAS Multilingual versions

For more information about the <span class="title-ref">multilingual-e5-large</span> feature extractor, including its support for over 100 languages, visit the official documentation on Hugging Face: <https://huggingface.co/intfloat/multilingual-e5-large>.

### ELAS Heavy

The ELAS Heavy models are designed for tasks requiring advanced semantic understanding of text. These models utilize powerful feature extractors that focus on the underlying meaning of the text, making them ideal for systematic reviews where semantic context is crucial.

Key features of ELAS Heavy:

- **Semantic Understanding**: Focuses on the meaning of text rather than just word occurrences.
- **Advanced Feature Extraction**: Uses state-of-the-art feature extractors for deeper text analysis.
- **Ideal for Complex Reviews**: Suitable for datasets where semantic nuances play a significant role.

Requirements for ELAS Heavy:

- **Dory extension**: The ELAS Heavy models require the `dory` extension for feature extraction. Install the extension using the following command: `pip install asreview-dory`.
- **Hardware**: These models are computationally intensive and may require significant CPU or GPU power to perform efficiently, especially with large datasets. See the section on `Hardware Requirements <lab/models:Hardware
  Requirements>` for more details.

The following table outlines the components of the ELAS Heavy model for its various versions:

| Model   | Feature Extractor    | Classifier | Querier | Balancer |
|---------|----------------------|------------|---------|----------|
| ELAS h3 | mxbai-embed-large-v1 | SVM        | Maximum | Balanced |

ELAS Heavy versions

For more information about the <span class="title-ref">mxbai-embed-large-v1</span> feature extractor and its capabilities, refer to the official documentation provided in the ASReview Dory extension.

### Custom ELAS Models

Custom ELAS models allow you to tailor the AI model to your specific needs by combining different components. Each AI model in ASReview LAB is composed of four key components that work together to rank your remaining documents:

- **Querier**: Determines which records to show you next. For example, it can prioritize potentially relevant records, mix in random records, or use uncertainty-based strategies.
- **Feature Extractor**: Converts text into numerical features that the classifier can interpret.
- **Classifier**: Predicts the relevance of records based on your decisions using the numerical features created by the feature extractor.
- **Balancer**: Handles imbalanced data to improve learning accuracy and ensure robust performance.

The following components are available out of the box for creating custom models:

- **Feature Extractors**: <span class="title-ref">OneHot</span>, <span class="title-ref">TF-IDF</span>
- **Classifiers**: <span class="title-ref">Naive Bayes</span>, <span class="title-ref">Support Vector Machine</span>, <span class="title-ref">Random Forest</span>, <span class="title-ref">Logistic Regression</span>
- **Queriers**: <span class="title-ref">Maximum</span>, <span class="title-ref">Mixed (95% Maximum and 5% Random)</span>, <span class="title-ref">Mixed (95% Maximum and 5% Uncertainty)</span>, <span class="title-ref">Random</span>, <span class="title-ref">Top-down</span>, <span class="title-ref">Uncertainty</span>
- **Balancers**: <span class="title-ref">Balanced</span>

For advanced users, you can also integrate components from the `dory` extension, which provides access to more powerful feature extractors and classifiers:

- **ASReview Dory Feature Extractors**: <span class="title-ref">doc2vec</span>, <span class="title-ref">gtr-t5-large</span>, <span class="title-ref">labse</span>, <span class="title-ref">multilingual-e5-large</span>, <span class="title-ref">mxbai-embed-large-v1</span>, <span class="title-ref">sbert</span>
- **ASReview Dory Classifiers**: <span class="title-ref">AdaBoost</span>, <span class="title-ref">Neural Network - 2-Layer</span>, <span class="title-ref">Neural Network - Dynamic</span>, <span class="title-ref">Neural Network - Warm Start</span>, <span class="title-ref">XGBoost</span>

Tips for customization:

- Combining components from ASReview and Dory allows for highly flexible and powerful models. However, some feature extractors may not work with certain classifiers. For example, some Dory feature extractors cannot be combined with the ASReview Naive Bayes classifier.
- Experiment with different combinations to find the best fit for your dataset and research goals. You can use the simulation mode in ASReview LAB to evaluate the performance of different models before applying them to your actual dataset.
- Creating custom models requires some knowledge of how the components work. Start with simpler combinations and gradually explore more complex setups as you gain experience.

## Hardware Requirements

The hardware requirements for running AI models in ASReview LAB vary depending on the complexity of the model. The ELAS Ultra models are lightweight and can run efficiently on most modern systems, including laptops and desktops, without requiring specialized hardware. In contrast, the ELAS Multilingual and ELAS Heavy models utilize advanced machine learning techniques and feature extractors, making them computationally intensive. These models often require significant CPU or GPU power to perform efficiently, especially when working with large datasets.

For optimal performance, ELAS Multilingual and ELAS Heavy models are better suited for server installations or systems equipped with dedicated GPUs. If you plan to use these models, ensure that your hardware includes a multi-core processor with high clock speed and at least 16 GB of RAM. Some operating systems will also benefit from a modern GPU for faster processing. Running these models on underpowered hardware may result in slower performance, longer training times, and inefficient screening.

## Model Numbering

The ELAS models are numbered with a letter and a number. The letter indicates the type of model, and the number indicates the version. The latest version of each model type is always the one with the highest number. For example, the latest version of the Ultra model is denoted as ELAS uX, where X represents the highest available version number. Not all historical versions are available in ASReview LAB, but you can always use the latest version of the model.

## Changing Models

You can change the AI model used in your systematic review at any time. When you switch models, the new model will start training in the background. This process might take some time, depending on the size of your dataset and the complexity of the model. However, you can continue screening records without interruption while the new model is being trained.

To change the model, follow these steps:

1.  Go to the **Customize** section in ASReview LAB.
2.  Navigate to the **AI** card.
3.  Select the desired model from the list of available options.

Once the new model is trained, it will automatically take over and start prioritizing records based on its predictions. In the meantime, you can keep screening records as usual.

> [!NOTE]
> Switching to a more complex model, such as those requiring the ASReview Dory extension, may take longer to train.
