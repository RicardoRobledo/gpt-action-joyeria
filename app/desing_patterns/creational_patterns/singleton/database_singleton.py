from sqlalchemy import func
from sqlalchemy.sql import exists
from sqlalchemy.orm import joinedload
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.api.users.models.user import UserModel, UserActionModel
from app.api.training.models.training import TopicModel, TrainingDocumentModel
from app import config


__author__ = 'Ricardo'
__version__ = '0.1'


class DatabaseSingleton():
    """
    This class manage our connection to a database
    """


    __client = None


    @classmethod
    def __get_connection(cls):
        """
        This method create our client
        """

        Session = async_sessionmaker(bind=create_async_engine(config.DATABASE_URL, echo=True))

        return Session


    def __new__(cls, *args, **kwargs):
        
        if cls.__client==None:
            cls.__client = cls.__get_connection()

        return cls.__client


    @classmethod
    async def post_register_action(cls, id:int, method:str, path:str, status_code:int):
        """
        This method log a user action
        """

        action = None

        async with cls.__client() as session:

            action = UserActionModel(user_id=id, method=method, path=path, status_code=status_code)
            session.add(action)

            await session.commit()
        
        return action


    @classmethod
    async def get_training_document(cls, topic_name:str, document_name:str):
        """
        This method search a training document

        :param topic_name: str: The topic name
        :param document_name: str: The document name
        :return: a training document instance
        """

        training_document = None

        async with cls.__client() as session:

            topic_exists = await session.execute(select(exists().where(TopicModel.topic_name==topic_name)))

            if topic_exists.scalar():

                topic = (
                    await session.execute(select(TopicModel).filter_by(topic_name=topic_name))
                ).scalars().first()

                training_document = (
                    await session.execute(select(TrainingDocumentModel).filter_by(topic_id=topic.id, document_name=document_name))
                ).scalars().first()
                
                training_document = training_document.content
        
        return training_document


    @classmethod
    async def get_active_user(cls, username:str):
        """
        This method get an user
        """

        user = None

        async with cls.__client() as session:

            user = (
                await session.execute(select(UserModel).filter_by(username=username))
            ).scalars().first()
        
        return user


    @classmethod
    async def is_existing_user(cls, username:str):
        """
        This method verify that an user exists
        """

        user = False

        async with cls.__client() as session:

            user = (await session.execute(select(exists().where(UserModel.username==username)))).scalar()
        
        return user
    

    @classmethod
    async def get_workshop(cls):

        async with cls.__client() as session:
            random_row = (
                await session.execute(select(TrainingDocumentModel)
                .options(joinedload(TrainingDocumentModel.topic))
                .order_by(func.random()))
            ).scalars().first()

        return {'topic':random_row.topic.topic_name, 'content':random_row.content}
