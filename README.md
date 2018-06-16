# Trabalho Final de DAC

Sistema para gerenciamento de estágios. A descrição completa  do problema pode ser lida [clicando aqui](./descricao-trabalho.pdf)

## Configurando

Copie o arquivo `contrib/.env.example` para a raíz com o nome `.env`, e coloque uma nova secret key.

### Pegando uma nova Secret Key

Rode no terminal:
```
python contrib/secret_gen.py
```

### Instruções para teste em virtual env

Primeiro crie um virtualenv na pasta raiz do projeto (console)

```
python -m venv venv
```

Ative o virtual env (windows)

```
venv\Scripts\activate.bat
```

Instale as dependências
```
pip install -r requirements.txt
```

Rode as migrações
```
python manage.py migrate
```

Crie um super usuário para usar a área administrativa
```
python manage.py createsuperuser
```

Inicie o servidor
```
python manage.py runserver
```

## Grupo

- Beatriz Lopes
- Caio Silva
- Daniel Chactoura
- Ricardo José
- Wallace Coelho
