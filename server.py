import argparse
from concurrent import futures
import time
import math
import logging

import grpc

import info_pb2
import info_pb2_grpc

import psutil
"""
    print(psutil.cpu_count())
    print(psutil.getloadavg())
"""

def get_cpu_info():
    cpu_count = psutil.cpu_count()
    load_average = psutil.getloadavg()
    return info_pb2.CpuInfo(
            cpu_count = cpu_count,
            load_average = load_average,
            )

class SysInfoServiceServicer(info_pb2_grpc.SysInfoServiceServicer):
    """Provides methods that implement functionality of SysInfoServiceServicer."""

    def __init__(self):
        pass

    def GetSysInfo(self, request, context):
        cpu_info = get_cpu_info()
        return info_pb2.SysInfo(
                cpu_info = cpu_info,
                )

def serve(args):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    info_pb2_grpc.add_SysInfoServiceServicer_to_server(
        SysInfoServiceServicer(), server)
    address = f'{args.ip}:{args.port}'
    port = server.add_insecure_port(address)
    print(f'serving on port {port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()

    parser = argparse.ArgumentParser(description="Parse arguments")
    parser.add_argument("--ip", type = str, default="[::]", help="port")
    parser.add_argument("--port", type = str, default="50051", help="port")
    args = parser.parse_args()

    serve(args)
