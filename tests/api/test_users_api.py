import pytest
import requests

pytestmark = pytest.mark.api


class TestUsersAPI:

    @pytest.mark.smoke
    def test_listar_usuarios_retorna_200(self, api_base_url):
        response = requests.get(f"{api_base_url}/users?page=2")

        assert response.status_code == 200
        body = response.json()
        assert "data" in body
        assert len(body["data"]) > 0

    def test_buscar_usuario_existente(self, api_base_url):
        response = requests.get(f"{api_base_url}/users/2")

        assert response.status_code == 200
        assert response.json()["data"]["id"] == 2

    def test_buscar_usuario_inexistente_retorna_404(self, api_base_url):
        response = requests.get(f"{api_base_url}/users/23")

        assert response.status_code == 404

    def test_criar_usuario(self, api_base_url):
        payload = {"name": "morpheus", "job": "leader"}
        response = requests.post(f"{api_base_url}/users", json=payload)

        assert response.status_code == 201
        body = response.json()
        assert body["name"] == payload["name"]
        assert body["job"] == payload["job"]
        assert "id" in body

    def test_atualizar_usuario(self, api_base_url):
        payload = {"name": "morpheus", "job": "zion resident"}
        response = requests.put(f"{api_base_url}/users/2", json=payload)

        assert response.status_code == 200
        assert response.json()["job"] == "zion resident"

    def test_deletar_usuario(self, api_base_url):
        response = requests.delete(f"{api_base_url}/users/2")

        assert response.status_code == 204
