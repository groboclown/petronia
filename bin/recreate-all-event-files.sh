#!/bin/bash

h=$( dirname "$0" )
pd="${h}/../projects"

# Foreman events
echo foreman/petronia_foreman/events:
"${h}/generate-events.sh" \
  --output "${pd}/foreman/petronia_foreman/events" \
  --implementation \
  "${pd}/foreman/foreman.yaml"

echo foreman/petronia_foreman/launcher/util/cmd_events:
"${h}/generate-events.sh" \
  --output "${pd}/foreman/petronia_foreman/launcher/util/cmd_events" \
  --implementation \
  "${pd}/foreman/cmd-extension-events.yaml"


# Extension-loader events
echo extension-loader/petronia_extension_loader/events:
"${h}/generate-events.sh" \
  --output "${pd}/extension-loader/petronia_extension_loader/events" \
  --implementation \
  "${pd}/foreman/foreman.yaml" \
  "${pd}/extension-loader/extension-loader.yaml"

