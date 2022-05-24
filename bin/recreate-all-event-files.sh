#!/bin/bash

set -e

h=$( dirname "$0" )
pd="${h}/../projects"


# Foreman events
echo foreman:
"${h}/generate-events.sh" \
  --output "${pd}/foreman/petronia_foreman/events" \
  --implementation --api \
  "${pd}/foreman/foreman-extension.yaml" \
  "${pd}/foreman/foreman-announcement-extension.yaml"


# Extension-loader events
echo extension-loader:
"${h}/generate-events.sh" \
  --output "${pd}/extension-loader/petronia_extension_loader/events/impl" \
  --implementation --api --state \
  "${pd}/foreman/foreman-extension.yaml" \
  "${pd}/extension-loader/extension-loader-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/extension-loader/petronia_extension_loader/events/ext" \
  --api \
  "${pd}/core-extensions/datastore-extension.yaml" \
  "${pd}/foreman/foreman-announcement-extension.yaml"


# Core extension implementations
echo core-extensions:
"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/datastore/events/impl" \
  --implementation --api --state \
  "${pd}/core-extensions/datastore-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/datastore/state" \
  --state \
  "${pd}/core-extensions/core-datastore-extension.yaml"

"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/binarystore/events/impl" \
  --implementation --api --state \
  "${pd}/core-extensions/binarystore-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/binarystore/state" \
  --state \
  "${pd}/core-extensions/core-binarystore-extension.yaml"

"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/file_logger/state" \
  --state \
  "${pd}/core-extensions/core-file-logger-extension.yaml"

"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/timer/events/impl" \
  --implementation --api --state \
  "${pd}/core-extensions/timer-extension.yaml"

"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/timer/state" \
  --state \
  "${pd}/core-extensions/core-timer-extension.yaml"

"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/hotkey_binding/events/impl" \
  --implementation --api --state \
  "${pd}/core-extensions/hotkey-binding-extension.yaml"

"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/hotkey_binding/events/ext" \
  --api --state \
  "${pd}/native-handler/native-hotkey-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/core-extensions/petronia_core/hotkey_binding/state" \
  --state \
  "${pd}/core-extensions/core-hotkey-binding-extension.yaml"


# Native
echo native-handler:
"${h}/generate-events.sh" \
  --output "${pd}/native-handler/petronia_native/common/events/impl" \
  --implementation --api --state \
  "${pd}/native-handler/native-hotkey-extension.yaml" \
  "${pd}/native-handler/native-l10n-extension.yaml" \
  "${pd}/native-handler/native-monitor-extension.yaml" \
  "${pd}/native-handler/native-screen-extension.yaml" \
  "${pd}/native-handler/native-ui-extension.yaml" \
  "${pd}/native-handler/native-window-extension.yaml" \
  "${pd}/native-handler/native-notification-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/native-handler/petronia_native_windows/datastore" \
  --state \
  "${pd}/native-handler/windows-native-impl-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/native-handler/petronia_native_x11/datastore" \
  --state \
  "${pd}/native-handler/x11-native-impl-extension.yaml"


# Extension lib.
echo py-extension-lib:
"${h}/generate-events.sh" \
  --output "${pd}/py-extension-lib/petronia_ext_lib/events" \
  --api \
  "${pd}/core-extensions/datastore-extension.yaml" \
  "${pd}/core-extensions/logging-extension.yaml" \
  "${pd}/core-extensions/timer-extension.yaml" \
  "${pd}/extension-loader/extension-loader-extension.yaml" \
  "${pd}/foreman/foreman-announcement-extension.yaml"


# Portal events
echo portal:
"${h}/generate-events.sh" \
  --output "${pd}/portal/petronia_portal/events" \
  --implementation --api --state \
  "${pd}/portal/portal-extension.yaml" \
  "${pd}/ui-extensions/positioner-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/portal/petronia_portal/events" \
  --api --state \
  "${pd}/native-handler/native-window-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/portal/petronia_portal/state" \
  --state \
  "${pd}/native-handler/native-screen-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/portal/petronia_portal/events" \
  --api --state \
  "${pd}/core-extensions/hotkey-binding-extension.yaml"
"${h}/generate-events.sh" \
  --output "${pd}/portal/petronia_portal/state" \
  --state \
  "${pd}/portal/portal-impl-extension.yaml"
