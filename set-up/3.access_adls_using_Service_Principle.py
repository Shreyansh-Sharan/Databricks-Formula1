# Databricks notebook source


# COMMAND ----------



# COMMAND ----------

client_id = "0db11108-1edf-4a24-8c7d-27bf7450a0ab"
tenant_id = "5c979e27-0063-4697-891c-ba85b3eddf83"
secret = "STa8Q~o430sSgEc4nk5_jVkL3jgO6myf3bw5-aNB"

# COMMAND ----------


spark.conf.set("fs.azure.account.auth.type.formula1adlsshreyansh.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.formula1adlsshreyansh.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.formula1adlsshreyansh.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.formula1adlsshreyansh.dfs.core.windows.net", secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.formula1adlsshreyansh.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")


# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1adlsshreyansh.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1adlsshreyansh.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


