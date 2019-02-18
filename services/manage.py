# services/insta-broker/manage.py
import coverage
import unittest
import sys

from api import create_app


COV = coverage.coverage(
    branch=True,
    include='*',
    omit=[
        'tests/*',
        'config.py',
    ]
)
COV.start()

app = create_app()


@app.app.cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@app.app.cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.xml_report()
        COV.erase()
        return 0
    sys.exit(result)

