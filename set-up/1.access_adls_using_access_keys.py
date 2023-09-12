# Databricks notebook source


# COMMAND ----------

formula1_dl_accountkey = dbutils.secrets.get(scope="Formula1 Scope",key="formula1-account-key")

# COMMAND ----------



# COMMAND ----------

spark.conf.set("fs.azure.account.key.formula1adlsshreyansh.dfs.core.windows.net",formula1_dl_accountkey)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1adlsshreyansh.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1adlsshreyansh.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


