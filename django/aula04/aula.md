# Aula 04 - Visão Geral do Protocolo HTTP

O **HTTP (HyperText Transfer Protocol)** é o protocolo principal da web que define como os dados sã trocados entre clientes (navegadores, apps) e servidores.

---

## Request

Quando você acessa um site ou envia dados, o cliente faz uma **requisição HTTP** para o servidor

### Componentes principais da requisição:

-   **Método (Method):** Define a ação que deseja realizar (ex: buscar dados, enviar dados).
-   **URL:** O endereço do recurso (ex: `/sobre`, `/produtos`).
-   **Headers:** Informações adicionais, como tipo de conteúdo, autenticação, etc.
-   **Body (corpo):** Dados enviados no caso de métodos como POST, PUT.

### Métodos HTTP mais comuns:

| Método | Descrição                                    |
| ------ | -------------------------------------------- |
| GET    | Solicita um recurso (buscar dados)           |
| POST   | Envia dados para o servidor (ex: formulário) |
| PUT    | Atualiza um recurso existente                |
| DELETE | Exclui um recurso                            |
| PATCH  | Atualiza parcialmente um recurso             |

---

## Response

Após receber a requisição, o servidor responde com uma **resposta HTTP**, que inclui:

-   **Status Code:** Código numérico que indica o resultado da requisição.
-   **Headers:** Informações sobre a resposta (tipo do conteúdo, tamanho, etc).
-   **Body:** O conteúdo solicitado (ex: HTML, JSON, imagens).

---

## Códigos de Status HTTP (Status Codes)

| Código | Significado                                        |
| ------ | -------------------------------------------------- |
| 200    | OK – Requisição bem sucedida                       |
| 201    | Created – Recurso criado com sucesso               |
| 301    | Moved Permanently – Recurso movido permanentemente |
| 400    | Bad Request – Requisição inválida                  |
| 401    | Unauthorized – Falta autenticação                  |
| 403    | Forbidden – Proibido acessar o recurso             |
| 404    | Not Found – Recurso não encontrado                 |
| 500    | Internal Server Error – Erro no servidor           |
