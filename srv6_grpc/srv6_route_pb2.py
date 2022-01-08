# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: srv6_route.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='srv6_route.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10srv6_route.proto\"\xed\x01\n\x05Route\x12\x13\n\x0b\x64\x65stination\x18\x01 \x01(\t\x12\x14\n\x07gateway\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03\x64\x65v\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06metric\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x12\n\x05table\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12 \n\nseg6_encap\x18\n \x01(\x0b\x32\n.Seg6EncapH\x00\x12*\n\x0fseg6local_encap\x18\x0b \x01(\x0b\x32\x0f.Seg6LocalEncapH\x00\x42\x07\n\x05\x65ncapB\n\n\x08_gatewayB\x06\n\x04_devB\t\n\x07_metricB\x08\n\x06_table\"O\n\tSeg6Encap\x12\x17\n\x04type\x18\x01 \x01(\x0e\x32\t.Seg6Type\x12\x17\n\x04mode\x18\x02 \x01(\x0e\x32\t.Seg6Mode\x12\x10\n\x08segments\x18\x03 \x03(\t\"\xcb\x01\n\x0eSeg6LocalEncap\x12\x17\n\x04type\x18\x01 \x01(\x0e\x32\t.Seg6Type\x12 \n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x10.Seg6LocalAction\x12\r\n\x03nh6\x18\n \x01(\tH\x00\x12\r\n\x03nh4\x18\x0b \x01(\tH\x00\x12\"\n\x03srh\x18\x0c \x01(\x0b\x32\x13.Seg6LocalEncap.SrhH\x00\x1a\x33\n\x03Srh\x12\x10\n\x08segments\x18\x01 \x03(\t\x12\x11\n\x04hmac\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_hmacB\x07\n\x05param\"\x1c\n\nRouteReply\x12\x0e\n\x06status\x18\x01 \x01(\r\"\x14\n\x12ShowRoutes6Request\"\x12\n\x10ShowRoutes6Reply*#\n\x08Seg6Type\x12\x08\n\x04SEG6\x10\x00\x12\r\n\tSEG6LOCAL\x10\x01*.\n\x08Seg6Mode\x12\n\n\x06INLINE\x10\x00\x12\t\n\x05\x45NCAP\x10\x01\x12\x0b\n\x07L2ENCAP\x10\x02*^\n\x0fSeg6LocalAction\x12\x07\n\x03\x45ND\x10\x00\x12\t\n\x05\x45ND_X\x10\x01\x12\x0b\n\x07\x45ND_DX4\x10\x02\x12\x0b\n\x07\x45ND_DX6\x10\x03\x12\n\n\x06\x45ND_B6\x10\x04\x12\x11\n\rEND_B6_ENCAPS\x10\x05\x32\x87\x01\n\x0bSeg6Service\x12\x1f\n\x08\x41\x64\x64Route\x12\x06.Route\x1a\x0b.RouteReply\x12\"\n\x0bRemoveRoute\x12\x06.Route\x1a\x0b.RouteReply\x12\x33\n\tShowRoute\x12\x13.ShowRoutes6Request\x1a\x11.ShowRoutes6Replyb\x06proto3'
)

_SEG6TYPE = _descriptor.EnumDescriptor(
  name='Seg6Type',
  full_name='Seg6Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEG6', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEG6LOCAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=619,
  serialized_end=654,
)
_sym_db.RegisterEnumDescriptor(_SEG6TYPE)

Seg6Type = enum_type_wrapper.EnumTypeWrapper(_SEG6TYPE)
_SEG6MODE = _descriptor.EnumDescriptor(
  name='Seg6Mode',
  full_name='Seg6Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INLINE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENCAP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='L2ENCAP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=656,
  serialized_end=702,
)
_sym_db.RegisterEnumDescriptor(_SEG6MODE)

Seg6Mode = enum_type_wrapper.EnumTypeWrapper(_SEG6MODE)
_SEG6LOCALACTION = _descriptor.EnumDescriptor(
  name='Seg6LocalAction',
  full_name='Seg6LocalAction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='END', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='END_X', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='END_DX4', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='END_DX6', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='END_B6', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='END_B6_ENCAPS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=704,
  serialized_end=798,
)
_sym_db.RegisterEnumDescriptor(_SEG6LOCALACTION)

Seg6LocalAction = enum_type_wrapper.EnumTypeWrapper(_SEG6LOCALACTION)
SEG6 = 0
SEG6LOCAL = 1
INLINE = 0
ENCAP = 1
L2ENCAP = 2
END = 0
END_X = 1
END_DX4 = 2
END_DX6 = 3
END_B6 = 4
END_B6_ENCAPS = 5



