
def lambda_handler(event, context):
    # Define the EMR cluster configuration
    emr_client = boto3.client('emr', region_name='your-region')  # Replace 'your-region' with your AWS region
    
    cluster_name = 'your-cluster-name'  # Replace 'your-cluster-name' with your desired cluster name
    release_label = 'emr-6.4.0'  # Specify the EMR release label
    instance_type = 'm5.xlarge'  # Specify the EC2 instance type
    instance_count = 2  # Specify the number of instances in the cluster
    
    # Create EMR cluster
    response = emr_client.run_job_flow(
        Name=cluster_name,
        ReleaseLabel=release_label,
        Instances={
            'InstanceGroups': [
                {
                    'InstanceRole': 'MASTER',
                    'InstanceType': instance_type,
                    'InstanceCount': 1
                },
                {
                    'InstanceRole': 'CORE',
                    'InstanceType': instance_type,
                    'InstanceCount': instance_count - 1
                }
            ],
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False
        },
        VisibleToAllUsers=True,  # Set to True if you want the cluster to be visible to all IAM users
        JobFlowRole='EMR_EC2_DefaultRole',  # IAM role for EMR cluster
        ServiceRole='EMR_DefaultRole'  # IAM role for EMR service
    )
    
    # Extract the cluster ID from the response
    cluster_id = response['JobFlowId']
    
    return {
        'statusCode': 200,
        'body': f'EMR cluster creation initiated. Cluster ID: {cluster_id}'
    }