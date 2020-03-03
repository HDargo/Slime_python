import cx_Oracle
import os

weapon = []
os.putenv(
    "NLS_LANG", "KOREAN"
)

connection = cx_Oracle.connect("hr2", "1234", "localhost/XE")
cursor = connection.cursor()


class DB:
    def __init__(self):
        self.list = None
        self.list2 = []

    def WeaponDB(self):
        cursor.execute("""
        
            select  *
            from  weapon_shop
           
        """)
        for name in cursor:
            self.list = name[1], name[2], name[3]
            self.list = list(self.list)
            self.list.insert(0, 0)
            self.list2 += [self.list]
        return self.list2

    def armorDB(self):
        cursor.execute("""

            select  *
            from  armor_shop

        """)
        for name in cursor:
            self.list = name[1], name[2], name[3]
            self.list = list(self.list)
            self.list.insert(0,1)
            self.list2 += [self.list]
        return self.list2

    def ItemDB(self):
        cursor.execute("""

            select  *
            from  item_shop

        """)
        for name in cursor:
            self.list = name[1], name[2], name[3], name[4]
            self.list = list(self.list)
            self.list.insert(0,2)
            self.list2 += [self.list]
        return self.list2

    def findWeaponDb(self, name):
        cursor.execute("""

                    select  *
                    from  weapon_shop
                    where item_name = number
                """, number=name)


db = DB()
