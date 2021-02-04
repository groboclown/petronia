#!/bin/bash

set -e

h=$( dirname "$0" )
pd="${h}/../projects"

# Foreman events
echo foreman/petronia_foreman/events:
"${h}/generate-events.sh" \
  --output "${pd}/foreman/petronia_foreman/events" \
  --implementation --api \
  "${pd}/foreman/foreman-extension.yaml"


# Extension-loader events
echo extension-loader/petronia_extension_loader/events:
"${h}/generate-events.sh" \
  --output "${pd}/extension-loader/petronia_extension_loader/events/impl" \
  --implementation --api --state \
  "${pd}/foreman/foreman-extension.yaml" \
  "${pd}/extension-loader/extension-loader-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/extension-loader/petronia_extension_loader/events/ext" \
  --api \
  "${pd}/core-extensions/datastore-extension.yaml"


# Core extension implementations
echo core-extensions:
"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_extension/petronia/core/impl/datastore/events/impl" \
  --implementation --api --state \
  "${pd}/core-extensions/datastore-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_extension/petronia/core/impl/logging/events/impl" \
  --implementation --api --state \
  "${pd}/core-extensions/logging-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_extension/petronia/core/impl/timer/events/impl" \
  --implementation --api --state \
  "${pd}/core-extensions/timer-extension.yaml"


# Native
echo native-handler:
"${h}/generate-events.sh" \
  --output "${pd}/native-handler/petronia_native/common/events/impl" \
  --implementation --api --state \
  "${pd}/native-handler/native-extension.yaml"
