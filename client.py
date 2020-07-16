from __future__ import print_function

import random
import logging

import grpc

import info_pb2
import info_pb2_grpc
from info_resources import Host
from info_resources import print_sys_info
import time


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    hosts = [
            # add hosts here
            ]
    while True:
        for host in hosts:
            print(f'host: {host.name}')
            sys_info = host.GetSysInfo()
            print_sys_info(sys_info)
        print('sleep')
        time.sleep(1)


if __name__ == '__main__':
    logging.basicConfig()
    run()
