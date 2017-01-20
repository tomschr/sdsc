# Copyright (c) 2017 SUSE Linux GmbH
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 3 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, contact SUSE LLC.
#
# To contact SUSE about this file by physical or electronic mail,
# you may find current contact information at www.suse.com

from lxml import etree
import glob
import os


class XSLTFiles(object):
    def __init__(self, parser):
        self.parser = parser
        location = os.path.dirname(os.path.realpath(__file__))
        self._checkfiles = glob.glob(os.path.join(location, 'xsl-checks', '*.xslc'))
        # if self._checkfiles:
        #    raise

    @property
    def checkfiles(self):
        return self._checkfiles

    def __iter__(self):
        for checkfile in self._checkfiles:
            checkmodule = os.path.splitext(os.path.basename(checkfile))[0]
            transform = etree.XSLT(etree.parse(checkfile, self.parser))
            yield {'name': checkmodule, 'transform': transform}

    def __repr__(self):
        return "<{}: {}>".format(type(self).__name__, list(self))


##
def linenumber(context, ...):


class App(object):
    def __init__(self, clidict=None):
        self._clidict = {} if clidict is None else clidict
        # Prepare parser (add py: namespace)
        self.ns = etree.FunctionNamespace('https://www.github.com/openSUSE/suse-doc-style-checker')
        self.ns.prefix = 'py'
        #ns.update(dict(linenumber=linenumber,
        #               termcheck=termcheck,
        #               buildtermdata=buildtermdata,
        #               dupecheck=dupecheck,
        #               sentencelengthcheck=sentencelengthcheck,
        #               sentencesegmenter=sentencesegmenter,
        #               tokenizer=tokenizer,
        #               counttokens=counttokens,
        #               splitpath=splitpath,
        #               splitvalueunit=splitvalueunit))


        self.parser = etree.XMLParser(ns_clean=True,
                                      remove_pis=False,
                                      dtd_validation=False,
                                      )
        self.xsltfiles = XSLTFiles(self.parser)

    @property
    def cli(self):
        return self._clidict

    @property
    def inputfile(self):
        return self._clidict.get('INPUTFILE')

    @property
    def outputfile(self):
        return self._clidict.get('OUTPUTFILE')

    def __repr__(self):
        return "<{} input={!r} output={!r}>".format(type(self).__name__,
                                       self.inputfile,
                                       self.outputfile)

    def linenumber(self, context, ...):
        # ...
