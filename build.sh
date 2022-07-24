#! /bin/bash
rm -r build/ dist/ playwithmpv.egg-info/
python setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*
