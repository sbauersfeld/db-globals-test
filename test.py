from databricks.sdk.runtime import sc

def func_test():
  return sc.parallelize(range(10)).map(lambda x: x + 1).collect()