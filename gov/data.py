def load():
    import pymysql
    from datetime import datetime
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "GOVDATA", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 如果数据表已经存在使用 execute() 方法删除表。
    cursor.execute("DROP TABLE IF EXISTS EVENT")

    # 创建数据表SQL语句
    sql = """CREATE TABLE event (
                REC_ID INT NOT NULL ,
                REPORT_NUM  int , 
                CREATE_TIME DATETIME ,  
                DISTRICT_NAME VARCHAR (30),
                DISTRICT_ID INT, 
                STREET_NAME VARCHAR (30) ,
                STREET_ID INT ,
                COMMUNITY_NAME VARCHAR (30),
                COMMUNITY_ID INT ,
                EVENT_TYPE_NAME VARCHAR (30),
                EVENT_TYPE_ID  INT,
                MAIN_TYPE_NAME VARCHAR (30),
                MAIN_TYPE_ID  INT ,
                SUB_TYPE_NAME VARCHAR (30),
                SUB_TYPE_ID INT ,
                DISPOSE_UNIT_NAME VARCHAR (30),
                DISPOSE_UNIT_ID INT ,
                EVENT_SRC_NAME VARCHAR (30),
                EVENT_SRC_ID  INT ,
                OPERATE_NUM INT ,
                OVERTIME_ARCHIVE_NUM INT ,
                INTIME_TO_ARCHIVE_NUM INT ,
                INTIME_ARCHIVE_NUM INT,
                EVENT_PROPERTY_ID INT ,
                EVENT_PROPERTY_NAME VARCHAR (30),
                PRIMARY KEY(REC_ID)
                  )"""

    cursor.execute(sql)
    import xml.dom.minidom
    dom = xml.dom.minidom.parse('坪山区-民生诉求数据_完整版.xml')
    root = dom.documentElement
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a[0] = root.getElementsByTagName('REC_ID')
    a[1] = root.getElementsByTagName('REPORT_NUM')
    a[2] = root.getElementsByTagName('CREATE_TIME')
    a[3] = root.getElementsByTagName('DISTRICT_NAME')
    a[4] = root.getElementsByTagName('DISTRICT_ID')
    a[5] = root.getElementsByTagName('STREET_NAME')
    a[6] = root.getElementsByTagName('STREET_ID')
    a[7] = root.getElementsByTagName('COMMUNITY_NAME')
    a[8] = root.getElementsByTagName('COMMUNITY_ID')
    a[9] = root.getElementsByTagName('EVENT_TYPE_NAME')
    a[10] = root.getElementsByTagName('EVENT_TYPE_ID')
    a[11] = root.getElementsByTagName('MAIN_TYPE_NAME')
    a[12] = root.getElementsByTagName('MAIN_TYPE_ID')
    a[13] = root.getElementsByTagName('SUB_TYPE_NAME')
    a[14] = root.getElementsByTagName('SUB_TYPE_ID')
    a[15] = root.getElementsByTagName('DISPOSE_UNIT_NAME')
    a[16] = root.getElementsByTagName('DISPOSE_UNIT_ID')
    a[17] = root.getElementsByTagName('EVENT_SRC_NAME')
    a[18] = root.getElementsByTagName('EVENT_SRC_ID')
    a[19] = root.getElementsByTagName('OPERATE_NUM')
    a[20] = root.getElementsByTagName('OVERTIME_ARCHIVE_NUM')
    a[21] = root.getElementsByTagName('INTIME_TO_ARCHIVE_NUM')
    a[22] = root.getElementsByTagName('INTIME_ARCHIVE_NUM')
    a[23] = root.getElementsByTagName('EVENT_PROPERTY_ID')
    a[24] = root.getElementsByTagName('EVENT_PROPERTY_NAME')
    b = "'"
    for i in range(len(a[0])):
        if a[0][i].firstChild.data == '-':
            a[0][i] = 'null'
        else:
            a[0][i] = int(a[0][i].firstChild.data)
        if a[1][i].firstChild.data == '-':
            a[1][i] = 'null'
        else:
            a[1][i] = int(a[1][i].firstChild.data)
        if a[2][i].firstChild.data == '-':
            a[2][i] = 'null'
        else:
            a[2][i] = datetime.strptime(a[2][i].firstChild.data, '%Y-%m-%d %H:%M:%S')
        if a[3][i].firstChild.data == '-':
            a[3][i] = 'null'
        else:
            a[3][i] = b + a[3][i].firstChild.data + b
        if a[4][i].firstChild.data == '-':
            a[4][i] = 'null'
        else:
            a[4][i] = int(a[4][i].firstChild.data)
        if a[5][i].firstChild.data == '-':
            a[5][i] = 'null'
        else:
            a[5][i] = b + a[5][i].firstChild.data + b
        if a[6][i].firstChild.data == '-':
            a[6][i] = 'null'
        else:
            a[6][i] = int(a[6][i].firstChild.data)
        if a[7][i].firstChild.data == '-':
            a[7][i] = 'null'
        else:
            a[7][i] = b + a[7][i].firstChild.data + b
        if a[8][i].firstChild.data == '-':
            a[8][i] = 'null'
        else:
            a[8][i] = int(a[8][i].firstChild.data)
        if a[9][i].firstChild.data == '-':
            a[9][i] = 'null'
        else:
            a[9][i] = b + a[9][i].firstChild.data + b
        if a[10][i].firstChild.data == '-':
            a[10][i] = 'null'
        else:
            a[10][i] = int(a[10][i].firstChild.data)
        if a[11][i].firstChild.data == '-':
            a[11][i] = 'null'
        else:
            a[11][i] = b + a[11][i].firstChild.data + b
        if a[12][i].firstChild.data == '-':
            a[12][i] = 'null'
        else:
            a[12][i] = int(a[12][i].firstChild.data)
        if a[13][i].firstChild.data == '-':
            a[13][i] = 'null'
        else:
            a[13][i] = b + a[13][i].firstChild.data + b
        if a[14][i].firstChild.data == '-':
            a[14][i] = 'null'
        else:
            a[14][i] = int(a[14][i].firstChild.data)
        if a[15][i].firstChild.data == '-':
            a[15][i] = 'null'
        else:
            a[15][i] = b + a[15][i].firstChild.data + b
        if a[16][i].firstChild.data == '-':
            a[16][i] = 'null'
        else:
            a[16][i] = int(a[16][i].firstChild.data)
        if a[17][i].firstChild.data == '-':
            a[17][i] = 'null'
        else:
            a[17][i] = b + a[17][i].firstChild.data + b
        if a[18][i].firstChild.data == '-':
            a[18][i] = 'null'
        else:
            a[18][i] = int(a[18][i].firstChild.data)
        if a[19][i].firstChild.data == '-':
            a[19][i] = 'null'
        else:
            a[19][i] = int(a[19][i].firstChild.data)
        if a[20][i].firstChild.data == '-':
            a[20][i] = 'null'
        else:
            a[20][i] = int(a[20][i].firstChild.data)
        if a[21][i].firstChild.data == '-':
            a[21][i] = 'null'
        else:
            a[21][i] = int(a[21][i].firstChild.data)
        if a[22][i].firstChild.data == '-':
            a[22][i] = 'null'
        else:
            a[22][i] = int(a[22][i].firstChild.data)
        if a[23][i].firstChild.data == '-':
            a[23][i] = 'null'
        else:
            a[23][i] = int(a[23][i].firstChild.data)
        if a[24][i].firstChild.data == '-':
            a[24][i] = 'null'
        else:
            a[24][i] = b + a[24][i].firstChild.data + b

    # 使用cursor()方法获取操作游标
    for i in range(len(a[0])):
        cursor = db.cursor()
        # SQL 插入语句
        sql = "INSERT INTO event(REC_ID ,\
                REPORT_NUM ,\
                CREATE_TIME ,\
                DISTRICT_NAME ,\
                DISTRICT_ID ,\
                STREET_NAME, \
                STREET_ID, \
                COMMUNITY_NAME, \
                COMMUNITY_ID, \
                EVENT_TYPE_NAME, \
                EVENT_TYPE_ID, \
                MAIN_TYPE_NAME, \
                MAIN_TYPE_ID,\
                SUB_TYPE_NAME,\
                SUB_TYPE_ID, \
                DISPOSE_UNIT_NAME, \
                DISPOSE_UNIT_ID, \
                EVENT_SRC_NAME, \
                EVENT_SRC_ID, \
                OPERATE_NUM, \
                OVERTIME_ARCHIVE_NUM,\
                INTIME_TO_ARCHIVE_NUM, \
                INTIME_ARCHIVE_NUM, \
                EVENT_PROPERTY_ID, \
                EVENT_PROPERTY_NAME\
                ) VALUES (%s,%s,str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % \
              (a[0][i], a[1][i], a[2][i], a[3][i], a[4][i], a[5][i], a[6][i], a[7][i], a[8][i], a[9][i], a[10][i],
               a[11][i], a[12][i], a[13][i], a[14][i], a[15][i], a[16][i], a[17][i], a[18][i], a[19][i], a[20][i],
               a[21][i], a[22][i], a[23][i], a[24][i])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

    # 关闭数据库连接
    db.close()
    return 0
def search(time1,time2):
    # !/usr/bin/python3
    import pymysql
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "GOVDATA", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "SELECT * FROM event \
               WHERE  CREATE_TIME BETWEEN str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s') AND str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s')" % (time1, time2)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    return results
def error():
    import pymysql
    db = pymysql.connect("localhost", "root", "root", "GOVDATA", charset='utf8')
    cursor = db.cursor()
    sql = "SELECT * FROM event \
                   WHERE rec_id < 100000 and CREATE_TIME BETWEEN str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s') AND str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s')" % (0,0)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    return results