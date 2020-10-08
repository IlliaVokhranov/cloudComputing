from app import conn


class TodoItem(conn.Model):
    id = conn.Column(conn.Integer, primary_key=True)
    text = conn.Column(conn.String(200))
    complete = conn.Column(conn.Boolean)

    def __repr__(self):
        return self.text