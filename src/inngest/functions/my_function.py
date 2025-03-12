import logging
from inngest import Context, Step, TriggerEvent
from src.inngest.client import inngest_client

@inngest_client.create_function(
    fn_id="my_function",
    # Event that triggers this function
    trigger=TriggerEvent(event="app/my_function"),
)
async def my_function(ctx: Context, step: Step) -> str:
    ctx.logger.info(ctx.event)
    return "done" 