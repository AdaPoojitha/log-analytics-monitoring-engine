from dask.distributed import Client,LocalCluster 
# client ():client is a python method which is used to make a connection between dask cluster and pyhton code which is mean as local machine
# local cluster:It is a cluster used to develop and test or prove distributed computing locally before deploying into main cluster.
# without client,
# we cannot know number of workers exist in  clusters 
# we cannot know what is the task and where the task is running and cannot know the status of the task
# we cannot monitor the process of execution
# with client: we can assign task to workers and can easily connect python code with the dask and 
# can see the status of dask

def create_dask_client():
    cluster = LocalCluster(
        n_workers=4,  # Number of workers in the cluster
        threads_per_worker=1,  # Number of threads per worker
        memory_limit='1GB' , # Memory limit for each worker
        dashboard_address=":8790"
    )
    return Client(cluster)
