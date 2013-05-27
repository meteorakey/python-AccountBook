#!/usr/bin python
# -*- coding: utf-8 -*-
# オプションを管理するクラス
import optparse

class Option:

    def __init__(self):
        usage = u'%prog [-a ITEM AMOUNT DATE] [-d ITEM] [-s DATE] [-l]'
        version = u'%prog 0.0'
        self.parser = optparse.OptionParser(usage=usage, version=version)
        self.parser.add_option('-a', '--add', type='string')
        self.parser.add_option('-d', '--delete', type='string')
        self.parser.add_option('-s', '--sum', type='string')
        self.parser.add_option('-l', '--list', action='store_true', default=False)
        self.options, self.args = self.parser.parse_args()

    def print_options(self):
        print self.options
        print self.args

    def get_options(self):
        return self.options

    def get_args(self):
        return self.args

    def check_multi_option(self):
        flg = 0
        if (self.options.add != None):
            flg = flg + 1
        if (self.options.delete != None):
            flg = flg + 1
        if (self.options.sum != None):
            flg = flg + 1
        if (self.options.list):
            flg = flg + 1
        print flg
        if (flg != 1):
            return False
        return True
