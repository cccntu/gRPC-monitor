from __future__ import print_function

import random
import logging

import grpc

import info_pb2
import info_pb2_grpc
import time

def print_sys_info(sys_info):
    cpu_info = sys_info.cpu_info
    print(cpu_info.cpu_count)
    print(cpu_info.load_average)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    channels = []
    stubs = []
    for i in range(100):
        channel = grpc.insecure_channel('localhost:50600')
        channels.append(channel)
        stub = info_pb2_grpc.SysInfoServiceStub(channel)
        stubs.append(stubs)
    with grpc.insecure_channel('localhost:50600') as channel:
        stub = info_pb2_grpc.SysInfoServiceStub(channel)
        sys_info_request = info_pb2.SysInfoRequest()

        while True:
            sys_info = stub.GetSysInfo(sys_info_request)
            print_sys_info(sys_info)
            time.sleep(1)



if __name__ == '__main__':
    logging.basicConfig()
    run()
    with grpc.insecure_channel('localhost:50600') as channel:
        stub = info_pb2_grpc.SysInfoServiceStub(channel)
        sys_info_request = info_pb2.SysInfoRequest()

        while True:
            sys_info = stub.GetSysInfo(sys_info_request)
            print_sys_info(sys_info)
            time.sleep(1)



if __name__ == '__main__':
    logging.basicConfig()
    run()
