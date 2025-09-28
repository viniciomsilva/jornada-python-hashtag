# 📊 Python Insights | Analyzing data with Python

You were hired by a company with over 800,000 customers for a data analysis
project. Recently, this company realized that most of the customers in its
database are inactive, meaning they have already canceled their accounts.  
Needing to improve its results, it decided to understand the reasons behind
these cancellations and thus find the most efficient solutions to reduce this
number.

---

\[pt-BR\] Você foi contrato por uma empresa com mais de 800mil clientes para um
projeto de análise de dados. Recentemente esta empresa percebeu que no seu banco
de dados de clientes, a maioria são de clientes inativos, ou seja, que já
cancelaram o serviço.  
Precisando melhorar seus resultados, ela resolveu entender os motivos que levam
a esses cancelamentos, e assim, achar as soluções mais eficientes para reduzir
este número.

## Library Installation

By shell:

```shell
pip install pandas numpy openpyxl nbformat ipykernel plotly
```

By Jupyter Notebook:

```python
%pip install pandas numpy openpyxl nbformat ipykernel plotly
```

> NOTE: If the installation of all requirements by the ` requirements.txt ` has
> already been done file, no longer need to install.

## Data Analysis | Flow

1. Import libraries and database
2. View (understand) the database
3. Correct the database ant prepare it for analysis
4. See the actual number of cancellations
5. Show the relationship between cancellations and other data in visual graphs *(how does other data directly impact cancellations?)*
6. Implement viable solutions and show their numerical results in the number of cancellations

### #1 Flow | Import the Libs and Database

**Database:** comes from the ` cancellations.csv ` file.

**Libs:**

* Pandas: process CSV file data into a Python structure
* Plotly Express: create visual graphics

All project databases are located in ` ./data/ `. You must resolve the path
before opening any file with Pandas.

```python
path.join(path.dirname(getcwd()), "data", "cancellations.csv")  # ../data/cancellations.csv
```

### #2 Flow | View (Understand) the Database

Display the database data and the structural information of that data.

```python
display(df)
display(df.info())
```

### #3 Flow | Correct database "errors"

Begin analyzing the data by correcting "errors" and eliminating information that
is irrelevant to the main analysis.

**The initial data processing:**

* The CustomerID column, being randomly generated data, does not influence the number of cancellations. Therefore, it has been removed
* Indexes with empty data can interfere with the main analysis. Therefore, they were also eliminated

```python
df = df.drop(columns="CustomerID")  # delete "CustomerID" column
df = df.dropna()  # delete empty indexes
```

### #4 Flow | View the Actual Number of Cancellations

Starting the main analysis by looking at the actual number of cancellations.

```python
# shows the actual number of customers who canceled
display(df["cancelou"].value_counts())  # show the count of indexes where there is a value in the "cancelou" column
display(df["cancelou"].value_counts(normalize=True))  # normalizes count value (%)
```

### #5 Flow | How does each columns impact cancellations?

For each column in the table, create a graph (histogram) showing its direct
relationship with the "cancelou" column.  
The graphical visualization helps to map out the main causes of cancellations in
a practical way.

```python
for column in df.columns:
    # creates a histogram relating the value of the current column to the "canceled" column.
    graphic = px.histogram(df, x=column, color="cancelou")
    graphic.show()  # shows the graphic
```

## Result

**Main factors for cancellations:**

1. All customers with monthly contracts
2. Customers who call the call-center more than four times
3. Customers who are more than twenty days late

**Possible solutions:**

1. Offer discounts on quarterly and annual plans
2. Try to resolve the customer's problem before the fourth call to the call-center
3. Charge the customer before the twenty days of delay

**Implementing the solutions:**

```python
df = df[df["duracao_contrato"] != "Monthly"]  # remove customers with a contract duration equal to “Monthly”
df = df[df["ligacoes_callcenter"] <= 4]  # remove customers with more than four calls to the call center
df = df[df["dias_atraso"] <= 20]  # remove customers who are more than twenty days late
```

---

Previously, cancellations were 56.6%. Applying these solutions, the statistic
drops to 18.4%.
