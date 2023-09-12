# Databricks notebook source
dbutils.secrets.get(scope="Formula1 Scope",key="formula1-account-key")

# COMMAND ----------

dbutils.secrets.list(scope='Formula1 Scope')

# COMMAND ----------



# COMMAND ----------

client_id = dbutils.secrets.get(scope="Formula1 Scope",key="formula-1-clientID")
tenant_id = dbutils.secrets.get(scope="Formula1 Scope",key="tenantId")
secret = dbutils.secrets.get(scope="Formula1 Scope",key="formula1-secret")

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


