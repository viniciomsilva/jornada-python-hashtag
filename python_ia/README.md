# 🧠 Python IA | Artificial Intelligence and Predictions

You've been hired by a bank to determine its customers' credit scores.  
You need to analyze the bank's entire customer database and, based on it, create
an AI model that can determine a new customer's credit score based on their
data, such as: **Bad**; **Regular**; **Good**.

---

\[pt_BR\] Você foi contrato por um banco para conseguir definir o score de
crédito dos clientes.  
Você precisa analisar toda a base de dados de clientes do banco e, com base
nela, criar um modelo de IA que consiga definir o score de crédito do novo
cliente com base nos dados dele como: **Poor**; **Regular**; **Good**.

## Library Installation

By shell:

```shell
pip install pandas scikit-learn
```

By Jupyter Notebook:

```python
%pip install pandas scikit-learn
```

> NOTE: If the installation of all requirements by the ` requirements.txt ` has
> already been done file, no longer need to install.

## Data Preprocessing

In data preprocessing, understanding the challenge and the institution behind it
shapes the filters for the most acceptable results. In this case, the model that
best predicts customers' credit scores with an accuracy between 80% and 100% is
the most appropriate.

**Project steps:**

1. Import the libraries and database
2. Prepare the database for AI
3. Create the AI ​​models and train them to predict customers' credit scores
4. Choose the best model (the one with the most accurate score)
5. Use this model to make new predictions

### #1 Import Libs and Databases

**Databases:**  
Since all databases are in the ` ../data/ ` directory, you need to resolve the
path for Pandas.

* Customer data for AI training (` clients.csv ` file)
* New customer data for AI credit score prediction (` new_clients.csv ` file)

**IA Models:**  
In AI projects, it's always best to train more than one model simultaneously for
comparison and to select the best model without bias.

**Libs:**  

* Pandas: processes data from CSV files into a Python structure
* Scikit Learn
  * Label Encoder: treat non-numeric data as numeric, the only formats accepted by AI models ([see documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder))
  * KNeighbors Classifier: AI model that classifies a customer's credit score based on customers with similar characteristics, their "neighbors" ([see documentation](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier))
  * Random Forest Classifier: AI model that ranks customer scores based on random analysis of other customer information ([see documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier))
  * Train Test Split *Method*: a method that divides the database into training data and test data, which are then further divided into analysis data and template data ([see documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split))
  * Accuracy Score *Method*: a method that calculates the accuracy of the AI ​​model by comparing its response to the test analysis data with the test template ([see documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score))

### #2 Prepare the Database for AI (Label Encoder)

Preparing data for AI involves encoding non-numeric data into numeric data, as
AI can only perform calculations with numeric data (obviously). To do this, you
use the Label Encoder, which is responsible for encoding and decoding the data.

The "profissao," "mix_credito," and "comportamento_pagamento" columns are object
types in the database. Therefore, an encoder is created for each of them.

```python
profession_coder = LabelEncoder()  # "profissao" column coder
credit_mix_coder = LabelEncoder()  # "mix_credito" column coder
payment_behavior_coder = LabelEncoder()  # "comportamento_pagamento" column coder
```

Each encoder creates a "map" of the original data to the numeric value. It is
from this mapping that the data can be easily transformed and reversed.
Therefore, the Label Encoder process is practical.

**Example:**

| professional value | transform(obj) -> num | invert(num) -> obj |
| :----------------: | :-------------------: | :----------------: |
| cientista          |  1                    | cientista          |
| professor          |  2                    | professor          |
| ...                |  ...                  | ...                |
| desenvolvedor      |  n                    | desenvolvedor      |

```py
# column "profissao" receives the original encoded value
df["profissao"] = profession_coder.fit_transform(df["profissao"])  # transforme the value of the "profissao" column from object to number
# column "mix_credito" receives the original encoded value
df["mix_credito"] = credit_mix_coder.fit_transform(df["mix_credito"])  # transforme the value of the "mix_credito" column from object to number
# column "comportamento_pagamento" receives the original encoded value
df["comportamento_pagamento"] = payment_behavior_coder.fit_transform(df["comportamento_pagamento"])  # transforme the value of the "comportamento_pagamento" column from object to number
```

### #3 Prepare the Database for AI (Train Test Split Database)

Before starting to train AI models, the database needs to be divided.

**How ​​Will this Division Work?**  
For a better understanding, the database can be imagined as a Cartesian plane
with an X and Y axes. In this analogy, the X information will be used to predict
the Y values. X and Y will be divided again into two parts: X and Y for training
and X and Y for testing. Thus, the following structure is obtained:

* Training X: information that the AI ​​will use to predict the training Y values
* Training Y: template information to train the AI's accuracy
* Test X: information that, after training, will be used to determine the test Y values
* Test Y: information to measure the AI ​​model's accuracy and determine the best model for the project

**Who X and Y Are?**

* Y is the column you want to predict
* X are all other columns relevant to predicting Y

```python
y = df["score_credito"]  # column "score_credito" that the AI ​​should predict
X = df.drop(columns=["id_cliente", "score_credito"])  # all other columns except "id_cliente" and "score_credito"
```

**Separate Into Training and Test Data:**

1. Training X to predict training Y
2. Training Y to train the AI
3. Test X to predict test Y
4. Test Y to measure the AI's prediction accuracy

```python
X_train, X_test, y_train, y_test = train_test_split(X, y)  # test_size default = 0.25
```

> NOTE: Y data does not need to go through the LabelEncoder process.  
> NOTE: The ideal size of data reserved for testing should be between
> 20% and 30%.

## Instantiate and Train AI Models

With the models imported, it's time to instantiate and train them. In each
model's constructor, you can pass various calibration parameters. However, in
this project, the models were used with the default calibration.

```python
clf = RandomForestClassifier()  # random forest classification model
neigh = KNeighborsClassifier()  # nearest neighbor classification model
```

Here the training is done automatically, passing to each training model X and Y.

```python
clf.fit(X=X_train, y=y_train)  # fits the random classification model
neigh.fit(X=X_train, y=y_train)  # fits the nearest neighbor classification model
```

## Choose the best AI model

The model with the best accuracy in predicting customers' credit scores will be
chosen.

To calculate this, the model will attempt to predict the test value of Y using
the test value of X. Its response will be stored. Then, the AI ​​prediction is
compared with the original test value of Y, thus calculating its success rate.

```python
# the model predicts using X test
pred_clf = clf.predict(X=X_test)
pred_neigh = neigh.predict(X=X_test)

# calculate the accuracy of each model by comparing its prediction with the test Y value
accuracy_score(y_test, pred_clf)
accuracy_score(y_test, pred_neigh)
```

**In these circumstances:**

* The random forest classification model had an accuracy of 83% (*chosen*)
* The nearest neighbor classification model had an accuracy of 75%

For this project, both are good values. But there's nothing stopping you from
improving the model or testing others.

## Use the Chosen Model for New Predictions

To use the chosen model to make new predictions, you need to follow the same
steps as before regarding data processing. After processing the data, it can be
used to calculate the credit scores of new customers.

> NOTE: Here there is no way to separate the data into X and Y, as there is no
> Y. It is what will be discovered.
