#!/bin/bash

RE_TEXT='^.*\(\(default\|README\)\|\(\.\(png\|bmp\|jpg\|php\|html\|conf\|Sample\|xls\|doc\|pdf\|css\)\)\)$'

find . -type f -regex $RE_TEXT -exec echo {} \; -exec chmod a-x {} \;
