// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: flwr/proto/fab.proto

#include "flwr/proto/fab.pb.h"

#include <algorithm>

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>

PROTOBUF_PRAGMA_INIT_SEG
namespace flwr {
namespace proto {
constexpr Fab::Fab(
  ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized)
  : hash_str_(&::PROTOBUF_NAMESPACE_ID::internal::fixed_address_empty_string)
  , content_(&::PROTOBUF_NAMESPACE_ID::internal::fixed_address_empty_string){}
struct FabDefaultTypeInternal {
  constexpr FabDefaultTypeInternal()
    : _instance(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized{}) {}
  ~FabDefaultTypeInternal() {}
  union {
    Fab _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT FabDefaultTypeInternal _Fab_default_instance_;
constexpr GetFabRequest::GetFabRequest(
  ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized)
  : hash_str_(&::PROTOBUF_NAMESPACE_ID::internal::fixed_address_empty_string)
  , node_(nullptr){}
struct GetFabRequestDefaultTypeInternal {
  constexpr GetFabRequestDefaultTypeInternal()
    : _instance(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized{}) {}
  ~GetFabRequestDefaultTypeInternal() {}
  union {
    GetFabRequest _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT GetFabRequestDefaultTypeInternal _GetFabRequest_default_instance_;
constexpr GetFabResponse::GetFabResponse(
  ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized)
  : fab_(nullptr){}
struct GetFabResponseDefaultTypeInternal {
  constexpr GetFabResponseDefaultTypeInternal()
    : _instance(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized{}) {}
  ~GetFabResponseDefaultTypeInternal() {}
  union {
    GetFabResponse _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT GetFabResponseDefaultTypeInternal _GetFabResponse_default_instance_;
}  // namespace proto
}  // namespace flwr
static ::PROTOBUF_NAMESPACE_ID::Metadata file_level_metadata_flwr_2fproto_2ffab_2eproto[3];
static constexpr ::PROTOBUF_NAMESPACE_ID::EnumDescriptor const** file_level_enum_descriptors_flwr_2fproto_2ffab_2eproto = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_flwr_2fproto_2ffab_2eproto = nullptr;

const ::PROTOBUF_NAMESPACE_ID::uint32 TableStruct_flwr_2fproto_2ffab_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::flwr::proto::Fab, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  PROTOBUF_FIELD_OFFSET(::flwr::proto::Fab, hash_str_),
  PROTOBUF_FIELD_OFFSET(::flwr::proto::Fab, content_),
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::flwr::proto::GetFabRequest, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  PROTOBUF_FIELD_OFFSET(::flwr::proto::GetFabRequest, node_),
  PROTOBUF_FIELD_OFFSET(::flwr::proto::GetFabRequest, hash_str_),
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::flwr::proto::GetFabResponse, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  PROTOBUF_FIELD_OFFSET(::flwr::proto::GetFabResponse, fab_),
};
static const ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, -1, sizeof(::flwr::proto::Fab)},
  { 8, -1, -1, sizeof(::flwr::proto::GetFabRequest)},
  { 16, -1, -1, sizeof(::flwr::proto::GetFabResponse)},
};

static ::PROTOBUF_NAMESPACE_ID::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::flwr::proto::_Fab_default_instance_),
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::flwr::proto::_GetFabRequest_default_instance_),
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::flwr::proto::_GetFabResponse_default_instance_),
};

const char descriptor_table_protodef_flwr_2fproto_2ffab_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\024flwr/proto/fab.proto\022\nflwr.proto\032\025flwr"
  "/proto/node.proto\"(\n\003Fab\022\020\n\010hash_str\030\001 \001"
  "(\t\022\017\n\007content\030\002 \001(\014\"A\n\rGetFabRequest\022\036\n\004"
  "node\030\001 \001(\0132\020.flwr.proto.Node\022\020\n\010hash_str"
  "\030\002 \001(\t\".\n\016GetFabResponse\022\034\n\003fab\030\001 \001(\0132\017."
  "flwr.proto.Fabb\006proto3"
  ;
