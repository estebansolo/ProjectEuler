from time import time
import click


def timing(fn):
    def wrapper(*args, **kwargs):
        start = time()
        response = fn(*args, **kwargs)
        click.echo(f"Time: {time() - start} sec")
        click.echo()
        return response

    return wrapper


def execution(fn):
    def wrapper(*args, **kwargs):
        response = fn(*args, **kwargs)
        click.echo(f"Solved with {args}: {response}")
        return response

    return wrapper
