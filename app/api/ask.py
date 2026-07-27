from fastapi import APIRouter, HTTPException

from app.agent.agent import financial_agent
from app.schemas.ask import AskRequest, AskResponse

router = APIRouter()


@router.post(
    "",
    response_model=AskResponse,
)
def ask(request: AskRequest):

    try:

        result = financial_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": request.question,
                    }
                ]
            }
        )

        answer = result["messages"][-1].content

        return AskResponse(
            answer=answer,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )