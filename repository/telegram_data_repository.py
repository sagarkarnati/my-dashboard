from repository.db_utils import DBUtils
import streamlit as st


class TelegramDataRepository:

    def save_bulk(self, telegram_data):
        insert_query = """
            INSERT IGNORE INTO TELEGRAM_DATA (ENTITY_ID, CHANNEL_NAME, MESSAGE_ID, MESSAGE, MESSAGE_TIME) 
            VALUES(%s, %s, %s, %s, %s)
        """
        connection = DBUtils().get_connection()
        cursor = connection.cursor()
        for telegram_data_obj in telegram_data:
            val = (telegram_data_obj.entity_id, telegram_data_obj.channel_name,
                   telegram_data_obj.message_id, telegram_data_obj.message,
                   telegram_data_obj.message_time)
            cursor.execute(insert_query, val)

        connection.commit()

    def get_max_message_id_by_entity(self, entity_id):
        select_query = """
            SELECT MAX(MESSAGE_ID) FROM TELEGRAM_DATA WHERE ENTITY_ID = %s;
        """
        connection = DBUtils().get_connection()
        cursor = connection.cursor(dictionary=False)
        cursor.execute(select_query, (entity_id,))
        result = cursor.fetchone()[0]
        if result is None:
            return 0
        else:
            return result

    @st.cache(func=None, persist=True, allow_output_mutation=False, show_spinner=True, suppress_st_warning=False,
              hash_funcs=None, max_entries=None, ttl=1800)
    def get_telegram_data(self, channel_name, start_date):
        select_query = """
            SELECT * FROM TELEGRAM_DATA WHERE CHANNEL_NAME = %s ORDER BY MESSAGE_TIME DESC LIMIT 500;
        """
        connection = DBUtils().get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(select_query, (channel_name,))
        return cursor.fetchall()

    @st.cache(func=None, persist=True, allow_output_mutation=False, show_spinner=True, suppress_st_warning=False,
             hash_funcs=None, max_entries=None, ttl=2629746)
    def get_all_channels(self):
        select_query = """
            SELECT DISTINCT CHANNEL_NAME FROM TELEGRAM_DATA;
        """
        connection = DBUtils().get_connection()
        cursor = connection.cursor(dictionary=False)
        cursor.execute(select_query)
        result_arr = []
        for row in cursor.fetchall():
            result_arr.append(row[0])
        return result_arr