# AWS REST API Helpers

## Overview:

A set of helper scripts to set HTTP headers while making requests to AWS REST API from the command line.

Components:
- get_aws_auth_header.py - for the `Authorization` header
- get_aws_date.py - for the `x-amz-date` header
- get_aws_content_sha.py - for the `x-amz-content-sha256` header

### Examples

Sample usage can be demonstrated with curl.

#### GET on a private S3 bucket:
```
curl -XGET https://{bucket-name}.s3.eu-central-1.amazonaws.com
```
fails with
```
<?xml version="1.0" encoding="UTF-8"?>
<Error><Code>AccessDenied</Code><Message>Access Denied</Message><RequestId>...</RequestId><HostId>...</HostId></Error>
```
But with the headers from the helper scripts:
```
curl -XGET https://{bucket-name}.s3.eu-central-1.amazonaws.com \
    -H 'Authorization: '"$(python3 get_aws_auth_header.py GET s3 eu-central-1 https://{bucket-name}.s3.eu-central-1.amazonaws.com)" \
    -H 'Host: {bucket-name}.s3.eu-central-1.amazonaws.com' \
    -H 'x-amz-date: '"$(python3 get_aws_date.py)" \
    -H 'x-amz-content-sha256: '"$(python3 get_aws_content_sha.py)"
```
succeeds.

#### GET on API Gateway resource with Authorization set to AWS_IAM:
```
curl -XGET https://{restapi_id}.execute-api.eu-central-1.amazonaws.com/test
```
fails with
```
{"message":"Missing Authentication Token"}
```
But with the headers from the helper scripts:
```
curl -XGET https://{restapi_id}.execute-api.eu-central-1.amazonaws.com/test \
    -H 'Authorization: '"$(python3 get_aws_auth_header.py GET execute-api eu-central-1 https://{restapi_id}.execute-api.eu-central-1.amazonaws.com/test)" \
    -H 'Host: {restapi_id}.execute-api.eu-central-1.amazonaws.com' \
    -H 'X-Amz-Date: '"$(python3 get_aws_date.py)"
```
succeeds.

#### POST on API Gateway resource with Authorization set to AWS_IAM:
```
curl -XPOST -H 'Content-Type: application/json' -d '{"type":"dog","price":1000}' https://{restapi_id}.execute-api.eu-central-1.amazonaws.com/test/pets
```
fails with
```
{"message":"Missing Authentication Token"}
```
But with the headers from the helper scripts:

```
curl -XPOST https://{restapi_id}.execute-api.eu-central-1.amazonaws.com/test/pets \
    -H 'Authorization: '"$(python3 get_aws_auth_header.py POST execute-api eu-central-1 https://{restapi_id}.execute-api.eu-central-1.amazonaws.com/test/pets '{"type":"dog","price":1000}')" \
    -H 'Host: {restapi_id}.execute-api.eu-central-1.amazonaws.com' \
    -H 'X-Amz-Date: '"$(python3 get_aws_date.py)" \
    -H 'Content-Type: application/json' \
    -d '{"type":"dog","price":1000}' 
```
succeeds.

## Why would you find that useful?

Even though AWS provides its own CLI tools and SDKs, sometimes it might be useful to use some third-party CLI commands. 
Actually the scripts were prepared to use with Apache Bench to stress test SageMaker endpoints, but they could potentially be used with any command line tool supporting HTTP headers, as demonstrated by the examples using curl.


## How would you setup your own scripts?

1. Export AWS credentials as env variables e.g. like this:
```
export AWS_ACCESS_KEY_ID=`aws configure get default.aws_access_key_id`
export AWS_SECRET_ACCESS_KEY=`aws configure get default.aws_secret_access_key`
```
2. Use the scripts to set HTTP headers as shown in the examples.