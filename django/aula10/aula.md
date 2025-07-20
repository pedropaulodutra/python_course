# Aula 10 - Entendendo os Arquivos Estáticos no Django

Arquivos estáticos são CSS, JS, imagens, fontes e outros que não são gerados dinamicamente. Eles são essenciais para o visual e a interação da sua aplicação.

No Django, trabalhamos com eles de forma organizada. O framework oferece uma estrutura para agrupar e servir esses arquivos no ambiente de desenvolvimento e prepará-los para produção.

---

## Estrutura esperada

Dentro de um app Django, você pode criar uma pasta chamada `static`, assim:

```bash
meu_app/
├── static/
│   └── meu_app/
│       ├── style.css
│       └── script.js
```

Observe que, dentro da pasta `static`, você cria outra pasta com o nome do app. já conversamos sobre isso, se chama `namespace` e ajuda a evitar conflitos quando múltiplos apps têm arquivos com o mesmo nome (por exemplo, dois style.css diferentes).
