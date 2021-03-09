from invoke import task


@task
def unit(c):
    """Run the unit tests."""
    c.run("pytest tests/")


@task
def cov(c, xml_report=False):
    """Run the unit tests and the test coverage."""
    options = ['--cov-report term']
    if xml_report:
        options.append("--cov-report xml")
    c.run(f"pytest {' '.join(options)} --cov=dabeplech/ tests/")
