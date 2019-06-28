#!/bin/bash
#
# entry file

__DIR__=${PWD%%\/public}

. $__DIR__/.env
. $__DIR__/config/app.conf

. $__DIR__/lib/petunia/route/router

router::handle
