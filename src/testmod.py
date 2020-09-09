import click


@click.group()
def cli():
    pass


@cli.command()
def testing_function():
    print("NOthign herse")


@cli.command()
def testing():
    print("Testing 2")


cli()