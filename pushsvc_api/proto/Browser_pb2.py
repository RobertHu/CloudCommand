# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Browser.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Browser.proto',
  package='',
  serialized_pb='\n\rBrowser.proto\"U\n\nReqSiteCmd\x12&\n\x08siteType\x18\x01 \x02(\x0e\x32\x14.ReqSiteCmd.SiteType\"\x1f\n\x08SiteType\x12\n\n\x06\x43OMMON\x10\x00\x12\x07\n\x03\x41LL\x10\x01\"P\n\nRspSiteCmd\x12\x0f\n\x07rescode\x18\x01 \x02(\x05\x12\x0e\n\x06resmsg\x18\x02 \x02(\t\x12!\n\x0b\x63\x61tegoryCmd\x18\x03 \x03(\x0b\x32\x0c.CategoryCmd\"N\n\x0b\x43\x61tegoryCmd\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x31\n\x13sitesPerCategoryCmd\x18\x02 \x03(\x0b\x32\x14.SitesPerCategoryCmd\">\n\x13SitesPerCategoryCmd\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x19\n\x07siteCmd\x18\x02 \x03(\x0b\x32\x08.SiteCmd\"5\n\x07SiteCmd\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0b\n\x03url\x18\x02 \x02(\t\x12\x0f\n\x07iconUrl\x18\x03 \x01(\t\"\x14\n\x12ReqSearchEngineCmd\"l\n\x12RspSearchEngineCmd\x12\x0f\n\x07rescode\x18\x01 \x02(\x05\x12\x0e\n\x06resmsg\x18\x02 \x02(\t\x12\x35\n\x15searchEngineConfigCmd\x18\x03 \x03(\x0b\x32\x16.SearchEngineConfigCmd\"v\n\x15SearchEngineConfigCmd\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07iconUrl\x18\x02 \x02(\t\x12\x0b\n\x03url\x18\x03 \x02(\t\x12\x0b\n\x03pos\x18\x04 \x02(\x05\x12\x11\n\tisEnabled\x18\x05 \x02(\x08\x12\x11\n\tisDefault\x18\x06 \x02(\x08\"#\n\x10ReqSearchWordCmd\x12\x0f\n\x07keyword\x18\x01 \x02(\t\"`\n\x10RspSearchWordCmd\x12\x0f\n\x07rescode\x18\x01 \x02(\x05\x12\x0e\n\x06resmsg\x18\x02 \x02(\t\x12+\n\x10keyWordConfigCmd\x18\x03 \x01(\x0b\x32\x11.KeyWordConfigCmd\"Z\n\x10KeyWordConfigCmd\x12\x33\n\x14keyWordConfigItemCmd\x18\x01 \x03(\x0b\x32\x15.KeyWordConfigItemCmd\x12\x11\n\tisEnabled\x18\x02 \x02(\x08\"1\n\x14KeyWordConfigItemCmd\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0b\n\x03url\x18\x02 \x02(\t\"]\n\x17ReqProcessSearchWordCmd\x12\x0f\n\x07keyword\x18\x01 \x02(\t\x12\x18\n\x10searchEngineName\x18\x02 \x02(\t\x12\x17\n\x0fsearchEngineUrl\x18\x03 \x01(\t\"J\n\x17RspProcessSearchWordCmd\x12\x0f\n\x07rescode\x18\x01 \x02(\x05\x12\x0e\n\x06resmsg\x18\x02 \x02(\t\x12\x0e\n\x06result\x18\x03 \x01(\t')



_REQSITECMD_SITETYPE = _descriptor.EnumDescriptor(
  name='SiteType',
  full_name='ReqSiteCmd.SiteType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMMON', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=71,
  serialized_end=102,
)


_REQSITECMD = _descriptor.Descriptor(
  name='ReqSiteCmd',
  full_name='ReqSiteCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='siteType', full_name='ReqSiteCmd.siteType', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQSITECMD_SITETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=17,
  serialized_end=102,
)


_RSPSITECMD = _descriptor.Descriptor(
  name='RspSiteCmd',
  full_name='RspSiteCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rescode', full_name='RspSiteCmd.rescode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resmsg', full_name='RspSiteCmd.resmsg', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='categoryCmd', full_name='RspSiteCmd.categoryCmd', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=104,
  serialized_end=184,
)


