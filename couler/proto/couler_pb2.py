# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/couler.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/couler.proto',
  package='couler.v1',
  syntax='proto3',
  serialized_options=_b('Z\tcouler/v1'),
  serialized_pb=_b('\n\x12proto/couler.proto\x12\tcouler.v1\x1a\x19google/protobuf/any.proto\"=\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x13\n\x0bglobal_name\x18\x03 \x01(\t\"2\n\x06Secret\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\xe3\x01\n\x08\x41rtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x12\n\nlocal_path\x18\x04 \x01(\t\x12\x13\n\x0bremote_path\x18\x05 \x01(\t\x12%\n\naccess_key\x18\x06 \x01(\x0b\x32\x11.couler.v1.Secret\x12%\n\nsecret_key\x18\x07 \x01(\x0b\x32\x11.couler.v1.Secret\x12\x10\n\x08\x65ndpoint\x18\x08 \x01(\t\x12\x0e\n\x06\x62ucket\x18\t \x01(\t\x12\x13\n\x0bglobal_name\x18\n \x01(\t\"\x16\n\x06StdOut\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xaa\x01\n\x06StepIO\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\x05\x12)\n\tparameter\x18\x03 \x01(\x0b\x32\x14.couler.v1.ParameterH\x00\x12\'\n\x08\x61rtifact\x18\x04 \x01(\x0b\x32\x13.couler.v1.ArtifactH\x00\x12#\n\x06stdout\x18\x05 \x01(\x0b\x32\x11.couler.v1.StdOutH\x00\x42\t\n\x07step_io\"\xa1\x01\n\rContainerSpec\x12\r\n\x05image\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x03(\t\x12.\n\x03\x65nv\x18\x03 \x03(\x0b\x32!.couler.v1.ContainerSpec.EnvEntry\x1a@\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"\x83\x01\n\x0cResourceSpec\x12\x10\n\x08manifest\x18\x01 \x01(\t\x12\x19\n\x11success_condition\x18\x02 \x01(\t\x12\x19\n\x11\x66\x61ilure_condition\x18\x03 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\t\x12\x1b\n\x13set_owner_reference\x18\x05 \x01(\x08\"\xea\x01\n\x04Step\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\ttmpl_name\x18\x03 \x01(\t\x12\x30\n\x0e\x63ontainer_spec\x18\x04 \x01(\x0b\x32\x18.couler.v1.ContainerSpec\x12.\n\rresource_spec\x18\x05 \x01(\x0b\x32\x17.couler.v1.ResourceSpec\x12\x0e\n\x06script\x18\x06 \x01(\t\x12\x1f\n\x04\x61rgs\x18\x07 \x03(\x0b\x32\x11.couler.v1.StepIO\x12\x14\n\x0c\x64\x65pendencies\x18\x08 \x03(\t\x12\x0c\n\x04when\x18\t \x01(\t\"1\n\x0f\x43oncurrentSteps\x12\x1e\n\x05steps\x18\x01 \x03(\x0b\x32\x0f.couler.v1.Step\"c\n\x0cStepTemplate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x06inputs\x18\x02 \x03(\x0b\x32\x11.couler.v1.StepIO\x12\"\n\x07outputs\x18\x03 \x03(\x0b\x32\x11.couler.v1.StepIO\"\x89\x02\n\x08Workflow\x12)\n\x05steps\x18\x01 \x03(\x0b\x32\x1a.couler.v1.ConcurrentSteps\x12\x35\n\ttemplates\x18\x02 \x03(\x0b\x32\".couler.v1.Workflow.TemplatesEntry\x12\x13\n\x0bparallelism\x18\x03 \x01(\x05\x12\x0e\n\x06secret\x18\x04 \x01(\t\x12+\n\x12\x65xit_handler_steps\x18\x05 \x03(\x0b\x32\x0f.couler.v1.Step\x1aI\n\x0eTemplatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.couler.v1.StepTemplate:\x02\x38\x01\x42\x0bZ\tcouler/v1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='couler.v1.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='couler.v1.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='couler.v1.Parameter.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_name', full_name='couler.v1.Parameter.global_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=60,
  serialized_end=121,
)


_SECRET = _descriptor.Descriptor(
  name='Secret',
  full_name='couler.v1.Secret',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='couler.v1.Secret.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='couler.v1.Secret.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='couler.v1.Secret.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=123,
  serialized_end=173,
)


_ARTIFACT = _descriptor.Descriptor(
  name='Artifact',
  full_name='couler.v1.Artifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='couler.v1.Artifact.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='couler.v1.Artifact.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='couler.v1.Artifact.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_path', full_name='couler.v1.Artifact.local_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_path', full_name='couler.v1.Artifact.remote_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_key', full_name='couler.v1.Artifact.access_key', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_key', full_name='couler.v1.Artifact.secret_key', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='couler.v1.Artifact.endpoint', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='couler.v1.Artifact.bucket', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_name', full_name='couler.v1.Artifact.global_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=176,
  serialized_end=403,
)


_STDOUT = _descriptor.Descriptor(
  name='StdOut',
  full_name='couler.v1.StdOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='couler.v1.StdOut.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=405,
  serialized_end=427,
)


