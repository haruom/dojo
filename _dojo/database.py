import sqlite3

class Database(object):

  def __init__(self, file):
    '''
    '''
    self.__connection = sqlite3.connect(file)
    self.__cursor = self.__connection.cursor()

  def get_segment_info(self):
    '''
    '''
    self.__cursor.execute('SELECT * FROM segmentInfo')

    result = self.__cursor.fetchall()

    output = [None] * (len(result) + 1)

    for r in result:
      output[r[0]] = r[1:]

    return output

  def get_largest_id(self):
    '''
    '''
    self.__cursor.execute('SELECT * FROM segmentInfo ORDER BY id DESC')

    result = self.__cursor.fetchone()

    # output = [None] * (len(result) + 1)

    # for r in result:
    #   output[r[0]] = r[1:]

    return result[0] 

  def get_id_tile_index(self,tile_id):
    '''
    '''
    self.__cursor.execute('SELECT * FROM idTileIndex WHERE id='+tile_id)

    result = self.__cursor.fetchall()

    output = []

    for r in result:
      output.append(r[1:])

    # w, z, y, x
    return output

  def get_merge_table(self):
    '''
    '''
    self.__cursor.execute('SELECT * FROM relabelMap')

    result = self.__cursor.fetchall()

    output = {}

    for r in result:
      output[r[0]] = r[1:]

    return output

  def insert_merge(self, id1, id2):
    '''
    '''
    try:
      with self.__connection:
        self.__connection.execute('INSERT INTO relabelMap VALUES (?,?)', id1, id2);
    except:
      print 'ERROR WHEN MERGING', id1, id2
      

