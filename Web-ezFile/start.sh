#! /bin/bash
service cron restart && apache2 -D FOREGROUND
