rm -rf dist/*
python setup.py sdist
tar -xvf dist/ShareYourSystem-1.0.tar.gz
mv ShareYourSystem-1.0 dist/
rm -rf build/*
sudo python dist/ShareYourSystem-1.0/setup.py install