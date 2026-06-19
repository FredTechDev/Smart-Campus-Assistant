"""Chatbot API endpoints"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.schemas import ChatMessageCreate, ChatMessageResponse

router = APIRouter()


@router.post("/query", response_model=ChatMessageResponse)
async def send_message(
    message_data: ChatMessageCreate,
    db: AsyncSession = Depends(get_db),
):
    """
    Send a message to the chatbot
    
    Returns AI-generated response for academic FAQs
    """
    # TODO: Implement chatbot logic
    return ChatMessageResponse(
        id=1,
        student_id=message_data.student_id,
        user_message=message_data.message,
        bot_response="I'm here to help with your academic questions!",
        created_at=None,
    )


@router.get("/history/{student_id}")
async def get_chat_history(
    student_id: str,
    limit: int = 50,
    db: AsyncSession = Depends(get_db),
):
    """
    Get chat history for a student
    
    - **student_id**: Student ID
    - **limit**: Maximum number of messages (default: 50)
    """
    # TODO: Implement history retrieval
    return {"student_id": student_id, "messages": []}
