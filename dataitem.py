#!/usr/bin/python
from subprocess import call
from os import path

class DataItem(object):
    """A class that makes downloading data from the web easy.

    Attributes
    ----------
    web_url : String, indicating the path to the data

    filename : String, indicating what the file should be named when saved
    to disk. Defaults to None (leaving the name to be the name of the
    download file.

    """

    def __init__(self, web_url, filename=None):
        self.web_url = web_url
        self.filename = filename

    def __repr__(self):
        return "{'url': {0}, 'filename': {1}".format(self.web_url, self.filename)

    def postprocessing_step(postprocess):
        pass

    @staticmethod
    def from_json(filename):
        assert type(filename) is str
        pass # TODO

    def download(self, overwrite=True):
        save_file = "-O " + self.filename if self.filename is not None else ""
        #verbosity = "-q" if not verbose else ""
        print "Downloading {0}".format(self.filename)
        if path.exists(self.filename):
            call("rm " + self.filename, shell=True)
        retval = call("wget -q {0} {1}".format(save_file, self.web_url),
                      shell=True)

urls = ["https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data",
        "http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
        "https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/bupa.data",
        "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
        ]
names = ["mushroom.data", "breast.data", "liver.data", "sonar.data"]

items = [DataItem(url, name) for url, name in zip(urls, names)]
for item in items: item.download()
