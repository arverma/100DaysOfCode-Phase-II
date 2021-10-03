# user_id, channel_id, timestamp(ms)
# 1, 1, 6000
# 1, 1, 6500
# 2, 1, 6500
# 1, 1, 7000
# 2, 1, 7000
# 1, 2, 8000
# 2, 1, 7500
# 2, 1, 8000
# 1, 2, 8500
# 1, 1, 9000
def update_config_file(prev_offset, PREV_TIMESTAMP):
    pass


def read_config_file(file_path):
    return 0, 0


class Database:
    def read(self, pre_offset, range, PREV_TIMESTAMP, retry=3, WINDOW=1):
        conn = None  #JDBC Connection
        res = None
        try:
            res = self.data = conn.read("SELECT * FROM TABLE_NAME LIMIT 1000000 OFFSET {} WHERE TIMESTAMP IN BETWEEN "
                                        "(PREV_TIMESTAMP, PREV_TIMESTAMP+WINDOW) ORDER BY TIMESTAMP".format(
                pre_offset))
            pre_offset = pre_offset + range
            PREV_TIMESTAMP = PREV_TIMESTAMP+WINDOW
            return res, pre_offset, PREV_TIMESTAMP
        except:
            return self.read(pre_offset, range, retry-1)


class ETL:
    def __init__(self):
        self.prev_offset, self.PREV_TIMESTAMP = read_config_file("path_to_config_file")
        self.df = []

    def extract(self):
        db = Database()
        self.df, self.prev_offset, self.PREV_TIMESTAMP = db.read(self.prev_offset, self.prev_offset, 1, self.PREV_TIMESTAMP) # 1= 1 million
        update_config_file(self.prev_offset, self.PREV_TIMESTAMP)


    def transformation(self):
        return self.df

    def load(self):
        self.df.write("output_path")




# postgress(spread over shards(index)) -> s3
# server(1 GB = 1 million rows)
# preserve the order in s3

# news_rows -> postgress

# every_hr = 10 million

# server(1 GB = 1 million rows)

# Postgress -> Glue(connection) -> Glue(SPARK) -> S3







