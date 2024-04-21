"""The home page of the app."""

from UCLA import styles
from UCLA.templates import template
from .state import TutorialState
import reflex as rx

import reflex as rx

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question),
            text_align="right",
        ),
        rx.box(
            rx.text(answer),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            TutorialState.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=TutorialState.question,
            placeholder="Ask a question",
            on_change=TutorialState.set_question,
            ),
        rx.button("Ask", on_click=TutorialState.answer),
    )



@template(route="/", title="Chat")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )