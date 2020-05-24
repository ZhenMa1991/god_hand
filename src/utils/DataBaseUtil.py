import sqlite3


class DataBaseUtil(object):

    connect = None

    @staticmethod
    def get_connect():
        if not DataBaseUtil.connect:
            DataBaseUtil.connect = sqlite3.connect('C:\\Users\\13376\\PycharmProjects\\god_hand\\src\\db\\god_hand.db')
        return DataBaseUtil.connect

    @staticmethod
    def query_by_sql(sql):
        c = DataBaseUtil.get_connect().cursor()
        return c.execute(sql)
