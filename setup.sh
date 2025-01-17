# AWS commands

# create an AWS bucket, with name_of_bucket replacing 'frequently-modulated'
aws s3 mb s3://frequently-modulated

# get vpcId from
aws ec2 describe-vpcs

# get RouteTableId from
aws ec2 describe-route-tables

# create S3 gateway endpoint (aka VPC gateway)
aws ec2 create-vpc-endpoint --vpc-id <vpcId from above> --service-name com.amazonaws.us-east-1.s3 --route-table-ids <RouteTableId>


