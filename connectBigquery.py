from google.cloud import bigquery

client = bigquery.Client()

def sqlCommand(sql):
    query_job = client.query(sql)  # API request
    table = query_job.result()  # Waits for query to finish
    #Enable method: values(), keys(), get(), items()
    #query_job method respond object: google.cloud.bigquery.table.RowIterator
    #output object:  google.cloud.bigquery.table.Row from google.cloud.bigquery.table.RowIterator
    #doc: https://google-cloud-python.readthedocs.io/en/0.32.0/bigquery/reference.html#module-google.cloud.bigquery.table
    return [list(row.values()) for row in table]

def connectTesting():
    sql = "select SESSION_USER();"
    query_job = client.query(sql)  # API request
    table = query_job.result()
    print([list(row.values()) for row in table])

print('connection testing....')
connectTesting()
