class BasePage:
    """Classe base com comportamentos comuns a todas as páginas."""

    def __init__(self, page):
        self.page = page

    def goto(self, path: str = "/"):
        self.page.goto(path)

    def title(self) -> str:
        return self.page.title()
