import sqlite3
import CCrypto


def is_new_user(user_id):
    conn = sqlite3.connect('server')
    cursor = conn.cursor()

    data = cursor.execute("SELECT * FROM data")
    records = cursor.fetchall()

    innit = True

    for row in records:
        if row[0] == user_id:
            innit = False
    conn.close()
    return innit


def is_new_user_and_reg(user_id):
    conn = sqlite3.connect('server')
    cursor = conn.cursor()

    data = cursor.execute("SELECT * FROM data")
    records = cursor.fetchall()

    innit = True

    for row in records:
        if row[0] == user_id:
            innit = False
    if innit:
        data = cursor.execute(f"INSERT INTO data VALUES ({user_id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
        conn.commit()
    conn.close()


def reg_new_user(user_id):
    conn = sqlite3.connect('server')
    cursor = conn.cursor()
    data = cursor.execute(f"INSERT INTO data VALUES ({user_id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
    conn.commit()
    conn.close()


def print_somethn_in_data(var_name):
    conn = sqlite3.connect('server')
    cursor = conn.cursor()

    data = cursor.execute("SELECT " + var_name + " FROM data")
    records = cursor.fetchall()

    print("\nAll Data=====")
    for row in records:
        print(f"\t{var_name} =", row[0], )
        print('\t-----------------------------------\n')
    print("All Data______\n")
    conn.close()


def print_all_data():
    conn = sqlite3.connect('server')
    cursor = conn.cursor()

    data = cursor.execute("SELECT * FROM data")
    records = cursor.fetchall()

    print("\nAll Data=====")
    for row in records:
        print("\tId =", row[0], )
        print("\tPrice  =", row[1])
        print("\tPrice  =", row[2])
        print("\tPrice  =", row[3])
        print("\tPrice  =", row[4])
        print("\tPrice  =", row[5])
        print("\tPrice  =", row[6])
        print("\tPrice  =", row[7])
        print("\tPrice  =", row[8])
        print("\tPrice  =", row[9])
        print('\t-----------------------------------\n\n')
    print("All Data______\n")
    conn.close()


def get_all_user_data(user_id):
    conn = sqlite3.connect('server')
    cursor = conn.cursor()

    data = cursor.execute(f"SELECT * FROM data WHERE id={user_id}")
    records = cursor.fetchall()
    conn.close()

    return records


def add_trigger(message, cur_name, user_id):
    trigger_price = message.text
    cc = CCrypto
    price = cc.get_crypto_price(crypto_name=cur_name)

    if float(trigger_price) < price:
        trigger_price = float(trigger_price) * (-1)

    conn = sqlite3.connect('server')
    cursor = conn.cursor()

    request = f"UPDATE data SET {cur_name}='{trigger_price}' WHERE id='{user_id}';"
    cursor.execute(request)
    conn.commit()

    conn.close()


def get_records():
    conn = sqlite3.connect('server')
    cursor = conn.cursor()

    data = cursor.execute("SELECT * FROM data")
    records = cursor.fetchall()
    conn.close()

    return records


def reset_all(user_id):
    crypto_acts = ["BTC", "LTC", "ETH", "SOL", "TRX", "XRP", "DOT", "ATOM", "WAVES"]
    conn = sqlite3.connect('server')
    cursor = conn.cursor()
    for i in crypto_acts:
        data = cursor.execute(f"UPDATE data SET {i}='0' WHERE id='{user_id}';")

    conn.commit()
    conn.close()


def reset_curr(user_id, cur_name):
    conn = sqlite3.connect('server')
    cursor = conn.cursor()
    data = cursor.execute(f"UPDATE data SET {cur_name}='0' WHERE id='{user_id}';")
    conn.commit()
    conn.close()