"""
Copyright (c) 2016 Keitaro AB

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import uuid
import os


# turns on logger at Debug level
DEBUG = bool(os.environ.get('DATAPUSHER_DEBUG_MODE', 'False'))
# If False, configures the logger for production
# i.e. logs to STDERR and LOG_FILE (autorotates after 68mb, with 5 backups),
# and emails errors to admins.
# If True, only turns on Debug if DEBUG = True
TESTING = bool(os.environ.get('DATAPUSHER_TESTING', 'False'))
SECRET_KEY = str(uuid.uuid4())
USERNAME = str(uuid.uuid4())
PASSWORD = str(uuid.uuid4())

NAME = 'datapusher-plus'

# The connect string of the Datapusher+ Job database

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/job_store.db'

# webserver host and port
WRITE_ENGINE_URL = os.environ.get('DATAPUSHER_WRITE_ENGINE_URL', 'postgresql://datastorerw:pass@postgres/datastore_default')
HOST = '0.0.0.0'
PORT = 8000

# logging

#FROM_EMAIL = 'server-error@example.com'
#ADMINS = ['yourname@example.com']  # where to send emails

#LOG_FILE = '/tmp/ckan_service.log'
STDERR = True

# Content length settings
MAX_CONTENT_LENGTH = int(os.environ.get('DATAPUSHER_MAX_CONTENT_LENGTH', '1024000'))
CHUNK_SIZE = int(os.environ.get('DATAPUSHER_CHUNK_SIZE', '16384'))
CHUNK_INSERT_ROWS = int(os.environ.get('DATAPUSHER_CHUNK_INSERT_ROWS', '250'))
DOWNLOAD_TIMEOUT = int(os.environ.get('DATAPUSHER_DOWNLOAD_TIMEOUT', '30'))
# A Datapusher+ job is triggered automatically everytime a resource is modified (even just its metadata)
# if its mimetype is one of the supported datapusher.formats. 
# To ensure DP+ doesn't push an unchanged resource, it computes and stores the hash of the file
# If the hash has not changed (i.e. the file has not been modified), it refrains from "re-pushing" it
IGNORE_FILE_HASH = False

# Verify SSL
SSL_VERIFY = os.environ.get('DATAPUSHER_SSL_VERIFY', False)

# Rewrite resource URL's when ckan callback url base is used
REWRITE_RESOURCES = os.environ.get('DATAPUSHER_REWRITE_RESOURCES', False)
REWRITE_URL = os.environ.get('DATAPUSHER_REWRITE_URL', 'http://ckan:5000/')
# If this is not zero, the number of preview rows to push into the datastore
# If zero, it pushes the entire file
PREVIEW_ROWS = int(os.environ.get('DATAPUSHER_PREVIEW_ROWS', 0))
# If this is True, only the first n PREVIEW_ROWS are downloaded, and not the whole file
DOWNLOAD_PREVIEW_ONLY = bool(os.environ.get('DATAPUSHER_DOWNLOAD_PREVIEW_ONLY', False))
# number of days to keep job history
KEEP_JOBS_AGE = 60

# ============ QSV ANALYSIS SETTINGS ==========

# ---------- BINARY PATHS -------------
# qsv binary to use
# optionally, you can also use qsvdp_nightly.
# qsvdp is already very fast, but if you want even more speed
# qsvdp_nightly is compiled/linked in such a way that it's even faster/smaller
# see https://github.com/jqnatividad/qsv/blob/master/docs/PERFORMANCE.md#nightly-release-builds
QSV_BIN = '/usr/local/bin/qsvdp'

# file binary to use. `file` is used to get file metadata to display on the log
# if qsv cannot open a spreadsheet file (probably, because its password-protected or corrupt)
FILE_BIN = '/usr/bin/file'

# Dates are parsed with an MDY preference by default
# set PREFER_DMY = True if date-parsing should prefer DMY instead
PREFER_DMY = True

# The zero-based index of the default sheet to export to CSV. 0 is the first sheet.
# Accepts negative numbers. -1 is the last sheet, -2 the 2nd to last sheet, etc.
DEFAULT_EXCEL_SHEET = int(os.environ.get('DATAPUSHER_DEFAULT_EXCEL_SHEET', 0))

# Check if a file is sorted and has duplicates
SORT_AND_DUPE_CHECK = bool(os.environ.get('DATAPUSHER_SORT_AND_DUPE_CHECK', True))

# Should CSVs be deduped? Note that deduping also
# sorts the CSV.
DEDUP = bool(os.environ.get('DATAPUSHER_DEDUP', False))

# -------- SUMMARY STATS SETTINGS -----------
# Create a resource for calculated summary stats?
ADD_SUMMARY_STATS_RESOURCE = bool(os.environ.get('DATAPUSHER_ADD_SUMMARY_STATS_RESOURCE', False))

# Summary Stats don't make sense if PREVIEW_ROWS > 0
# because, you're only summarizing the preview, not the whole file
# Set to True if Summary Stats should also be done for previews
SUMMARY_STATS_WITH_PREVIEW = bool(os.environ.get('DATAPUSHER_SUMMARY_STATS_WITH_PREVIEW', False))

# additional command line options to pass to qsv stats when creating
# summary stats. Set to `--everything` if you want to include all the stats,
# particularly, when ADD_SUMMARY_STATS_RESOURCE is True
SUMMARY_STATS_OPTIONS = os.environ.get('DATAPUSHER_SUMMARY_STATS_OPTIONS', '')

# -------- AUTO INDEX SETTINGS ----------
# if AUTO_INDEX_THRESHOLD > 0 or AUTO_INDEX_DATES is true
# create indices automatically based on as column's cardinality (number of unique values)
#   - if a column's cardinality <= AUTO_INDEX_THRESHOLD, create an index for that column
#   - if AUTO_INDEX_THRESHOLD = -1, index all columns regardless of its cardinality
AUTO_INDEX_THRESHOLD = int(os.environ.get('DATAPUSHER_AUTO_INDEX_THRESHOLD', 3))

# for columns w/ cardinality equal to record_count, it's all unique values, create a unique index
AUTO_UNIQUE_INDEX = bool(os.environ.get('DATAPUSHER_AUTO_UNIQUE_INDEX', True))

# always index date fields?
AUTO_INDEX_DATES = bool(os.environ.get('DATAPUSHER_AUTO_INDEX_DATES', True))

# ------ AUTO ALIAS SETTINGS ----------
# Should an alias be automatically created?
# Aliases are easier to use than resource_ids, and can be used with the CKAN API where
# resource_ids are used. Aliases are also SQL views that are easier to use when querying
# the CKAN Datastore database.
# Aliases are created by concatenating "{resource_name}-{package_name}-{owner_org_name}"
# truncated at 55-characters.
AUTO_ALIAS = bool(os.environ.get('DATAPUSHER_AUTO_ALIAS', False))

# Should aliases should always be unique? In case of an alias name collision, a three-digit
# sequence number is appended.
AUTO_ALIAS_UNIQUE = bool(os.environ.get('DATAPUSHER_AUTO_ALIAS_UNIQUE', False))

# -------- PII SETTINGS -----------
PII_SCREENING = bool(os.environ.get('DATAPUSHER_PII_SCREENING', False))

# Stop scanning on first PII found
PII_QUICK_SCREEN = bool(os.environ.get('DATAPUSHER_PII_QUICK_SCREEN', False))

# Abort Datapusher+ job if PII is found
PII_FOUND_ABORT = bool(os.environ.get('DATAPUSHER_PII_FOUND_ABORT', True))

# Create a resource where PII candidates are stored?
PII_SHOW_CANDIDATES = bool(os.environ.get('DATAPUSHER_PII_SHOW_CANDIDATES', True))

# The resource ID/alias of a Text file that has the 
# regex patterns to use for PII scanning.
# If this is not specified, the default PII scanning rules in
# default_pii_regexes.txt are used
PII_REGEX_RESOURCE_ID_OR_ALIAS = os.environ.get('DATAPUSHER_PII_REGEX_RESOURCE_ID_OR_ALIAS', '')