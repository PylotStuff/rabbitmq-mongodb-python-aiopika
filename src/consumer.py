import logging

from aio_pika.message import IncomingMessage
from aio_pika.queue import Queue
from motor.motor_asyncio import AsyncIOMotorClient
from src.utils.abstract_rabbitmq_consumer import RabbitMQConsumer

logger = logging.getLogger(__name__)

class Consumer(RabbitMQConsumer):
    def __init__(
            self,
            queue: Queue,
            db_client: AsyncIOMotorClient,
    ):
        super().__init__(
            queue=queue,
            db_client=db_client,
        )

        self.db_client
    async def process_message(self, orig_message: IncomingMessage):
        logger.info(orig_message)
