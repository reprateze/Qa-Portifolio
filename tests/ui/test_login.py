import pytest

pytestmark = pytest.mark.ui


class TestLogin:

    @pytest.mark.smoke
    def test_login_com_credenciais_validas(self, login_page):
        login_page.login("standard_user", "secret_sauce")

        assert login_page.is_logged_in(), "Usuário deveria acessar a lista de produtos após login"

    def test_login_com_senha_invalida(self, login_page):
        login_page.login("standard_user", "senha_errada")

        assert "do not match" in login_page.get_error_message().lower()

    def test_login_usuario_bloqueado(self, login_page):
        login_page.login("locked_out_user", "secret_sauce")

        assert "locked out" in login_page.get_error_message().lower()

    @pytest.mark.parametrize("username,password", [
        ("", "secret_sauce"),
        ("standard_user", ""),
        ("", ""),
    ])
    def test_login_com_campos_vazios(self, login_page, username, password):
        login_page.login(username, password)

        assert login_page.get_error_message() != ""