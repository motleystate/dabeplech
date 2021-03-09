from invoke import task


@task
def black_format(c):
    """Run black format."""
    c.run("black dabeplech/")


@task
def black_check(c):
    """Run black check."""
    c.run("black dabeplech/ --check")


@task
def docstyle(c):
    """Run pydocstyle."""
    c.run("pydocstyle dabeplech/")


@task
def lint(c):
    """Run flake8."""
    c.run("flake8 dabeplech/")