static const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable*const descriptor_table_flwr_2fproto_2ffab_2eproto_deps[1] = {
  &::descriptor_table_flwr_2fproto_2fnode_2eproto,
};
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_flwr_2fproto_2ffab_2eproto_once;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_flwr_2fproto_2ffab_2eproto = {
  false, false, 222, descriptor_table_protodef_flwr_2fproto_2ffab_2eproto, "flwr/proto/fab.proto", 
  &descriptor_table_flwr_2fproto_2ffab_2eproto_once, descriptor_table_flwr_2fproto_2ffab_2eproto_deps, 1, 3,
  schemas, file_default_instances, TableStruct_flwr_2fproto_2ffab_2eproto::offsets,
  file_level_metadata_flwr_2fproto_2ffab_2eproto, file_level_enum_descriptors_flwr_2fproto_2ffab_2eproto, file_level_service_descriptors_flwr_2fproto_2ffab_2eproto,
};
PROTOBUF_ATTRIBUTE_WEAK const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable* descriptor_table_flwr_2fproto_2ffab_2eproto_getter() {
  return &descriptor_table_flwr_2fproto_2ffab_2eproto;
}

// Force running AddDescriptors() at dynamic initialization time.
PROTOBUF_ATTRIBUTE_INIT_PRIORITY static ::PROTOBUF_NAMESPACE_ID::internal::AddDescriptorsRunner dynamic_init_dummy_flwr_2fproto_2ffab_2eproto(&descriptor_table_flwr_2fproto_2ffab_2eproto);
namespace flwr {
namespace proto {

// ===================================================================

class Fab::_Internal {
 public:
};

Fab::Fab(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena, is_message_owned) {
  SharedCtor();
  if (!is_message_owned) {
    RegisterArenaDtor(arena);
  }
  // @@protoc_insertion_point(arena_constructor:flwr.proto.Fab)
}
Fab::Fab(const Fab& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  hash_str_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (!from._internal_hash_str().empty()) {
    hash_str_.Set(::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::EmptyDefault{}, from._internal_hash_str(), 
      GetArenaForAllocation());
  }
  content_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (!from._internal_content().empty()) {
    content_.Set(::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::EmptyDefault{}, from._internal_content(), 
      GetArenaForAllocation());
  }
  // @@protoc_insertion_point(copy_constructor:flwr.proto.Fab)
}

void Fab::SharedCtor() {
hash_str_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
content_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}

Fab::~Fab() {
  // @@protoc_insertion_point(destructor:flwr.proto.Fab)
  if (GetArenaForAllocation() != nullptr) return;
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

inline void Fab::SharedDtor() {
  GOOGLE_DCHECK(GetArenaForAllocation() == nullptr);
  hash_str_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  content_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}

void Fab::ArenaDtor(void* object) {
  Fab* _this = reinterpret_cast< Fab* >(object);
  (void)_this;
}
void Fab::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void Fab::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}

void Fab::Clear() {
// @@protoc_insertion_point(message_clear_start:flwr.proto.Fab)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  hash_str_.ClearToEmpty();
  content_.ClearToEmpty();
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* Fab::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    switch (tag >> 3) {
      // string hash_str = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 10)) {
          auto str = _internal_mutable_hash_str();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(::PROTOBUF_NAMESPACE_ID::internal::VerifyUTF8(str, "flwr.proto.Fab.hash_str"));
          CHK_(ptr);
        } else
          goto handle_unusual;
        continue;
      // bytes content = 2;
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 18)) {
          auto str = _internal_mutable_content();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(ptr);
        } else
          goto handle_unusual;
        continue;
      default:
        goto handle_unusual;
    }  // switch
  handle_unusual:
    if ((tag == 0) || ((tag & 7) == 4)) {
      CHK_(ptr);
      ctx->SetLastTag(tag);
      goto message_done;
    }
    ptr = UnknownFieldParse(
        tag,
        _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
        ptr, ctx);
    CHK_(ptr != nullptr);
  }  // while
message_done:
  return ptr;
failure:
  ptr = nullptr;
  goto message_done;
#undef CHK_
}

::PROTOBUF_NAMESPACE_ID::uint8* Fab::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:flwr.proto.Fab)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // string hash_str = 1;
  if (!this->_internal_hash_str().empty()) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_hash_str().data(), static_cast<int>(this->_internal_hash_str().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "flwr.proto.Fab.hash_str");
    target = stream->WriteStringMaybeAliased(
        1, this->_internal_hash_str(), target);
  }

  // bytes content = 2;
  if (!this->_internal_content().empty()) {
    target = stream->WriteBytesMaybeAliased(
        2, this->_internal_content(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:flwr.proto.Fab)
  return target;
}

size_t Fab::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:flwr.proto.Fab)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // string hash_str = 1;
  if (!this->_internal_hash_str().empty()) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
        this->_internal_hash_str());
  }

  // bytes content = 2;
  if (!this->_internal_content().empty()) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::BytesSize(
        this->_internal_content());
  }

  return MaybeComputeUnknownFieldsSize(total_size, &_cached_size_);
}

