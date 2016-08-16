#!/usr/bin/env python
#-*- coding:utf-8 -*-

import argparse
import pkg_resources

def pkg_driver(namespace, name, package=""):
    print "--- pkg_resources.load_entry_point(%s,%s,%s) ---" % (namespace,name,package)
    plugin = pkg_resources.load_entry_point(package,namespace,name)
    plugin().catch()

def pkg_extension(namespace, name):
    print "--- pkg_resouces.iter_entry_points(%s,%s) ---" % (namespace,name)
    if len(name) <= 0:
        name = None
    for ep in pkg_resources.iter_entry_points(group=namespace,name=name):
        plugin = ep.load()
        plugin().catch()

if __name__ == '__main__':
    types = ['driver', 'extension']
    parser = argparse.ArgumentParser()
    parser.add_argument('type', choices=types, help='Type of plugin')
    parser.add_argument('--namespace', default='pokemon', help='Namespace of entry point', )
    parser.add_argument('--name', default='default', help='Name of entry point', )
    parser.add_argument('package', nargs='?', default='pokemon', help='Name of package', )
    options = parser.parse_args()

    if options.type == 'driver':
        pkg_driver(options.namespace,options.name,options.package)
    elif options.type == 'extension':
        pkg_extension(options.namespace,options.name)