_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='Route',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination', full_name='Route.destination', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='Route.gateway', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dev', full_name='Route.dev', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric', full_name='Route.metric', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table', full_name='Route.table', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seg6_encap', full_name='Route.seg6_encap', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seg6local_encap', full_name='Route.seg6local_encap', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='encap', full_name='Route.encap',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_gateway', full_name='Route._gateway',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_dev', full_name='Route._dev',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_metric', full_name='Route._metric',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_table', full_name='Route._table',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=21,
  serialized_end=258,
)


_SEG6ENCAP = _descriptor.Descriptor(
  name='Seg6Encap',
  full_name='Seg6Encap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Seg6Encap.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='Seg6Encap.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='segments', full_name='Seg6Encap.segments', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=339,
)


_SEG6LOCALENCAP_SRH = _descriptor.Descriptor(
  name='Srh',
  full_name='Seg6LocalEncap.Srh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='segments', full_name='Seg6LocalEncap.Srh.segments', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hmac', full_name='Seg6LocalEncap.Srh.hmac', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_hmac', full_name='Seg6LocalEncap.Srh._hmac',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=485,
  serialized_end=536,
)

_SEG6LOCALENCAP = _descriptor.Descriptor(
  name='Seg6LocalEncap',
  full_name='Seg6LocalEncap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Seg6LocalEncap.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='Seg6LocalEncap.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nh6', full_name='Seg6LocalEncap.nh6', index=2,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nh4', full_name='Seg6LocalEncap.nh4', index=3,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='srh', full_name='Seg6LocalEncap.srh', index=4,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SEG6LOCALENCAP_SRH, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='param', full_name='Seg6LocalEncap.param',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=342,
  serialized_end=545,
)


_ROUTEREPLY = _descriptor.Descriptor(
  name='RouteReply',
  full_name='RouteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='RouteReply.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=575,
)


_SHOWROUTES6REQUEST = _descriptor.Descriptor(
  name='ShowRoutes6Request',
  full_name='ShowRoutes6Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=597,
)


_SHOWROUTES6REPLY = _descriptor.Descriptor(
  name='ShowRoutes6Reply',
  full_name='ShowRoutes6Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=617,
)

_ROUTE.fields_by_name['seg6_encap'].message_type = _SEG6ENCAP
_ROUTE.fields_by_name['seg6local_encap'].message_type = _SEG6LOCALENCAP
_ROUTE.oneofs_by_name['encap'].fields.append(
  _ROUTE.fields_by_name['seg6_encap'])
_ROUTE.fields_by_name['seg6_encap'].containing_oneof = _ROUTE.oneofs_by_name['encap']
_ROUTE.oneofs_by_name['encap'].fields.append(
  _ROUTE.fields_by_name['seg6local_encap'])
_ROUTE.fields_by_name['seg6local_encap'].containing_oneof = _ROUTE.oneofs_by_name['encap']
_ROUTE.oneofs_by_name['_gateway'].fields.append(
  _ROUTE.fields_by_name['gateway'])
_ROUTE.fields_by_name['gateway'].containing_oneof = _ROUTE.oneofs_by_name['_gateway']
_ROUTE.oneofs_by_name['_dev'].fields.append(
  _ROUTE.fields_by_name['dev'])
_ROUTE.fields_by_name['dev'].containing_oneof = _ROUTE.oneofs_by_name['_dev']
_ROUTE.oneofs_by_name['_metric'].fields.append(
  _ROUTE.fields_by_name['metric'])
_ROUTE.fields_by_name['metric'].containing_oneof = _ROUTE.oneofs_by_name['_metric']
_ROUTE.oneofs_by_name['_table'].fields.append(
  _ROUTE.fields_by_name['table'])
_ROUTE.fields_by_name['table'].containing_oneof = _ROUTE.oneofs_by_name['_table']
_SEG6ENCAP.fields_by_name['type'].enum_type = _SEG6TYPE
_SEG6ENCAP.fields_by_name['mode'].enum_type = _SEG6MODE
_SEG6LOCALENCAP_SRH.containing_type = _SEG6LOCALENCAP
_SEG6LOCALENCAP_SRH.oneofs_by_name['_hmac'].fields.append(
  _SEG6LOCALENCAP_SRH.fields_by_name['hmac'])
_SEG6LOCALENCAP_SRH.fields_by_name['hmac'].containing_oneof = _SEG6LOCALENCAP_SRH.oneofs_by_name['_hmac']
_SEG6LOCALENCAP.fields_by_name['type'].enum_type = _SEG6TYPE
_SEG6LOCALENCAP.fields_by_name['action'].enum_type = _SEG6LOCALACTION
_SEG6LOCALENCAP.fields_by_name['srh'].message_type = _SEG6LOCALENCAP_SRH
_SEG6LOCALENCAP.oneofs_by_name['param'].fields.append(
  _SEG6LOCALENCAP.fields_by_name['nh6'])
_SEG6LOCALENCAP.fields_by_name['nh6'].containing_oneof = _SEG6LOCALENCAP.oneofs_by_name['param']
_SEG6LOCALENCAP.oneofs_by_name['param'].fields.append(
  _SEG6LOCALENCAP.fields_by_name['nh4'])