const ::PROTOBUF_NAMESPACE_ID::Message::ClassData Fab::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::Message::CopyWithSizeCheck,
    Fab::MergeImpl
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*Fab::GetClassData() const { return &_class_data_; }

void Fab::MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to,
                      const ::PROTOBUF_NAMESPACE_ID::Message& from) {
  static_cast<Fab *>(to)->MergeFrom(
      static_cast<const Fab &>(from));
}


void Fab::MergeFrom(const Fab& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:flwr.proto.Fab)
  GOOGLE_DCHECK_NE(&from, this);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (!from._internal_hash_str().empty()) {
    _internal_set_hash_str(from._internal_hash_str());
  }
  if (!from._internal_content().empty()) {
    _internal_set_content(from._internal_content());
  }
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
}

void Fab::CopyFrom(const Fab& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:flwr.proto.Fab)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool Fab::IsInitialized() const {
  return true;
}

void Fab::InternalSwap(Fab* other) {
  using std::swap;
  auto* lhs_arena = GetArenaForAllocation();
  auto* rhs_arena = other->GetArenaForAllocation();
  _internal_metadata_.InternalSwap(&other->_internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::InternalSwap(
      &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      &hash_str_, lhs_arena,
      &other->hash_str_, rhs_arena
  );
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::InternalSwap(
      &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      &content_, lhs_arena,
      &other->content_, rhs_arena
  );
}

::PROTOBUF_NAMESPACE_ID::Metadata Fab::GetMetadata() const {
  return ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(
      &descriptor_table_flwr_2fproto_2ffab_2eproto_getter, &descriptor_table_flwr_2fproto_2ffab_2eproto_once,
      file_level_metadata_flwr_2fproto_2ffab_2eproto[0]);
}

// ===================================================================

class GetFabRequest::_Internal {
 public:
  static const ::flwr::proto::Node& node(const GetFabRequest* msg);
};

const ::flwr::proto::Node&
GetFabRequest::_Internal::node(const GetFabRequest* msg) {
  return *msg->node_;
}
void GetFabRequest::clear_node() {
  if (GetArenaForAllocation() == nullptr && node_ != nullptr) {
    delete node_;
  }
  node_ = nullptr;
}
GetFabRequest::GetFabRequest(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena, is_message_owned) {
  SharedCtor();
  if (!is_message_owned) {
    RegisterArenaDtor(arena);
  }
  // @@protoc_insertion_point(arena_constructor:flwr.proto.GetFabRequest)
}
GetFabRequest::GetFabRequest(const GetFabRequest& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  hash_str_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (!from._internal_hash_str().empty()) {
    hash_str_.Set(::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::EmptyDefault{}, from._internal_hash_str(), 
      GetArenaForAllocation());
  }
  if (from._internal_has_node()) {
    node_ = new ::flwr::proto::Node(*from.node_);
  } else {
    node_ = nullptr;
  }
  // @@protoc_insertion_point(copy_constructor:flwr.proto.GetFabRequest)
}

void GetFabRequest::SharedCtor() {
hash_str_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
node_ = nullptr;
}

GetFabRequest::~GetFabRequest() {
  // @@protoc_insertion_point(destructor:flwr.proto.GetFabRequest)
  if (GetArenaForAllocation() != nullptr) return;
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

inline void GetFabRequest::SharedDtor() {
  GOOGLE_DCHECK(GetArenaForAllocation() == nullptr);
  hash_str_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (this != internal_default_instance()) delete node_;
}

void GetFabRequest::ArenaDtor(void* object) {
  GetFabRequest* _this = reinterpret_cast< GetFabRequest* >(object);
  (void)_this;
}
void GetFabRequest::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void GetFabRequest::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}

void GetFabRequest::Clear() {
// @@protoc_insertion_point(message_clear_start:flwr.proto.GetFabRequest)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  hash_str_.ClearToEmpty();
  if (GetArenaForAllocation() == nullptr && node_ != nullptr) {
    delete node_;
  }
  node_ = nullptr;
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* GetFabRequest::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    switch (tag >> 3) {
      // .flwr.proto.Node node = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 10)) {
          ptr = ctx->ParseMessage(_internal_mutable_node(), ptr);
          CHK_(ptr);
        } else
          goto handle_unusual;
        continue;
      // string hash_str = 2;
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 18)) {
          auto str = _internal_mutable_hash_str();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(::PROTOBUF_NAMESPACE_ID::internal::VerifyUTF8(str, "flwr.proto.GetFabRequest.hash_str"));
          CHK_(ptr);
        } else
          goto handle_unusual;
        continue;
      default:
        goto handle_unusual;
    }  // switch
  handle_unusual:
    if ((tag == 0) || ((tag & 7) == 4)) {
      CHK_(ptr);
      ctx->SetLastTag(tag);
      goto message_done;
    }
    ptr = UnknownFieldParse(
        tag,
        _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
        ptr, ctx);
    CHK_(ptr != nullptr);
  }  // while
