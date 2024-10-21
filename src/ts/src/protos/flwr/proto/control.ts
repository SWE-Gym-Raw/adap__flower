// @generated by protobuf-ts 2.9.4
// @generated from protobuf file "flwr/proto/control.proto" (package "flwr.proto", syntax proto3)
// tslint:disable
//
// Copyright 2024 Flower Labs GmbH. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// ==============================================================================
//
import { UpdateRunStatusResponse } from "./run";
import { UpdateRunStatusRequest } from "./run";
import { GetRunStatusResponse } from "./run";
import { GetRunStatusRequest } from "./run";
import { CreateRunResponse } from "./run";
import { CreateRunRequest } from "./run";
import { ServiceType } from "@protobuf-ts/runtime-rpc";
/**
 * @generated ServiceType for protobuf service flwr.proto.Control
 */
export const Control = new ServiceType("flwr.proto.Control", [
    { name: "CreateRun", options: {}, I: CreateRunRequest, O: CreateRunResponse },
    { name: "GetRunStatus", options: {}, I: GetRunStatusRequest, O: GetRunStatusResponse },
    { name: "UpdateRunStatus", options: {}, I: UpdateRunStatusRequest, O: UpdateRunStatusResponse }
]);