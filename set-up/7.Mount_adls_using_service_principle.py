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

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://demo@formula1adlsshreyansh.dfs.core.windows.net/",
  mount_point = "/mnt/formula1adlsshreyansh/demo",
  extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

display(dbutils.fs.ls("//mnt/formula1adlsshreyansh/demo"))

# COMMAND ----------

display(spark.read.csv("//mnt/formula1adlsshreyansh/demo/circuits.csv"))

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


