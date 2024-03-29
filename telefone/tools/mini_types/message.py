import typing

from telefone.api import ABCAPI, API

from telefone_types import APIMethods, StatePeer
from telefone_types.objects import (
    ForceReply,
    InlineKeyboardMarkup,
    Message,
    MessageEntity,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)


class MessageMin(Message):
    unprepared_ctx_api: typing.Optional[typing.Any] = None
    state_peer: typing.Optional[StatePeer] = None

    @property
    def ctx_api(self) -> typing.Union["ABCAPI", "API"]:
        return getattr(self, "unprepared_ctx_api")

    async def answer(
        self,
        text: typing.Optional[str] = None,
        parse_mode: typing.Optional[str] = None,
        entities: typing.Optional[typing.List["MessageEntity"]] = None,
        disable_web_page_preview: typing.Optional[bool] = None,
        disable_notification: typing.Optional[bool] = None,
        protect_content: typing.Optional[bool] = None,
        reply_to_message_id: typing.Optional[int] = None,
        allow_sending_without_reply: typing.Optional[bool] = None,
        reply_markup: typing.Optional[
            typing.Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        **kwargs
    ) -> Message:
        params = APIMethods.get_params(locals())
        return await self.ctx_api.send_message(chat_id=self.chat.id, **params)

    async def reply(
        self,
        text: typing.Optional[str] = None,
        parse_mode: typing.Optional[str] = None,
        entities: typing.Optional[typing.List["MessageEntity"]] = None,
        disable_web_page_preview: typing.Optional[bool] = None,
        disable_notification: typing.Optional[bool] = None,
        protect_content: typing.Optional[bool] = None,
        allow_sending_without_reply: typing.Optional[bool] = None,
        reply_markup: typing.Optional[
            typing.Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        **kwargs
    ) -> Message:
        params = APIMethods.get_params(locals())
        return await self.ctx_api.send_message(
            chat_id=self.chat.id, reply_to_message_id=self.message_id, **params
        )

    async def forward(
        self,
        chat_id: typing.Union[int, str],
        from_chat_id: typing.Optional[typing.Union[int, str]] = None,
        disable_notification: typing.Optional[bool] = None,
        protect_content: typing.Optional[bool] = None,
        message_id: typing.Optional[int] = None,
        **kwargs
    ) -> Message:
        params = APIMethods.get_params(locals())
        return await self.ctx_api.forward_message(
            from_chat_id=self.chat.id, message_id=self.message_id, **params
        )


MessageMin.update_forward_refs()
