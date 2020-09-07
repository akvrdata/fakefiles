import boto3
import os
import logging
import sys
import click

file_pth = os.path.join(os.getcwd(), "output")


@click.command()
@click.option("--bucket_name", default="mint-scripts-test")
def s3_upload(bucket_name):
    """Loads all the files in output directory to a specified bucket.Bucket name needs to be passed in"""
    try:
        s3 = boto3.resource("s3")
        for root, dir, files in os.walk(file_pth):
            for file in files:
                key = "s3_output/" + file
                dest = file_pth + "/" + file
                s3.Object(bucket_name, key).upload_file(dest)
        return 1
    except Exception as err:
        logging.exception("Error in s3_upload {}".format(err))
        sys.exit(1)


# def cli():
#     s3_upload(bucket_name)


# res = s3_upload("mint-scripts-test")
# print(res)
