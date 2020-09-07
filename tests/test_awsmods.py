import boto3
from moto import mock_s3
from awsmods import s3_upload
import pytest
import os

out_pth = os.getcwd() + "/" + "output"
mock_bucket_name = "mint-scripts-test"
storage_pth = "fakefiles_outputs"


@pytest.fixture(autouse=True)
def setup_s3():
    mocks3 = mock_s3()
    mocks3.start()
    res = boto3.resource("s3", "us-west-2")
    res.create_bucket(Bucket=mock_bucket_name)
    yield
    mocks3.stop()


def test_s3_upload(setup_s3):
    s3_upload(mock_bucket_name)
    test_s3 = boto3.resource("s3")
    bucket = test_s3.Bucket(mock_bucket_name)
    for root, d, source_files in os.walk(out_pth):
        for file_in in source_files:
            src_file_count = len(source_files)
    target_count = 0
    for files_in_s3 in bucket.objects.all():
        target_count = target_count + 1
    assert src_file_count and target_count > 1


# assert src_file_count and target_count > 1
# @pytest.fixture(autouse=True)
# def moto_boto():
#     mocks3 = mock_s3()
#     mocks3.start()
#     res = boto3.resource("s3")
#     res.create_bucket(Bucket=mock_bucket_name)
#     yield
#     mocks3.stop()


# def test_list_buckets(moto_boto):
#     test_s3 = boto3.resource("s3")
#     bucket = test_s3.Bucket(mock_bucket_name)
#     target_count = 0
#     for files_in_s3 in bucket.objects.all():
#         target_count = target_count + 1
#     assert target_count == 0
