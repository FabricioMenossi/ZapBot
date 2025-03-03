"""The main Chat app."""

import reflex as rx
import reflex_chakra as rc

from zapbot.components import chat, navbar


def index() -> rx.Component:
    """The main app."""
    return rc.vstack(
        navbar(),
        chat.chat(),
        chat.action_bar(),
        background_color=rx.color("mauve", 1),
        color=rx.color("mauve", 12),
        min_height="100vh",
        align_items="stretch",
        spacing="0",
    )

async def api_test(item_id: int):
    return {"minha resposta": item_id} 


# Add state and page to the app.
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="violet",
    ),
)
app.add_page(index)
app.api.add_api_route("/items/{item_id}", api_test)
