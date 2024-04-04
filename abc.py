import sqlite3


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


c.execute("DELETE FROM tbl_pedido WHERE id = ?", (30,))  # Reemplaza 1 con el valor del id que quieres eliminar


conn.commit()


conn.close()