_CATEGORYCMD = _descriptor.Descriptor(
  name='CategoryCmd',
  full_name='CategoryCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CategoryCmd.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sitesPerCategoryCmd', full_name='CategoryCmd.sitesPerCategoryCmd', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=186,
  serialized_end=264,
)


_SITESPERCATEGORYCMD = _descriptor.Descriptor(
  name='SitesPerCategoryCmd',
  full_name='SitesPerCategoryCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SitesPerCategoryCmd.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteCmd', full_name='SitesPerCategoryCmd.siteCmd', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=266,
  serialized_end=328,
)


_SITECMD = _descriptor.Descriptor(
  name='SiteCmd',
  full_name='SiteCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SiteCmd.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='SiteCmd.url', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iconUrl', full_name='SiteCmd.iconUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=330,
  serialized_end=383,
)


_REQSEARCHENGINECMD = _descriptor.Descriptor(
  name='ReqSearchEngineCmd',
  full_name='ReqSearchEngineCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=385,
  serialized_end=405,
)


_RSPSEARCHENGINECMD = _descriptor.Descriptor(
  name='RspSearchEngineCmd',
  full_name='RspSearchEngineCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rescode', full_name='RspSearchEngineCmd.rescode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resmsg', full_name='RspSearchEngineCmd.resmsg', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='searchEngineConfigCmd', full_name='RspSearchEngineCmd.searchEngineConfigCmd', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=407,
  serialized_end=515,
)


_SEARCHENGINECONFIGCMD = _descriptor.Descriptor(
  name='SearchEngineConfigCmd',
  full_name='SearchEngineConfigCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SearchEngineConfigCmd.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iconUrl', full_name='SearchEngineConfigCmd.iconUrl', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='SearchEngineConfigCmd.url', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos', full_name='SearchEngineConfigCmd.pos', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isEnabled', full_name='SearchEngineConfigCmd.isEnabled', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isDefault', full_name='SearchEngineConfigCmd.isDefault', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=517,
  serialized_end=635,
)


_REQSEARCHWORDCMD = _descriptor.Descriptor(
  name='ReqSearchWordCmd',
  full_name='ReqSearchWordCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword', full_name='ReqSearchWordCmd.keyword', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=637,
  serialized_end=672,
)


_RSPSEARCHWORDCMD = _descriptor.Descriptor(
  name='RspSearchWordCmd',
  full_name='RspSearchWordCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rescode', full_name='RspSearchWordCmd.rescode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resmsg', full_name='RspSearchWordCmd.resmsg', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyWordConfigCmd', full_name='RspSearchWordCmd.keyWordConfigCmd', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=674,
  serialized_end=770,
)


_KEYWORDCONFIGCMD = _descriptor.Descriptor(
  name='KeyWordConfigCmd',
  full_name='KeyWordConfigCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyWordConfigItemCmd', full_name='KeyWordConfigCmd.keyWordConfigItemCmd', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isEnabled', full_name='KeyWordConfigCmd.isEnabled', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=772,
  serialized_end=862,
)


_KEYWORDCONFIGITEMCMD = _descriptor.Descriptor(
  name='KeyWordConfigItemCmd',
  full_name='KeyWordConfigItemCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='KeyWordConfigItemCmd.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='KeyWordConfigItemCmd.url', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=864,
  serialized_end=913,
)


_REQPROCESSSEARCHWORDCMD = _descriptor.Descriptor(
  name='ReqProcessSearchWordCmd',
  full_name='ReqProcessSearchWordCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword', full_name='ReqProcessSearchWordCmd.keyword', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='searchEngineName', full_name='ReqProcessSearchWordCmd.searchEngineName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='searchEngineUrl', full_name='ReqProcessSearchWordCmd.searchEngineUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=915,
  serialized_end=1008,
)


_RSPPROCESSSEARCHWORDCMD = _descriptor.Descriptor(
  name='RspProcessSearchWordCmd',
  full_name='RspProcessSearchWordCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rescode', full_name='RspProcessSearchWordCmd.rescode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resmsg', full_name='RspProcessSearchWordCmd.resmsg', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='RspProcessSearchWordCmd.result', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1010,
  serialized_end=1084,
)

