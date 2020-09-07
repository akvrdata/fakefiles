# import boto3
# from moto import mock_s3
# from awsmods import s3_upload
# import pytest
# import os


# mock_bucket_name = "mint-scripts-test"
# storage_pth = "fakefiles_outputs"


# @pytest.yield_fixture(scope="module")
# def s3_bucket():
#     with mock_s3():
#         conn = boto3.resource("s3").create_bucket(Bucket=mock_bucket_name)
#         # yield boto3.resource("s3").Bucket(mock_bucket_name)
#         yield conn