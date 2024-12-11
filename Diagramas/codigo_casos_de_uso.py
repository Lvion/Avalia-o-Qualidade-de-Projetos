
#Cadastrar dados(models.pyl):
class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True, verbose_name='E-mail')
    telefone = models.CharField(max_length=19, verbose_name='Telefone')
    endereco = models.CharField(max_length=100)
    cep = models.IntegerField()
    complemento = models.CharField(max_length=100)
    
#Agendar serviço(models.py)
class Agendamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.DateTimeField()
    descricao = models.CharField(max_length=300)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    
    
#Validar Acesso (settings.py)
    AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
    
#Enviar Orçamento/Registrar (models.py)
class Orcamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    preco = models.FloatField()
    descricao = models.CharField(max_length=500)
    tempo_servico = models.IntegerField()
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    
#Cadastrar Parceiro (models.py)
class Parceiro(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_responsavel = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco_estabelecimento = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=30)
    nome_fantasia = models.CharField(max_length=30)
    cnpj = models.BigIntegerField()
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    
#Cadastrar Serviços
class Servico(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=30)
    descricao = models.TextField()
    preco = models.FloatField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
#Validação de dados
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Validações do AllAuth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
    
#Acessar area do Cliente (URL.py)
path("cliente", agendamento, name='agendamento'),
path('cadastro-cliente/', cadastro_cliente, name='cadastro-cliente'),

#Acessar area do Parceiro (URL.py)
path("login-parceiro", cadastro_parceiro, name='cadastro_parceiro'),

#Visualizar tabela de Serviçoes(URL.py)
path("servicos", ServicoListView.as_view(), name='list-servicos'),

#Acessar aba de parcerias (URL.py)
path("parceiros", ParceirosListView.as_view(), name='list-parceiros'),

#Acessar a localização (URL.py)
path('', home, name='home'),

#Acessar o horário de funcionamento (URL.py)
path('', home, name='home'),