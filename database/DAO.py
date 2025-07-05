from database.DB_connect import DBConnect
from model.artObject import ArtObject


class DAO():

    @staticmethod
    def getAllNodes():
        cnx = DBConnect.get_connection()
        if cnx is None:
            return f"Error connecting to the database"
        else:
            result = []
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM objects"""

            cursor.execute(query)

            for row in cursor:
                result.append(ArtObject(**row))

        cursor.close()
        cnx.close()
        return result


    @staticmethod
    def getAllEdges():
        cnx = DBConnect.get_connection()
        if cnx is None:
            return f"Error connecting to the database"
        else:
            result = []
            cursor = cnx.cursor(dictionary=True)
            query = """select e1.object_id as o1, e2.object_id as o2, count(*) as peso
                        from exhibition_objects e1, exhibition_objects e2
                        where e1.exhibition_id = e2.exhibition_id 
                        and e1.object_id <e2.object_id
                        group by e1.object_id, e2.object_id
                        order by peso desc"""

            cursor.execute(query)

            for row in cursor:
                result.append((row['o1'], row['o2'], row['peso']))

        cursor.close()
        cnx.close()
        return result

