import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_user_table_query(self):
        if self.connection:
            print("Database connected successfully")
        self.connection.execute(sql_queries.create_user_table_query)
        self.connection.execute(sql_queries.create_quiz)
        self.connection.execute(sql_queries.create_user_ban)
        self.connection.execute(sql_queries.create_user_survey)
        self.connection.execute(sql_queries.create_complaint)
        self.connection.execute(sql_queries.create_wallet)
        self.connection.execute(sql_queries.create_referral)
        self.connection.execute(sql_queries.create_scraper_note)


    def sql_insert_user_table_query(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(sql_queries.insert_user_table_query, (telegram_id,
                                                                  username,
                                                                  first_name,
                                                                  last_name,))
        self.connection.commit()

    def sql_select_user_table_query(self):
        self.cursor.row_factory = lambda cursor, row: {"telegram_id": row[1],
                                                       "username": row[2],
                                                       "first_name": row[3],
                                                       "last_name": row[4]}
        return self.cursor.execute(sql_queries.select_user_table_query).fetchall()


    def sql_insert_quiz(self, telegram_id, quiz, quiz_option):
        self.cursor.execute(sql_queries.insert_quiz, (telegram_id,
                                                      quiz,
                                                      quiz_option,))
        self.connection.commit()



    def sql_insert_user_ban(self, telegram_id, group_id, reasons):
        self.cursor.execute(sql_queries.insert_user_ban, (telegram_id,
                                                          group_id,
                                                          reasons,))
        self.connection.commit()

    def sql_select_user_ban(self, telegram_id, group_id):
        self.cursor.row_factory = lambda cursor, row: {"telegram_id": row[0]}
        return self.cursor.execute(sql_queries.select_user_ban, (telegram_id,
                                                                 group_id)).fetchall()

    def sql_select_potential_user_ban(self):
        self.cursor.row_factory = lambda cursor, row: {"telegram_id": row[1],
                                                       "username": row[2],
                                                       "first_name": row[3],
                                                       "last_name": row[4],
                                                       "reasons": row[9]}
        return self.cursor.execute(sql_queries.select_potential_user_ban).fetchall()

    def sql_insert_user_survey(self, idea, problems, assessment, user_id):
        self.cursor.execute(sql_queries.insert_user_survey, (idea,
                                                             problems,
                                                             assessment,
                                                             user_id,))
        self.connection.commit()

    def sql_select_user_survey(self):
        self.cursor.row_factory = lambda cursor, row: {"id": row[0],
                                                       "idea": row[1],
                                                       "problems": row[2],
                                                       "assessment": row[3],
                                                       "user_id": row[4]}
        return self.cursor.execute(sql_queries.select_user_survey).fetchall()

    def sql_select_user_survey_by_id(self, id):
        self.cursor.row_factory = lambda cursor, row: {"id": row[0],
                                                       "telegram_id": row[1],
                                                       "username": row[2],
                                                       "first_name": row[3],
                                                       "last_name": row[4],
                                                       "idea": row[6],
                                                       "problems": row[7],
                                                       "assessment": row[8]}
        return self.cursor.execute(sql_queries.select_user_survey_by_id, (id,)).fetchall()

    def sql_insert_complaint(self, telegram_id, telegram_id_bad_user, reason, count):
        self.cursor.execute(sql_queries.insert_complaint, (telegram_id,
                                                           telegram_id_bad_user,
                                                           reason,
                                                           count,))
        self.connection.commit()

    def sql_select_id_by_username(self, username):
        self.cursor.row_factory = lambda cursor, row: {"username": row[0]}
        return self.cursor.execute(sql_queries.select_id_by_username, (username,)).fetchall()

    def sql_select_complaint(self, user_id):
        self.cursor.row_factory = lambda cursor, row: {"count": row[0]}
        return self.cursor.execute(sql_queries.select_complaint, (user_id,))

    def sql_select_complaint_check(self, user_id, bad_user_id):
        self.cursor.row_factory = lambda cursor, row: {"count": row[0]}
        return self.cursor.execute(sql_queries.select_complaint_check, (user_id, bad_user_id,))


    def sql_insert_wallet(self, telegram_id):
        self.cursor.execute(sql_queries.insert_wallet, (telegram_id,))
        self.connection.commit()

    def sql_select_wallet(self, id):
        return self.cursor.execute(sql_queries.select_wallet, (id,)).fetchall()[0][0]

    def sql_update_wallet(self, id, point):
        self.cursor.execute(sql_queries.update_wallet, (point, id,))
        self.connection.commit()


    def sql_insert_referral(self, owner_link_telegram_id, referral_telegram_id):
        self.cursor.execute(sql_queries.insert_referral, (owner_link_telegram_id, referral_telegram_id,))
        self.connection.commit()

    def sql_select_referral(self, referral_telegram_id):
        self.cursor.row_factory = lambda cursor, row: {"id": row[0],
                                                       "owner_link_telegram_id": row[1],
                                                       "referral_telegram_id": row[2], }
        return self.cursor.execute(sql_queries.select_referral, (referral_telegram_id,)).fetchall()

    def sql_select_all_referrals(self, owner_link_telegram_id):
        self.cursor.row_factory = lambda cursor, row: {"username": row[0],
                                                       "first_name": row[1],
                                                       "last_name": row[2]}
        return self.cursor.execute(sql_queries.select_all_referrals, (owner_link_telegram_id,)).fetchall()


    def sql_update_user_reference_link(self, link, telegram_id):
        self.cursor.execute(sql_queries.update_user_reference_link_query, (link, telegram_id,))
        self.connection.commit()

    def sql_select_user_return_link(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {"link": row[0]}
        return self.cursor.execute(
            sql_queries.select_user_by_id_return_link_query, (telegram_id,)
        ).fetchall()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {"link": row[0]}
        return self.cursor.execute(sql_queries.select_user_by_link, (link,)).fetchall()


    def sql_insert_scraper_note(self, user_id, link_anime):
        self.cursor.execute(sql_queries.insert_scraper_note, (user_id,
                                                              link_anime))
        self.connection.commit()

    def sql_select_scraper_note(self, id_user):
        self.cursor.row_factory = lambda cursor, row: {"user": row[0],
                                                       "link": row[1]}
        return self.cursor.execute(sql_queries.select_scraper_note, (id_user,)).fetchall()
