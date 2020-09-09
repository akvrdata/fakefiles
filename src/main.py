import yaml
import os
from mimesis import Generic
import csv
import logging
import sys
import click
import src.awsmods


fake = Generic("en")  # main object to be used in the yaml configs
"""Generate CSV files with dummy data based on mimesis configs"""


class createFakeFiles:
    def __init__(self):
        # declaring all the variables and filepath's

        self.v_config_path = os.getcwd()
        self.v_config_file = "configs/config.yml"
        self.v_config_file_path_location = self.v_config_path + "/" + self.v_config_file
        self.output_file_path = self.v_config_path + "/" + "output/"

    def extractor(self):
        """Extracts the attributes from yaml config.Helps in Concurrency mapping later.TODO"""
        try:
            self.v_dict_of_table_names = {}
            v_config_file_handler = open(self.v_config_file_path_location)
            self.data = yaml.load(v_config_file_handler, Loader=yaml.FullLoader)
            self.v_dict_of_table_names = self.data["tables"].keys()

            for table_name in self.v_dict_of_table_names:
                for cols in self.data["tables"][table_name]:
                    output_file_name = "{}".format(table_name)
                    headers = list(self.data["tables"][table_name].keys())[1:]
                    row_nos = self.data["tables"][table_name]["rows_to_generate"]
                    list_of_rows = str(
                        list(self.data["tables"][table_name].values())[1:]
                    ).replace("'", "")
                    self.write_csv(output_file_name, headers, row_nos, list_of_rows)
        except Exception as err:
            logging.error("Error in Extractor {}".format(err))
            sys.exit(1)

    def write_csv(self, out_file, header_row, row_count, rows):
        try:
            ##TODO: Ouptut path to be determined from userinput/via config
            file_name = self.output_file_path + "{}".format(out_file) + ".csv"
            with open(file_name, "w+") as filehandle:
                csvwriter = csv.writer(filehandle, quoting=csv.QUOTE_ALL)
                csvwriter.writerow(header_row)
                for _ in range(row_count):
                    csvwriter.writerow(eval(rows))
        except Exception as err:
            logging.exception("Error in write_csv {}".format(err))
            sys.exit(1)

    def sample_csv():
        pass


@click.group()
def cli():
    """
    CLI generates CSV based on the Configuration in /output/config.yml.
    Facility for upload too exists but works only on an EC2.
    """
    pass


@cli.command()
def generate():
    """
    \b
    Creates the file as per the configuration.
    \b Sample config :
    \b
    table1:
        rows_to_generate: 1
        first_name: fake.person.first_name()
        last_name: fake.person.last_name()
        status: fake.numbers.integer_number(1,15)
        id: fake.numbers.integer_number(1,10000)
        vendorid: fake.numbers.integer_number(1,100)
        userdate: fake.datetime.date(start=2019, end=2020)
        description: fake.text.word()
    """
    obj = createFakeFiles()
    lis = obj.extractor()
    # print("created")


@cli.command()
@click.option("--bucket_name", default="mint-scripts-test")
def upload(bucket_name):
    """Uploads the generated file to S3 Bucket.
    Works only when on an EC2"""
    src.awsmods.s3_upload(bucket_name)
    # print("uploaded")


cli()