message_done:
  return ptr;
failure:
  ptr = nullptr;
  goto message_done;
#undef CHK_
}

::PROTOBUF_NAMESPACE_ID::uint8* GetFabRequest::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:flwr.proto.GetFabRequest)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .flwr.proto.Node node = 1;
  if (this->_internal_has_node()) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::
      InternalWriteMessage(
        1, _Internal::node(this), target, stream);
  }

  // string hash_str = 2;
  if (!this->_internal_hash_str().empty()) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_hash_str().data(), static_cast<int>(this->_internal_hash_str().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "flwr.proto.GetFabRequest.hash_str");
    target = stream->WriteStringMaybeAliased(
        2, this->_internal_hash_str(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:flwr.proto.GetFabRequest)
  return target;
}

size_t GetFabRequest::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:flwr.proto.GetFabRequest)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // string hash_str = 2;
  if (!this->_internal_hash_str().empty()) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
        this->_internal_hash_str());
  }

  // .flwr.proto.Node node = 1;
  if (this->_internal_has_node()) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::MessageSize(
        *node_);
  }

  return MaybeComputeUnknownFieldsSize(total_size, &_cached_size_);
}

const ::PROTOBUF_NAMESPACE_ID::Message::ClassData GetFabRequest::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::Message::CopyWithSizeCheck,
    GetFabRequest::MergeImpl
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetFabRequest::GetClassData() const { return &_class_data_; }

void GetFabRequest::MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to,
                      const ::PROTOBUF_NAMESPACE_ID::Message& from) {
  static_cast<GetFabRequest *>(to)->MergeFrom(
      static_cast<const GetFabRequest &>(from));
}


void GetFabRequest::MergeFrom(const GetFabRequest& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:flwr.proto.GetFabRequest)
  GOOGLE_DCHECK_NE(&from, this);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (!from._internal_hash_str().empty()) {
    _internal_set_hash_str(from._internal_hash_str());
  }
  if (from._internal_has_node()) {
    _internal_mutable_node()->::flwr::proto::Node::MergeFrom(from._internal_node());
  }
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
}

void GetFabRequest::CopyFrom(const GetFabRequest& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:flwr.proto.GetFabRequest)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool GetFabRequest::IsInitialized() const {
  return true;
}

void GetFabRequest::InternalSwap(GetFabRequest* other) {
  using std::swap;
  auto* lhs_arena = GetArenaForAllocation();
  auto* rhs_arena = other->GetArenaForAllocation();
  _internal_metadata_.InternalSwap(&other->_internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::InternalSwap(
      &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      &hash_str_, lhs_arena,
      &other->hash_str_, rhs_arena
  );
  swap(node_, other->node_);
}

::PROTOBUF_NAMESPACE_ID::Metadata GetFabRequest::GetMetadata() const {
  return ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(
      &descriptor_table_flwr_2fproto_2ffab_2eproto_getter, &descriptor_table_flwr_2fproto_2ffab_2eproto_once,
      file_level_metadata_flwr_2fproto_2ffab_2eproto[1]);
}

// ===================================================================

class GetFabResponse::_Internal {
 public:
  static const ::flwr::proto::Fab& fab(const GetFabResponse* msg);
};

const ::flwr::proto::Fab&
GetFabResponse::_Internal::fab(const GetFabResponse* msg) {
  return *msg->fab_;
}
GetFabResponse::GetFabResponse(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena, is_message_owned) {
  SharedCtor();
  if (!is_message_owned) {
    RegisterArenaDtor(arena);
  }
  // @@protoc_insertion_point(arena_constructor:flwr.proto.GetFabResponse)
}
GetFabResponse::GetFabResponse(const GetFabResponse& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  if (from._internal_has_fab()) {
    fab_ = new ::flwr::proto::Fab(*from.fab_);
  } else {
    fab_ = nullptr;
  }
  // @@protoc_insertion_point(copy_constructor:flwr.proto.GetFabResponse)
}

void GetFabResponse::SharedCtor() {
fab_ = nullptr;
}

GetFabResponse::~GetFabResponse() {
  // @@protoc_insertion_point(destructor:flwr.proto.GetFabResponse)
  if (GetArenaForAllocation() != nullptr) return;
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

inline void GetFabResponse::SharedDtor() {
  GOOGLE_DCHECK(GetArenaForAllocation() == nullptr);
  if (this != internal_default_instance()) delete fab_;
}

void GetFabResponse::ArenaDtor(void* object) {
  GetFabResponse* _this = reinterpret_cast< GetFabResponse* >(object);
  (void)_this;
}
void GetFabResponse::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void GetFabResponse::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}

void GetFabResponse::Clear() {
// @@protoc_insertion_point(message_clear_start:flwr.proto.GetFabResponse)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  if (GetArenaForAllocation() == nullptr && fab_ != nullptr) {
    delete fab_;
  }
  fab_ = nullptr;
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* GetFabResponse::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    switch (tag >> 3) {
      // .flwr.proto.Fab fab = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 10)) {
          ptr = ctx->ParseMessage(_internal_mutable_fab(), ptr);
          CHK_(ptr);
        } else
          goto handle_unusual;
        continue;
      default:
        goto handle_unusual;
    }  // switch
  handle_unusual:
    if ((tag == 0) || ((tag & 7) == 4)) {
      CHK_(ptr);
      ctx->SetLastTag(tag);
      goto message_done;
    }
    ptr = UnknownFieldParse(
        tag,
        _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
        ptr, ctx);
    CHK_(ptr != nullptr);
  }  // while
