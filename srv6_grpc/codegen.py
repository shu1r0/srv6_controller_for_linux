#!/usr/bin/env python3

from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I.',
        '--python_out=.',
        '--grpc_python_out=.',
        './srv6_route.proto',
    )
)