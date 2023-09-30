import leancloud
import os

leancloud.init(os.environ.get('LEANCLOUD_APP_ID', '404'), os.environ.get('LEANCLOUD_APP_KEY', '404'))

def query_to_keep_unarchive():
    Announcement: leancloud.Object = leancloud.Object.extend('announcement')
    query = Announcement.query
    query.limit(1)  # 限制只获取一条数据
    query.descending('createdAt')  # 按照 createdAt 降序排列，即获取最新的一条数据
    query.not_equal_to('en', '')