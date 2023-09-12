# Databricks notebook source


# COMMAND ----------



# COMMAND ----------

# Access Key = wZ0q+V+Ln1EZDJbNdDSBb9PaEDhCNwaF2fyxtJ4jzq5yBpFxPo/LmhotgGkErapOPRawz3N9koYi+ASt2W+/Iw==
DefaultEndpointsProtocol=https;AccountName=formula1adlsshreyansh;AccountKey=APuZzCC+y7KQMi7PqENYbtDEBp04HpdpwwdTA5vy9JX/RsUIFOdgrtGhIUliApaoW6IB+m5zlZwT+AStCCb2Kw==;EndpointSuffix=core.windows.net

# COMMAND ----------

spark.conf.set("fs.azure.account.key.formula1adlsshreyansh.dfs.core.windows.net","wZ0q+V+Ln1EZDJbNdDSBb9PaEDhCNwaF2fyxtJ4jzq5yBpFxPo/LmhotgGkErapOPRawz3N9koYi+ASt2W+/Iw==")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1adlsshreyansh.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1adlsshreyansh.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


