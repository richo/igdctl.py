#!/usr/bin/env python

# AUTHOR: Rich Healey <richo@psych0tik.net>
# Copyright: (c) '11 Rich Healey
# License: Released under 3 clause BSD or WTFPL at your option
#
# Credit: This script is a loose port of igdctl.pl by Vincent Wochnik
#       : He is contactable at v.wochnik@yagoo.com or ubuntu.blogetery.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import sys

try:
    import argparse
except ImportError:
    sys.stderr.write("Missing dependencies\n")
    exit()

def get_parser(): #{{{
    parser = argparse.ArgumentParser(description="Control UPnP on internet gateway devices")
    # Actions
    parser.add_argument('--enable', dest='action_enable', action='store_true',
            help="Enable the internet connection")
    parser.add_argument('--disable', dest='action_disable', action='store_true',
            help="Disable the internet connection")
    parser.add_argument('-a', '--add-port', dest='action_add', action='store_true',
            help="Add a port forward")
    parser.add_argument('-g', '--get-port', dest='action_get', action='store_true',
            help="Get a port forward")
    parser.add_argument('-R', '--remove-port', dest='action_remove', action='store_true',
            help="Remote a port forward")
    parser.add_argument('-l', '--list-ports', dest='action_list', action='store_true',
            help="List active port forwards")

    # IP asssignment
    parser.add_argument('-E', '--external-ip', dest='external_ip', action='store',
            help="External IP address")
    parser.add_argument('-I', '--internal-ip', dest='internal_ip', action='store',
            help="Internal IP address")
    # Port assignment
    parser.add_argument('-e', '--external-port', dest='external_port', action='store',
            help="External port")
    parser.add_argument('-i', '--internal-port', dest='internal_port', action='store',
            help="Interal port")
    # Misc options
    parser.add_argument('-P', '--protocol', dest='protocol', action='store',
            help="Protocol, (TCP|UDP)")
    parser.add_argument('-D', '--duration', dest='duration', action='store',
            help="Duration of port forward")
    return parser
    #}}}

def bail(msg):
    sys.stderr.write("%(msg)s\n" % { "msg" : msg })
    sys.exit(1)

# def validate_ip_address(addr):

def validate_port(port):
    if 65535 < port or 1 > port:
        bail("Invalid port; %(port)s" % { "port": str(port)})

def validate_options(opts):
    # test for only a single action
    if (opts.action_enable, opts.action_disable, opts.action_add, opts.action_get,
            opts.action_remove, opts.action_list).count(True) != 1:
        bail("Specify exactly one action")
    # TODO validate IP addresses

def action_enable(opts): #{{{
    raise NotImplementedError
#}}}

def action_disable(opts): #{{{
    raise NotImplementedError
#}}}

def action_add(opts): #{{{
    raise NotImplementedError
#}}}

def action_get(opts): #{{{
    raise NotImplementedError
#}}}

def action_remove(opts): #{{{
    raise NotImplementedError
#}}}

def action_list(opts): #{{{
    raise NotImplementedError
#}}}

def main():
    opts = get_parser().parse_args()
    validate_options(opts) # Doesn't return if invalid

    if opts.action_enable:
        action_enable(opts)
    elif opts.action_disable:
        action_disable(opts)
    elif opts.action_add:
        action_add(opts)
    elif opts.action_get:
        action_get(opts)
    elif opts.action_remove:
        action_remove(opts)
    elif opts.action_list:
        action_list(opts)



if __name__ == "__main__":
    main()
