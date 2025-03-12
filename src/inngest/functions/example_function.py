import logging
from inngest import Context, Step, TriggerEvent
from src.inngest.client import inngest_client

@inngest_client.create_function(
    fn_id="example_function",
    # Event that triggers this function
    trigger=TriggerEvent(event="app/example_function"),
)
async def example_function(ctx: Context, step: Step) -> str:
    """
    An example function that demonstrates how to add more functions.
    """
    ctx.logger.info(f"Example function triggered with event: {ctx.event}")
    return "example completed" 