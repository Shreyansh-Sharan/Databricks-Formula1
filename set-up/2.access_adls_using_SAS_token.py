# Databricks notebook source


# COMMAND ----------



# COMMAND ----------

# Access Key = wZ0q+V+Ln1EZDJbNdDSBb9PaEDhCNwaF2fyxtJ4jzq5yBpFxPo/LmhotgGkErapOPRawz3N9koYi+ASt2W+/Iw==
DefaultEndpointsProtocol=https;AccountName=formula1adlsshreyansh;AccountKey=APuZzCC+y7KQMi7PqENYbtDEBp04HpdpwwdTA5vy9JX/RsUIFOdgrtGhIUliApaoW6IB+m5zlZwT+AStCCb2Kw==;EndpointSuffix=core.windows.net

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.formula1adlsshreyansh.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula1adlsshreyansh.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.<storage-account>.dfs.core.windows.net", "sp=rl&st=2023-09-12T09:30:36Z&se=2023-09-12T17:30:36Z&spr=https&sv=2022-11-02&sr=c&sig=YKL6EEO1vYrzO32KQtt4tPCZNrU%2ByBhR%2F0WmJx4VJlE%3D"))

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1adlsshreyansh.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1adlsshreyansh.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


