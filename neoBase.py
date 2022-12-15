from neo4j import GraphDatabase


class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        if self.driver is not None:
            self.driver.close()


    def query(self, query, db=None):
        assert self.driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.driver.session(database=db) if db is not None else self.driver.session()
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response

    def get_objs(self):
        q = conn.query(f"MATCH (n:object) RETURN n")
        res = sorted(list(set([dict(i[0])["name"] for i in list(q)])), key=len)
        return res


conn = Neo4jConnection(uri="bolt://localhost:7687", user="Nikita", password="1234")

obj_lst = sorted(list(set([dict(i[0])["name"] for i in list(conn.query(f"MATCH (n:OBJECT) RETURN n"))])), key=len)
genre_lst = sorted(list(set([dict(i[0])["name"] for i in list(conn.query(f"MATCH (n:GENRE) RETURN n"))])), key=len)


def clean_likes():
    conn.query(f"""MATCH (like:LIKE)
DETACH DELETE like""")


def like_object(name):
    ex = conn.query(f"""MATCH (object:OBJECT) -[save:SAVE]-> (like:LIKE)
WHERE object.name = '{name}' AND like.name = '{name}'
    RETURN like""")
    if len(ex) == 0:
        conn.query(f"""MATCH (object:OBJECT)
WHERE object.name = '{name}'
CREATE (like:LIKE)
SET like.name = '{name}'
CREATE (object)  -[save:SAVE]-> (like)""")

def unlike_object(name):
    ex = conn.query(f"""MATCH (object:OBJECT) -[save:SAVE]-> (like:LIKE)
    WHERE object.name = '{name}' AND like.name = '{name}'
    DETACH DELETE like""")

