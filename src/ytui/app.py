from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Input, DataTable

from .yt_tools import search_youtube

class YtuiApp(App):
    ROWS = [ ("index", "title", "channel") ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        yield Input(placeholder="YouTube Search", type = "text", id = "search")
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*self.ROWS[0])
        table.add_rows(self.ROWS[1:])

    @on(Input.Submitted, "#search")
    def handle_search(self, event: Input.Submitted) -> None:
        query = event.value.strip()

        if not query:
            self.notify("Enter a search term.", severity="warning")
            return

        self.notify(f"Submitted: {query}", markup=False)

        results = search_youtube(query, 25)

        rows = []
        for i, video in enumerate(results):
            rows.append((i, video.get("title"), video.get("channel")))

        table = self.query_one(DataTable)
        table.clear()
        table.add_rows(rows)
