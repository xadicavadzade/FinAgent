from fastapi import APIRouter, HTTPException

from app.agent.agent import financial_agent
from app.schemas.ask import AskRequest, AskResponse

router = APIRouter()


@router.post(
     "/ask",
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
        import traceback
        traceback.print_exc()

        return {
            "type": type(e).__name__,
            "message": str(e),
        }