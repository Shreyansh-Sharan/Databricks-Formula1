# Databricks notebook source
dbutils.secrets.help()


# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

test = r'Formula1 Scope'
dbutils.secrets.list('Formula1 Scope')

# COMMAND ----------

dbutils.secrets.get(scope="Formula1 Scope",key="formula1-account-key")

# COMMAND ----------


