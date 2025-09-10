from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from ..contract.ai_coding_cmd import QuestionRequest, ResponseModel
from ..local.ai_coding_local import AiCodingLocalService


ai_coding_router = APIRouter()


@ai_coding_router.post("/weather")
async def weather(request: QuestionRequest):
    ai_coding_local_service = AiCodingLocalService()
    question = request.question
    answer = ai_coding_local_service.get_weather(question)
    if not answer:
        return ResponseModel(code=400, message='bad request')
    return StreamingResponse(answer, media_type="text/plain; charset=utf-8")