_STEPIO = _descriptor.Descriptor(
  name='StepIO',
  full_name='couler.v1.StepIO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='couler.v1.StepIO.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='couler.v1.StepIO.source', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='couler.v1.StepIO.parameter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifact', full_name='couler.v1.StepIO.artifact', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stdout', full_name='couler.v1.StepIO.stdout', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
      name='step_io', full_name='couler.v1.StepIO.step_io',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=430,
  serialized_end=600,
)


_CONTAINERSPEC_ENVENTRY = _descriptor.Descriptor(
  name='EnvEntry',
  full_name='couler.v1.ContainerSpec.EnvEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='couler.v1.ContainerSpec.EnvEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='couler.v1.ContainerSpec.EnvEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=764,
)

_CONTAINERSPEC = _descriptor.Descriptor(
  name='ContainerSpec',
  full_name='couler.v1.ContainerSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='couler.v1.ContainerSpec.image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='couler.v1.ContainerSpec.command', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='couler.v1.ContainerSpec.env', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONTAINERSPEC_ENVENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=764,
)


_RESOURCESPEC = _descriptor.Descriptor(
  name='ResourceSpec',
  full_name='couler.v1.ResourceSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='manifest', full_name='couler.v1.ResourceSpec.manifest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success_condition', full_name='couler.v1.ResourceSpec.success_condition', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure_condition', full_name='couler.v1.ResourceSpec.failure_condition', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='couler.v1.ResourceSpec.action', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_owner_reference', full_name='couler.v1.ResourceSpec.set_owner_reference', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=767,
  serialized_end=898,
)


_STEP = _descriptor.Descriptor(
  name='Step',
  full_name='couler.v1.Step',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='couler.v1.Step.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='couler.v1.Step.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tmpl_name', full_name='couler.v1.Step.tmpl_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='container_spec', full_name='couler.v1.Step.container_spec', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_spec', full_name='couler.v1.Step.resource_spec', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='couler.v1.Step.script', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='couler.v1.Step.args', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='couler.v1.Step.dependencies', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='when', full_name='couler.v1.Step.when', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=901,
  serialized_end=1135,
)


_CONCURRENTSTEPS = _descriptor.Descriptor(
  name='ConcurrentSteps',
  full_name='couler.v1.ConcurrentSteps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steps', full_name='couler.v1.ConcurrentSteps.steps', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1137,
  serialized_end=1186,
)


_STEPTEMPLATE = _descriptor.Descriptor(
  name='StepTemplate',
  full_name='couler.v1.StepTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='couler.v1.StepTemplate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='couler.v1.StepTemplate.inputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='couler.v1.StepTemplate.outputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1188,
  serialized_end=1287,
)


_WORKFLOW_TEMPLATESENTRY = _descriptor.Descriptor(
  name='TemplatesEntry',
  full_name='couler.v1.Workflow.TemplatesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='couler.v1.Workflow.TemplatesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='couler.v1.Workflow.TemplatesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1482,
  serialized_end=1555,
)

_WORKFLOW = _descriptor.Descriptor(
  name='Workflow',
  full_name='couler.v1.Workflow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steps', full_name='couler.v1.Workflow.steps', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templates', full_name='couler.v1.Workflow.templates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parallelism', full_name='couler.v1.Workflow.parallelism', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret', full_name='couler.v1.Workflow.secret', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_handler_steps', full_name='couler.v1.Workflow.exit_handler_steps', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORKFLOW_TEMPLATESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1290,
  serialized_end=1555,
)

_ARTIFACT.fields_by_name['access_key'].message_type = _SECRET
_ARTIFACT.fields_by_name['secret_key'].message_type = _SECRET
_STEPIO.fields_by_name['parameter'].message_type = _PARAMETER
_STEPIO.fields_by_name['artifact'].message_type = _ARTIFACT
_STEPIO.fields_by_name['stdout'].message_type = _STDOUT
_STEPIO.oneofs_by_name['step_io'].fields.append(
  _STEPIO.fields_by_name['parameter'])
_STEPIO.fields_by_name['parameter'].containing_oneof = _STEPIO.oneofs_by_name['step_io']
_STEPIO.oneofs_by_name['step_io'].fields.append(
  _STEPIO.fields_by_name['artifact'])
_STEPIO.fields_by_name['artifact'].containing_oneof = _STEPIO.oneofs_by_name['step_io']
_STEPIO.oneofs_by_name['step_io'].fields.append(
  _STEPIO.fields_by_name['stdout'])
