from invoke import task


@task
def clean(c):
    """Delete the doc from the local."""
    c.run("rm -rf docs/_build")


@task(clean)
def build(c):
    """Build the doc in local."""
    c.run("sphinx-build docs docs/_build/html")


@task
def docstyle(c):
    """Check the doc using pydocstyle."""
    c.run("pydocstyle src/")