_REQSITECMD.fields_by_name['siteType'].enum_type = _REQSITECMD_SITETYPE
_REQSITECMD_SITETYPE.containing_type = _REQSITECMD;
_RSPSITECMD.fields_by_name['categoryCmd'].message_type = _CATEGORYCMD
_CATEGORYCMD.fields_by_name['sitesPerCategoryCmd'].message_type = _SITESPERCATEGORYCMD
_SITESPERCATEGORYCMD.fields_by_name['siteCmd'].message_type = _SITECMD
_RSPSEARCHENGINECMD.fields_by_name['searchEngineConfigCmd'].message_type = _SEARCHENGINECONFIGCMD
_RSPSEARCHWORDCMD.fields_by_name['keyWordConfigCmd'].message_type = _KEYWORDCONFIGCMD
_KEYWORDCONFIGCMD.fields_by_name['keyWordConfigItemCmd'].message_type = _KEYWORDCONFIGITEMCMD
DESCRIPTOR.message_types_by_name['ReqSiteCmd'] = _REQSITECMD
DESCRIPTOR.message_types_by_name['RspSiteCmd'] = _RSPSITECMD
DESCRIPTOR.message_types_by_name['CategoryCmd'] = _CATEGORYCMD
DESCRIPTOR.message_types_by_name['SitesPerCategoryCmd'] = _SITESPERCATEGORYCMD
DESCRIPTOR.message_types_by_name['SiteCmd'] = _SITECMD
DESCRIPTOR.message_types_by_name['ReqSearchEngineCmd'] = _REQSEARCHENGINECMD
DESCRIPTOR.message_types_by_name['RspSearchEngineCmd'] = _RSPSEARCHENGINECMD
DESCRIPTOR.message_types_by_name['SearchEngineConfigCmd'] = _SEARCHENGINECONFIGCMD
DESCRIPTOR.message_types_by_name['ReqSearchWordCmd'] = _REQSEARCHWORDCMD
DESCRIPTOR.message_types_by_name['RspSearchWordCmd'] = _RSPSEARCHWORDCMD
DESCRIPTOR.message_types_by_name['KeyWordConfigCmd'] = _KEYWORDCONFIGCMD
DESCRIPTOR.message_types_by_name['KeyWordConfigItemCmd'] = _KEYWORDCONFIGITEMCMD
DESCRIPTOR.message_types_by_name['ReqProcessSearchWordCmd'] = _REQPROCESSSEARCHWORDCMD
DESCRIPTOR.message_types_by_name['RspProcessSearchWordCmd'] = _RSPPROCESSSEARCHWORDCMD

class ReqSiteCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQSITECMD

  # @@protoc_insertion_point(class_scope:ReqSiteCmd)

class RspSiteCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RSPSITECMD

  # @@protoc_insertion_point(class_scope:RspSiteCmd)

class CategoryCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CATEGORYCMD

  # @@protoc_insertion_point(class_scope:CategoryCmd)

class SitesPerCategoryCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SITESPERCATEGORYCMD

  # @@protoc_insertion_point(class_scope:SitesPerCategoryCmd)

class SiteCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SITECMD

  # @@protoc_insertion_point(class_scope:SiteCmd)

class ReqSearchEngineCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQSEARCHENGINECMD

  # @@protoc_insertion_point(class_scope:ReqSearchEngineCmd)

class RspSearchEngineCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RSPSEARCHENGINECMD

  # @@protoc_insertion_point(class_scope:RspSearchEngineCmd)

class SearchEngineConfigCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SEARCHENGINECONFIGCMD

  # @@protoc_insertion_point(class_scope:SearchEngineConfigCmd)

class ReqSearchWordCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQSEARCHWORDCMD

  # @@protoc_insertion_point(class_scope:ReqSearchWordCmd)

class RspSearchWordCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RSPSEARCHWORDCMD

  # @@protoc_insertion_point(class_scope:RspSearchWordCmd)

class KeyWordConfigCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEYWORDCONFIGCMD

  # @@protoc_insertion_point(class_scope:KeyWordConfigCmd)

class KeyWordConfigItemCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEYWORDCONFIGITEMCMD

  # @@protoc_insertion_point(class_scope:KeyWordConfigItemCmd)

class ReqProcessSearchWordCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQPROCESSSEARCHWORDCMD

  # @@protoc_insertion_point(class_scope:ReqProcessSearchWordCmd)

class RspProcessSearchWordCmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RSPPROCESSSEARCHWORDCMD

  # @@protoc_insertion_point(class_scope:RspProcessSearchWordCmd)


# @@protoc_insertion_point(module_scope)