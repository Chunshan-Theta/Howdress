from google.cloud import bigquery

client = bigquery.Client()

def momoInsert(gid,picLink,title,base64,cat,itemLink):
    sql = "INSERT INTO `howdress.pic.basic` (`picId`,`source_link`,`source_title`,`base64`,`description`, `detail_link` ) VALUES (\""+str(gid)+"\",\""+str(picLink)+"\",\""+str(title)+"\",\""+str(base64)+"\",\""+str(cat)+"\",\""+str(itemLink)+"\");"
    #print(sql)
    return sqlCommand(sql)


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