message_done:
  return ptr;
failure:
  ptr = nullptr;
  goto message_done;
#undef CHK_
}

::PROTOBUF_NAMESPACE_ID::uint8* GetFabResponse::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:flwr.proto.GetFabResponse)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .flwr.proto.Fab fab = 1;
  if (this->_internal_has_fab()) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::
      InternalWriteMessage(
        1, _Internal::fab(this), target, stream);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:flwr.proto.GetFabResponse)
  return target;
}

size_t GetFabResponse::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:flwr.proto.GetFabResponse)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // .flwr.proto.Fab fab = 1;
  if (this->_internal_has_fab()) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::MessageSize(
        *fab_);
  }

  return MaybeComputeUnknownFieldsSize(total_size, &_cached_size_);
}

const ::PROTOBUF_NAMESPACE_ID::Message::ClassData GetFabResponse::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::Message::CopyWithSizeCheck,
    GetFabResponse::MergeImpl
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetFabResponse::GetClassData() const { return &_class_data_; }

void GetFabResponse::MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to,
                      const ::PROTOBUF_NAMESPACE_ID::Message& from) {
  static_cast<GetFabResponse *>(to)->MergeFrom(
      static_cast<const GetFabResponse &>(from));
}


void GetFabResponse::MergeFrom(const GetFabResponse& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:flwr.proto.GetFabResponse)
  GOOGLE_DCHECK_NE(&from, this);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from._internal_has_fab()) {
    _internal_mutable_fab()->::flwr::proto::Fab::MergeFrom(from._internal_fab());
  }
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
}

void GetFabResponse::CopyFrom(const GetFabResponse& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:flwr.proto.GetFabResponse)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool GetFabResponse::IsInitialized() const {
  return true;
}

void GetFabResponse::InternalSwap(GetFabResponse* other) {
  using std::swap;
  _internal_metadata_.InternalSwap(&other->_internal_metadata_);
  swap(fab_, other->fab_);
}

::PROTOBUF_NAMESPACE_ID::Metadata GetFabResponse::GetMetadata() const {
  return ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(
      &descriptor_table_flwr_2fproto_2ffab_2eproto_getter, &descriptor_table_flwr_2fproto_2ffab_2eproto_once,
      file_level_metadata_flwr_2fproto_2ffab_2eproto[2]);
}

// @@protoc_insertion_point(namespace_scope)
}  // namespace proto
}  // namespace flwr
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::flwr::proto::Fab* Arena::CreateMaybeMessage< ::flwr::proto::Fab >(Arena* arena) {
  return Arena::CreateMessageInternal< ::flwr::proto::Fab >(arena);
}
template<> PROTOBUF_NOINLINE ::flwr::proto::GetFabRequest* Arena::CreateMaybeMessage< ::flwr::proto::GetFabRequest >(Arena* arena) {
  return Arena::CreateMessageInternal< ::flwr::proto::GetFabRequest >(arena);
}
template<> PROTOBUF_NOINLINE ::flwr::proto::GetFabResponse* Arena::CreateMaybeMessage< ::flwr::proto::GetFabResponse >(Arena* arena) {
  return Arena::CreateMessageInternal< ::flwr::proto::GetFabResponse >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>