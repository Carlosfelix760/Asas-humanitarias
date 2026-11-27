# Asas Humanitárias Internacional
Protótipo HTML/CSS/JS + Flask + SQLite. Python 3.10+.

## Executar
`python -m pip install -r requirements.txt`

`python app.py`

Abra http://127.0.0.1:8000. O banco é criado automaticamente.

## GitHub
Envie os arquivos desta pasta ao repositório. GitHub Pages hospeda somente o conteúdo de public/ (sem cadastro funcional). Para backend use hospedagem Python com disco persistente, comando `gunicorn app:app`, HTTPS e DB_PATH apontando para o disco persistente. Não envie o banco ao GitHub.

## Antes de uso real
Protótipo não pronto para coletar dados reais: implementar autenticação administrativa, limitação de requisições, política LGPD, retenção e exclusão, segurança e revisão jurídica. CPF desativado por minimização. Doações demonstrativas; sem integração financeira. Google Translate depende de serviço externo e disponibilidade/elegibilidade do widget. Verifique direitos de uso das fotos. Nenhuma afiliação oficial ou aeronave em operação é alegada. Missões dependem de autorizações, consentimento comunitário e profissionais habilitados.
