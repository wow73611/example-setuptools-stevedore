#!/usr/bin/env python
#-*- coding:utf-8 -*-

import argparse
from stevedore import driver
from stevedore import extension
from stevedore import hook

def stevedore_driver(namespace, name):
    print "--- driver.DriverManager(%s,%s) ---" % (namespace,name)
    mgr = driver.DriverManager(
        namespace = namespace,
        name = name,
        invoke_on_load = True,
    )
    mgr.driver.catch()

def stevedore_extension(namespace, name):
    print "--- extension.ExtensionManager(%s,%s) ---" % (namespace,name)
    mgr = extension.ExtensionManager(
        namespace = namespace,
        invoke_on_load = True,
    )
    
    def catch_all(ext):
        return (ext.name, ext.obj.catch())
    
    results = mgr.map(catch_all)

def stevedore_hook(namespace, name):
    print "--- hook.HookManager(%s,%s) ---" % (namespace,name)
    mgr = hook.HookManager(
        namespace = namespace,
        name = name,
        invoke_on_load = True,
    ) 
    
    def catch_all(ext):
        return (ext.name, ext.obj.catch())
    
    results = mgr.map(catch_all)


if __name__ == '__main__':
    types = ['driver', 'extension', 'hook']
    parser = argparse.ArgumentParser()
    parser.add_argument('type', choices=types, help='Type of stevedore')
    parser.add_argument('--namespace', default='pokemon', help='Namespace of entry point', )
    parser.add_argument('--name', default='default', help='Name of entry point', )
    options = parser.parse_args()
    
    if options.type == 'driver':
        stevedore_driver(options.namespace,options.name)
    elif options.type == 'extension':
        stevedore_extension(options.namespace,options.name)
    elif options.type == 'hook':
        stevedore_hook(options.namespace,options.name)

