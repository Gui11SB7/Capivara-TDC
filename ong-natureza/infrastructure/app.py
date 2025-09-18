#!/usr/bin/env python3
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_s3_deployment as s3deploy,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    aws_dynamodb as dynamodb,
    aws_cloudwatch as cloudwatch,
    RemovalPolicy
)

class VerdeVivoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3 para site estático
        website_bucket = s3.Bucket(
            self, "VerdeVivoWebsite",
            website_index_document="index.html",
            public_read_access=True,
            removal_policy=RemovalPolicy.DESTROY
        )

        # CloudFront para CDN
        distribution = cloudfront.CloudFrontWebDistribution(
            self, "VerdeVivoDistribution",
            origin_configs=[
                cloudfront.SourceConfiguration(
                    s3_origin_source=cloudfront.S3OriginConfig(
                        s3_bucket_source=website_bucket
                    ),
                    behaviors=[cloudfront.Behavior(is_default_behavior=True)]
                )
            ]
        )

        # DynamoDB para dados ambientais
        impact_table = dynamodb.Table(
            self, "ImpactDataTable",
            table_name="verde-vivo-impact",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.DESTROY
        )

        # Lambda para API de dados
        impact_lambda = lambda_.Function(
            self, "ImpactDataFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "TABLE_NAME": impact_table.table_name
            }
        )

        impact_table.grant_read_write_data(impact_lambda)

        # API Gateway
        api = apigateway.RestApi(
            self, "VerdeVivoApi",
            rest_api_name="Verde Vivo Impact API"
        )

        impact_integration = apigateway.LambdaIntegration(impact_lambda)
        api.root.add_method("GET", impact_integration)

        # CloudWatch Dashboard
        dashboard = cloudwatch.Dashboard(
            self, "VerdeVivoDashboard",
            dashboard_name="verde-vivo-metrics"
        )

        # Deploy do site
        s3deploy.BucketDeployment(
            self, "DeployVerdeVivoSite",
            sources=[s3deploy.Source.asset("../")],
            destination_bucket=website_bucket,
            distribution=distribution,
            distribution_paths=["/*"]
        )

app = cdk.App()
VerdeVivoStack(app, "VerdeVivoStack")
app.synth()
