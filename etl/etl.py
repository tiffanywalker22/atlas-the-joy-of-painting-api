import csv
import json
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker

DB_USER = "new_user"
DB_PASS = "securepassword"
DB_HOST = "localhost"
DB_NAME = "joy_of_painting"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

episodes = Table(
    'episodes', metadata,
    Column('id', Integer, primary_key=True),
    Column('painting_index', String),
    Column('img_src', String),
    Column('painting_title', String),
    Column('season', String),
    Column('episode_number', Integer),
    Column('num_colors', Integer),
    Column('youtube_src', String),
    Column('broadcast_date', String),
    Column('special_guest', Boolean)
)

colors = Table(
    'colors', metadata,
    Column('id', Integer, primary_key=True),
    Column('episode_id', Integer),
    Column('color_name', String),
    Column('color_hex', String)
)

subjects = Table(
    'subjects', metadata,
    Column('id', Integer, primary_key=True),
    Column('episode_id', Integer),
    Column('apple_frame', Boolean),
    Column('aurora_borealis', Boolean),
    Column('barn', Boolean),
    Column('beach', Boolean),
    Column('boat', Boolean),
    Column('bridge', Boolean),
    Column('building', Boolean),
    Column('bushes', Boolean),
    Column('cabin', Boolean),
    Column('cactus', Boolean),
    Column('circle_frame', Boolean),
    Column('cirrus', Boolean),
    Column('cliff', Boolean),
    Column('clouds', Boolean),
    Column('conifer', Boolean),
    Column('cumulus', Boolean),
    Column('deciduous', Boolean),
    Column('diane_andre', Boolean),
    Column('dock', Boolean),
    Column('double_oval_frame', Boolean),
    Column('farm', Boolean),
    Column('fence', Boolean),
    Column('fire', Boolean),
    Column('florida_frame', Boolean),
    Column('flowers', Boolean),
    Column('fog', Boolean),
    Column('framed', Boolean),
    Column('grass', Boolean),
    Column('guest', Boolean),
    Column('half_circle_frame', Boolean),
    Column('half_oval_frame', Boolean),
    Column('hills', Boolean),
    Column('lake', Boolean),
    Column('lakes', Boolean),
    Column('lighthouse', Boolean),
    Column('mill', Boolean),
    Column('moon', Boolean),
    Column('mountain', Boolean),
    Column('mountains', Boolean),
    Column('night', Boolean),
    Column('ocean', Boolean),
    Column('oval_frame', Boolean),
    Column('palm_trees', Boolean),
    Column('path', Boolean),
    Column('person', Boolean),
    Column('portrait', Boolean),
    Column('rectangle_3d_frame', Boolean),
    Column('rectangular_frame', Boolean),
    Column('river', Boolean),
    Column('rocks', Boolean),
    Column('seashell_frame', Boolean),
    Column('snow', Boolean),
    Column('snowy_mountain', Boolean),
    Column('split_frame', Boolean),
    Column('steve_ross', Boolean),
    Column('structure', Boolean),
    Column('sun', Boolean),
    Column('tomb_frame', Boolean),
    Column('tree', Boolean),
    Column('trees', Boolean),
    Column('triple_frame', Boolean),
    Column('waterfall', Boolean),
    Column('waves', Boolean),
    Column('windmill', Boolean),
    Column('window_frame', Boolean),
    Column('winter', Boolean),
    Column('wood_framed', Boolean)
)
