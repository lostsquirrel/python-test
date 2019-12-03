#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
from pathlib import Path
from datetime import date, timedelta

expire_days = 31
expire_delta = timedelta(days=expire_days)
backup_path = "/data/backup/gitlab"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
backup_file_name_suffix = "gitlab_backup.tar"
max_split = 5


def is_backup_file(file_name: str) -> bool:
    return file_name.endswith(backup_file_name_suffix)


def get_backup_date(file_name):
    logger.debug("take apart {}".format(file_name))
    timestamp, year, month, day, version, remain = file_name.split("_", max_split)
    date_ = date(int(year), int(month), int(day))
    return int(timestamp), date_, version


def is_expired(backup_date):
    now = date.today()
    return now - backup_date > expire_delta


def is_expired_backup(file_name):
    timestamp, backup_date, backup_version = get_backup_date(file_name)
    return is_expired(backup_date)


def list_backups():
    return list(filter(is_backup_file, os.listdir(backup_path)))


def expired_backup(backups):
    logger.info("{} backups found".format(len(backups)))
    return list(filter(is_expired_backup, backups))


def delete_file(file_name):
    path = Path(file_name)
    if path.exists():
        logger.info("going to remove file {}".format(file_name))
        os.remove(str(file_name))


if __name__ == '__main__':
    backups = list_backups()
    expired_backups = expired_backup(backups)
    logger.info("{} expired backup files found".format(len(expired_backups)))
    for backup_file in expired_backups:
        delete_file(Path(backup_path) / backup_file)
