# Databricks notebook source
dbutils.secrets.get(scope="Formula1 Scope",key="formula1-account-key")

# COMMAND ----------

dbutils.secrets.list(scope='Formula1 Scope')

# COMMAND ----------

def mount_adls(storage_Account_Name, containerName):
    client_id = dbutils.secrets.get(scope="Formula1 Scope",key="formula-1-clientID")
    tenant_id = dbutils.secrets.get(scope="Formula1 Scope",key="tenantId")
    secret = dbutils.secrets.get(scope="Formula1 Scope",key="formula1-secret")

    configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

    if any(mount.mountPoint == f"/mnt/{storage_Account_Name}/{containerName}" for mount in dbutils.fs.mounts()):
        dbutils.fs.unmount(f"/mnt/{storage_Account_Name}/{containerName}")

    dbutils.fs.mount(
        source = f"abfss://{containerName}@{storage_Account_Name}.dfs.core.windows.net/",
        mount_point = f"/mnt/{storage_Account_Name}/{containerName}",
        extra_configs = configs)
    

mount_adls("formula1adlsshreyansh","raw")
mount_adls("formula1adlsshreyansh","processed")
mount_adls("formula1adlsshreyansh","presentation")

dbutils.fs.mounts()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