_SEG6LOCALENCAP.fields_by_name['nh4'].containing_oneof = _SEG6LOCALENCAP.oneofs_by_name['param']
_SEG6LOCALENCAP.oneofs_by_name['param'].fields.append(
  _SEG6LOCALENCAP.fields_by_name['srh'])
_SEG6LOCALENCAP.fields_by_name['srh'].containing_oneof = _SEG6LOCALENCAP.oneofs_by_name['param']
DESCRIPTOR.message_types_by_name['Route'] = _ROUTE
DESCRIPTOR.message_types_by_name['Seg6Encap'] = _SEG6ENCAP
DESCRIPTOR.message_types_by_name['Seg6LocalEncap'] = _SEG6LOCALENCAP
DESCRIPTOR.message_types_by_name['RouteReply'] = _ROUTEREPLY
DESCRIPTOR.message_types_by_name['ShowRoutes6Request'] = _SHOWROUTES6REQUEST
DESCRIPTOR.message_types_by_name['ShowRoutes6Reply'] = _SHOWROUTES6REPLY
DESCRIPTOR.enum_types_by_name['Seg6Type'] = _SEG6TYPE
DESCRIPTOR.enum_types_by_name['Seg6Mode'] = _SEG6MODE
DESCRIPTOR.enum_types_by_name['Seg6LocalAction'] = _SEG6LOCALACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), {
  'DESCRIPTOR' : _ROUTE,
  '__module__' : 'srv6_route_pb2'
  # @@protoc_insertion_point(class_scope:Route)
  })
_sym_db.RegisterMessage(Route)

Seg6Encap = _reflection.GeneratedProtocolMessageType('Seg6Encap', (_message.Message,), {
  'DESCRIPTOR' : _SEG6ENCAP,
  '__module__' : 'srv6_route_pb2'
  # @@protoc_insertion_point(class_scope:Seg6Encap)
  })
_sym_db.RegisterMessage(Seg6Encap)

Seg6LocalEncap = _reflection.GeneratedProtocolMessageType('Seg6LocalEncap', (_message.Message,), {

  'Srh' : _reflection.GeneratedProtocolMessageType('Srh', (_message.Message,), {
    'DESCRIPTOR' : _SEG6LOCALENCAP_SRH,
    '__module__' : 'srv6_route_pb2'
    # @@protoc_insertion_point(class_scope:Seg6LocalEncap.Srh)
    })
  ,
  'DESCRIPTOR' : _SEG6LOCALENCAP,
  '__module__' : 'srv6_route_pb2'
  # @@protoc_insertion_point(class_scope:Seg6LocalEncap)
  })
_sym_db.RegisterMessage(Seg6LocalEncap)
_sym_db.RegisterMessage(Seg6LocalEncap.Srh)

RouteReply = _reflection.GeneratedProtocolMessageType('RouteReply', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEREPLY,
  '__module__' : 'srv6_route_pb2'
  # @@protoc_insertion_point(class_scope:RouteReply)
  })
_sym_db.RegisterMessage(RouteReply)

ShowRoutes6Request = _reflection.GeneratedProtocolMessageType('ShowRoutes6Request', (_message.Message,), {
  'DESCRIPTOR' : _SHOWROUTES6REQUEST,
  '__module__' : 'srv6_route_pb2'
  # @@protoc_insertion_point(class_scope:ShowRoutes6Request)
  })
_sym_db.RegisterMessage(ShowRoutes6Request)

ShowRoutes6Reply = _reflection.GeneratedProtocolMessageType('ShowRoutes6Reply', (_message.Message,), {
  'DESCRIPTOR' : _SHOWROUTES6REPLY,
  '__module__' : 'srv6_route_pb2'
  # @@protoc_insertion_point(class_scope:ShowRoutes6Reply)
  })
_sym_db.RegisterMessage(ShowRoutes6Reply)



_SEG6SERVICE = _descriptor.ServiceDescriptor(
  name='Seg6Service',
  full_name='Seg6Service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=801,
  serialized_end=936,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddRoute',
    full_name='Seg6Service.AddRoute',
    index=0,
    containing_service=None,
    input_type=_ROUTE,
    output_type=_ROUTEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveRoute',
    full_name='Seg6Service.RemoveRoute',
    index=1,
    containing_service=None,
    input_type=_ROUTE,
    output_type=_ROUTEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ShowRoute',
    full_name='Seg6Service.ShowRoute',
    index=2,
    containing_service=None,
    input_type=_SHOWROUTES6REQUEST,
    output_type=_SHOWROUTES6REPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEG6SERVICE)

DESCRIPTOR.services_by_name['Seg6Service'] = _SEG6SERVICE

# @@protoc_insertion_point(module_scope)
