# Databricks notebook source
display(dbutils.fs.ls('/'))

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/FileStore/tables"))

# COMMAND ----------

display(spark.read.csv("dbfs:/FileStore/tables/circuits.csv"))

# COMMAND ----------


