# -*- coding:utf-8 -*-

class SeemRouter(object):
    """
    A router to control all database operations on models in the
    seem application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read seem models go to seem_db.
        """
        if model._meta.app_label == 'seems':
            return 'seem'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write seem models go to seem_db.
        """
        if model._meta.app_label == 'seems':
            return 'seem'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the seem app is involved.
        """
        if obj1._meta.app_label == 'seems' or \
           obj2._meta.app_label == 'seems':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the seem app only appears in the 'seem'
        database.
        """
        if app_label == 'seems':
            return db == 'seem'
        return None
