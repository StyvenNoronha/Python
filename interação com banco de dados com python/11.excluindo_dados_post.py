from conexao_post import conn

cursor_obj = conn.cursor()

sql = """ DELETE FROM game
            WHERE id = %s"""
                
cursor_obj.execute(sql, (2,))

conn.commit()

conn.close()