import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://frequently-modulated/accelerometer/landing/"],
        "recurse": True,
    },
    transformation_ctx="AccelerometerLanding_node1",
)

# Script generated for node Customer Trusted
CustomerTrusted_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://frequently-modulated/customer/trusted/"], "recurse": True},
    transformation_ctx="CustomerTrusted_node1",
)

# Script generated for node Customer Privacy Filter
CustomerPrivacyFilter_node1 = Join.apply(
    frame1=AccelerometerLanding_node1,
    frame2=CustomerTrusted_node1,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="CustomerPrivacyFilter_node1",
)

# Script generated for node Drop Fields
DropFields_node1 = ApplyMapping.apply(
    frame=CustomerPrivacyFilter_node1,
    mappings=[
        ("user", "string", "user", "string"),
        ("timeStamp", "long", "timeStamp", "long"),
        ("x", "double", "x", "float"),
        ("y", "double", "y", "float"),
        ("z", "double", "z", "float"),
    ],
    transformation_ctx="DropFields_node1",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://frequently-modulated/accelerometer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="AccelerometerTrusted_node1",
)

job.commit()