_STEPIO.fields_by_name['stdout'].containing_oneof = _STEPIO.oneofs_by_name['step_io']
_CONTAINERSPEC_ENVENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONTAINERSPEC_ENVENTRY.containing_type = _CONTAINERSPEC
_CONTAINERSPEC.fields_by_name['env'].message_type = _CONTAINERSPEC_ENVENTRY
_STEP.fields_by_name['container_spec'].message_type = _CONTAINERSPEC
_STEP.fields_by_name['resource_spec'].message_type = _RESOURCESPEC
_STEP.fields_by_name['args'].message_type = _STEPIO
_CONCURRENTSTEPS.fields_by_name['steps'].message_type = _STEP
_STEPTEMPLATE.fields_by_name['inputs'].message_type = _STEPIO
_STEPTEMPLATE.fields_by_name['outputs'].message_type = _STEPIO
_WORKFLOW_TEMPLATESENTRY.fields_by_name['value'].message_type = _STEPTEMPLATE
_WORKFLOW_TEMPLATESENTRY.containing_type = _WORKFLOW
_WORKFLOW.fields_by_name['steps'].message_type = _CONCURRENTSTEPS
_WORKFLOW.fields_by_name['templates'].message_type = _WORKFLOW_TEMPLATESENTRY
_WORKFLOW.fields_by_name['exit_handler_steps'].message_type = _STEP
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['Secret'] = _SECRET
DESCRIPTOR.message_types_by_name['Artifact'] = _ARTIFACT
DESCRIPTOR.message_types_by_name['StdOut'] = _STDOUT
DESCRIPTOR.message_types_by_name['StepIO'] = _STEPIO
DESCRIPTOR.message_types_by_name['ContainerSpec'] = _CONTAINERSPEC
DESCRIPTOR.message_types_by_name['ResourceSpec'] = _RESOURCESPEC
DESCRIPTOR.message_types_by_name['Step'] = _STEP
DESCRIPTOR.message_types_by_name['ConcurrentSteps'] = _CONCURRENTSTEPS
DESCRIPTOR.message_types_by_name['StepTemplate'] = _STEPTEMPLATE
DESCRIPTOR.message_types_by_name['Workflow'] = _WORKFLOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETER,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.Parameter)
  ))
_sym_db.RegisterMessage(Parameter)

Secret = _reflection.GeneratedProtocolMessageType('Secret', (_message.Message,), dict(
  DESCRIPTOR = _SECRET,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.Secret)
  ))
_sym_db.RegisterMessage(Secret)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), dict(
  DESCRIPTOR = _ARTIFACT,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.Artifact)
  ))
_sym_db.RegisterMessage(Artifact)

StdOut = _reflection.GeneratedProtocolMessageType('StdOut', (_message.Message,), dict(
  DESCRIPTOR = _STDOUT,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.StdOut)
  ))
_sym_db.RegisterMessage(StdOut)

StepIO = _reflection.GeneratedProtocolMessageType('StepIO', (_message.Message,), dict(
  DESCRIPTOR = _STEPIO,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.StepIO)
  ))
_sym_db.RegisterMessage(StepIO)

ContainerSpec = _reflection.GeneratedProtocolMessageType('ContainerSpec', (_message.Message,), dict(

  EnvEntry = _reflection.GeneratedProtocolMessageType('EnvEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONTAINERSPEC_ENVENTRY,
    __module__ = 'proto.couler_pb2'
    # @@protoc_insertion_point(class_scope:couler.v1.ContainerSpec.EnvEntry)
    ))
  ,
  DESCRIPTOR = _CONTAINERSPEC,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.ContainerSpec)
  ))
_sym_db.RegisterMessage(ContainerSpec)
_sym_db.RegisterMessage(ContainerSpec.EnvEntry)

ResourceSpec = _reflection.GeneratedProtocolMessageType('ResourceSpec', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCESPEC,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.ResourceSpec)
  ))
_sym_db.RegisterMessage(ResourceSpec)

Step = _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), dict(
  DESCRIPTOR = _STEP,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.Step)
  ))
_sym_db.RegisterMessage(Step)

ConcurrentSteps = _reflection.GeneratedProtocolMessageType('ConcurrentSteps', (_message.Message,), dict(
  DESCRIPTOR = _CONCURRENTSTEPS,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.ConcurrentSteps)
  ))
_sym_db.RegisterMessage(ConcurrentSteps)

StepTemplate = _reflection.GeneratedProtocolMessageType('StepTemplate', (_message.Message,), dict(
  DESCRIPTOR = _STEPTEMPLATE,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.StepTemplate)
  ))
_sym_db.RegisterMessage(StepTemplate)

Workflow = _reflection.GeneratedProtocolMessageType('Workflow', (_message.Message,), dict(

  TemplatesEntry = _reflection.GeneratedProtocolMessageType('TemplatesEntry', (_message.Message,), dict(
    DESCRIPTOR = _WORKFLOW_TEMPLATESENTRY,
    __module__ = 'proto.couler_pb2'
    # @@protoc_insertion_point(class_scope:couler.v1.Workflow.TemplatesEntry)
    ))
  ,
  DESCRIPTOR = _WORKFLOW,
  __module__ = 'proto.couler_pb2'
  # @@protoc_insertion_point(class_scope:couler.v1.Workflow)
  ))
_sym_db.RegisterMessage(Workflow)
_sym_db.RegisterMessage(Workflow.TemplatesEntry)


DESCRIPTOR._options = None
_CONTAINERSPEC_ENVENTRY._options = None
_WORKFLOW_TEMPLATESENTRY._options = None
# @@protoc_insertion_point(module_scope)