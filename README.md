# AniSearch - Velho Projeto, Novos Rumos

AniSearch é uma aplicação que surgiu de um antigo projeto desenvolvido para o Discord. Este projeto é o "coração" do bot, mas a versão anterior apresentava problemas de vazamento de memória e falhas no planejamento do código, resultando em uma aplicação ineficiente. Agora, apresentamos uma versão pública e open-source que qualquer pessoa pode modificar, aprimorar e evoluir.

<p align="center">
  <img src="https://media1.tenor.com/m/MKL7YfYYng0AAAAd/kanna-kamui-anime.gif" alt="Anime GIF">
</p>

## Como Funciona?

A nova versão do AniSearch é simples e intuitiva, enquanto a versão em desenvolvimento é mais complexa e robusta. Atualmente, as opções disponíveis são limitadas, mas podem ser expandidas futuramente.

### Comandos Disponíveis

| Prefixo | Comando      | Descrição                  | Uso                                    |
|---------|--------------|---------------------------|----------------------------------------|
| **-n**  | **--name**   | Insere o nome da busca    | `python client.py -n "nome do anime"`|

### Estrutura da Resposta

Ao buscar por um anime, a aplicação retorna uma lista contendo dicionários, com a seguinte estrutura:

```python
Resposta: [{"nome do site": [{'search': 'pesquisa', 'website': 'site onde encontrou', 'title': 'nome do anime', 'url': 'url do anime'}, {anime}, {anime}]}, ...]
```

Se nenhum anime for encontrado em um site específico, a resposta será:

```python
Resposta: {"nome do site": None}
```

## Configuração e Execução
### dependências:
- aiohttp

A aplicação deve ser executada dentro de um client, que neste caso é o `client.py`. Você pode expandir a aplicação, adicionando lógicas, ações e comandos. A AniSearch foi projetada como um módulo, permitindo que você:

- Crie uma interface gráfica
- Desenvolva novos sistemas de salvamento e caching
- Implemente pós-processamento e outras funcionalidades

É semelhante ao `discord.py`, onde a AniSearch é a api do discord e o bot como um client.
