import grpc
import info_pb2
import info_pb2_grpc

class Host():
    def __init__(self, address, name):
        self.name = name
        self.channel = grpc.insecure_channel(address)
        self.SysInfoServiceStub = info_pb2_grpc.SysInfoServiceStub(self.channel)
    def GetSysInfo(self, sys_info_request = info_pb2.SysInfoRequest()):
        sys_info = self.SysInfoServiceStub.GetSysInfo(sys_info_request)
        return sys_info
    def close(self):
        self.channel.close()



def print_sys_info(sys_info):
    cpu_info = sys_info.cpu_info
    print(cpu_info.cpu_count)
    print(cpu_info.load_average)
