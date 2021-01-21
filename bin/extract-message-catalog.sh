#!/bin/sh

set -e

HERE=$( dirname "$0" )
output_dir="${HERE}/../projects/l10n"
template_dir="${output_dir}/templates"
test -d "${template_dir}" && rm -r "${template_dir}"
mkdir -p "${template_dir}"
translation_dir="${output_dir}/translations"
mkdir -p "${translation_dir}"

for n in "${HERE}"/../projects/* ; do
  if [ -f "${n}/mypy.ini" ] ; then
    project_name=$( basename "${n}" )
    python3 -m babel.messages.frontend extract \
      -o "${template_dir}/${project_name}.pot" \
      --sort-by-file \
      --copyright-holder="Petronia" \
      --project="Petronia ${project_name}" \
      -c "I18N" \
      "${n}"
    if [ -f "${template_dir}/${project_name}.pot" ] ; then
      # Messages are, by default, in US English.
      python3 -m babel.messages.frontend init \
        --input-file="${template_dir}/${project_name}.pot" \
        --output-dir="${translation_dir}" \
        --domain="${project_name}" \
        --locale=en \
        "${n}"
      python3 -m babel.messages.frontend init \
        --input-file="${template_dir}/${project_name}.pot" \
        --output-dir="${translation_dir}" \
        --domain="${project_name}" \
        --locale=en_US \
        "${n}"
      # Now update existing translations...
      for locale_dir in "${translation_dir}"/* ; do
        locale_name=$( basename "${locale_dir}" )
        tn_po="${locale_dir}/LC_MESSAGES/${project_name}.po"
        if [ -f "${tn_po}" ] && [ "${locale_name}" != "en" ] && [ "${locale_name}" != "en_US" ] ; then
          python3 -m babel.messages.frontend update \
            --input-file="${template_dir}/${project_name}.pot" \
            --domain="${project_name}" \
            --output-dir="${output_dir}" \
            --locale=${locale_name} \
            "${n}"
        fi
      done
    fi
  fi
done
