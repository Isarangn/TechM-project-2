from multiprocessing.sharedctypes import Value
from aws_cdk import (
    Duration,
    App, RemovalPolicy,Stack,
    CfnOutput,
    aws_sqs as sqs,
    aws_s3 as s3,
    aws_dynamodb,
    aws_rds as rds,
    aws_ec2 as ec2
)
from constructs import Construct

class FirstCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        queue = sqs.Queue(
            self, "StaticappQueue",
            visibility_timeout=Duration.seconds(300),
         )

        bucket = s3.Bucket(self,"sitebucket",bucket_name="cdksarang3101",public_read_access=True,
        website_index_document="index.html")

        CfnOutput(self,"output1", value=bucket.bucket_name)
        CfnOutput(self,"output2", value=bucket.bucket_website_url)

class DynamodbLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        demo_table = aws_dynamodb.Table(
            self, "usecase2a",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING
            )
        )
class RDSStack(Stack):
    def __init__(self, app: App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        vpc = ec2.Vpc(self, "VPC")

        rds.DatabaseInstance(
            self, "RDS",
            database_name="usecase2b",
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_16
            ),
            vpc=vpc,
            port=3306,
            instance_type= ec2.InstanceType.of(
                ec2.InstanceClass.MEMORY4,
                ec2.InstanceSize.LARGE,
            ),
            removal_policy=RemovalPolicy.DESTROY,
            deletion_protection=False
        ),
app = App()
RDSStack(app, "RDSStack")
app.synth()
        # example resource
        # queue = sqs.Queue(
        #     self, "FirstCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
