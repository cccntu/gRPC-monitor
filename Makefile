
all: serve
proto: info.proto
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./info.proto
serve: proto server.py
	python server.py
