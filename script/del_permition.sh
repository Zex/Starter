#!/bin/bash

RE_TEXT='^.*\(\(default\|README\)\|\(\.\(png\|bmp\|jpg\|php\|html\|conf\|Sample\|xls\|doc\|pdf\|css\|sql\)\)\)$'

find . -type f -regex $RE_TEXT -exec echo {} \; -exec chmod a-x {} \;

chown www-data.www-data dbs/ -R
