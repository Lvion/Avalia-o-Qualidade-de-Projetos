
# Análise Crítica do Projeto Oficina Washi Car

Link: [https://github.com/orgs/ICEI-PUC-Minas-PPLES-TI/teams/oficina-washi-car](https://github.com/orgs/ICEI-PUC-Minas-PPLES-TI/teams/oficina-washi-car)

A análise crítica do projeto revela várias áreas que precisam de melhorias significativas para garantir sua robustez, segurança, escalabilidade e manutenibilidade, alinhando-o com as melhores práticas de desenvolvimento. A seguir, abordamos os principais pontos de melhoria identificados em várias dimensões do projeto.

## 1. **Arquitetura**
   - **Falta de separação clara entre camadas**: A arquitetura do projeto carece de uma divisão explícita entre as camadas de apresentação, lógica de negócios e dados, o que dificulta a manutenção e evolução do sistema.
   - **Código muito acoplado e pouco coeso**: A falta de coesão entre os componentes e o alto acoplamento entre as classes e módulos prejudicam a reutilização e a manutenção do código.
   - **Falta de documentação técnica de qualidade**: A ausência de documentação técnica adequada impede a compreensão do sistema e dificulta a integração de novos membros à equipe, além de dificultar a resolução de problemas.

## 2. **Segurança**
   - **Validações básicas e insuficientes**: O sistema não realiza validações suficientes nos dados inseridos, o que pode levar a falhas de segurança e dados inconsistentes.
   - **Ausência de tratamento adequado para dados sensíveis**: Dados sensíveis, como senhas e informações pessoais, não são protegidos de forma eficaz, expondo o sistema a riscos de vazamentos de informações.
   - **Falta de logs de auditoria**: A ausência de logs de auditoria impede a rastreabilidade de ações no sistema, dificultando a identificação e correção de falhas de segurança.
   - **Sem proteção contra ataques comuns**: O sistema não possui medidas adequadas para proteger contra ataques comuns, como injeção de SQL.

## 3. **Gestão de Dados**
   - **Modelos muito simplificados**: Os modelos de dados são simplistas e não refletem adequadamente as necessidades do negócio, o que pode gerar inconsistências e dificuldades na manipulação de dados.
   - **Falta de backup strategy**: A falta de uma estratégia de backup deixa o sistema vulnerável à perda de dados importantes em caso de falhas.

## 4. **Experiência do Usuário**
   - **Ausência de feedback adequado**: O sistema não fornece feedback claro e eficaz aos usuários, dificultando a interação e causando frustração.
   - **Falta de sistema de notificações**: A ausência de um sistema de notificações impede que os usuários sejam informados sobre eventos importantes dentro do sistema.
   - **Sem tratamento adequado de erros**: A falta de tratamento de erros adequado torna o sistema propenso a falhas inesperadas, impactando negativamente a experiência do usuário.
   - **Interface básica e pouco intuitiva**: A interface do usuário é simples e não é intuitiva, o que dificulta a navegação e o uso do sistema.

## 5. **Manutenibilidade**
   - **Código não modular**: O código não é modular o suficiente, dificultando a compreensão, a manutenção e a adição de novas funcionalidades.
   - **Difícil de escalar**: A arquitetura do sistema não permite que ele seja escalado facilmente, o que limita o crescimento do sistema à medida que a demanda aumenta.
   - **Testes inexistentes ou insuficientes**: A falta de testes automatizados e a insuficiência de testes manuais comprometem a qualidade do software e a confiança nas mudanças realizadas.
   - **Sem padrões de código definidos**: A ausência de padrões de código dificulta a colaboração entre os membros da equipe, tornando o código desorganizado e difícil de entender.
   - **Dificuldade para adicionar novas features**: A falta de uma arquitetura bem estruturada e de testes adequados torna difícil a adição de novas funcionalidades sem causar impacto no funcionamento do sistema.

## 6. **Performance**
   - **Sem cache implementado**: A ausência de cache impede que o sistema armazene dados temporários, levando a um desempenho inferior, especialmente em operações repetitivas.
   - **Carregamento de imagens sem otimização**: A falta de otimização no carregamento de imagens prejudica a performance do sistema, especialmente em páginas que exibem muitas imagens.
   - **Falta de paginação**: A ausência de paginação em listas grandes de dados compromete a usabilidade e a performance, tornando o sistema lento e difícil de usar.
   - **Sem monitoramento de performance**: A falta de monitoramento contínuo da performance impede a identificação de gargalos e a melhoria do desempenho do sistema.

## 7. **Integração**
   - **Ausência de API REST**: A falta de uma API REST dificulta a integração do sistema com outros serviços e plataformas externas.
   - **Falta de documentação de integração**: A ausência de documentação sobre como integrar o sistema com outras aplicações torna o processo de integração mais difícil e propenso a erros.

## 8. **Infraestrutura**
   - **Falta de CI/CD**: A ausência de integração contínua e entrega contínua (CI/CD) impede que o sistema seja implantado de forma rápida e segura, além de dificultar a automação de testes e deploys.
   - **Sem containerização**: A falta de containerização impede que o sistema seja facilmente replicado e escalado em diferentes ambientes.
   - **Ausência de monitoramento**: A ausência de monitoramento da infraestrutura dificulta a identificação de falhas e o ajuste da performance.

## 9. **Escalabilidade**
   - **Arquitetura monolítica**: A arquitetura monolítica limita a capacidade de escalar o sistema horizontalmente e torna a manutenção mais complexa.
   - **Dificuldade para escalar horizontalmente**: A arquitetura atual não facilita a escalabilidade horizontal, o que pode prejudicar a capacidade do sistema de lidar com aumentos na carga de trabalho.
   - **Dependências fortemente acopladas**: O forte acoplamento entre os componentes do sistema dificulta a modificação e a escalabilidade do sistema.
   - **Falta de estratégia de crescimento**: A ausência de uma estratégia de crescimento impede que o sistema seja preparado para suportar futuras expansões de capacidade.

# Refatoração

### 1. Cadastrar Dados (Cliente)

**ANTES:**

```python
# models.py
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

# views.py
def cadastrar_cliente(request):
    if request.method == 'POST':
        cliente = Cliente.objects.create(
            nome=request.POST['nome'],
            email=request.POST['email'],
            telefone=request.POST['telefone']
        )
        return redirect('home')
    return render(request, 'cadastro.html')
```

**DEPOIS:**

```python
# models/cliente.py
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

# forms/cliente_form.py
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']
        
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if not telefone.isdigit():
            raise ValidationError("Telefone deve conter apenas números")
        return telefone

# services/cliente_service.py
class ClienteService:
    def cadastrar_cliente(self, dados):
        form = ClienteForm(dados)
        if form.is_valid():
            cliente = form.save()
            self.enviar_email_boas_vindas(cliente)
            return cliente
        return None

# views/cliente_view.py
def cadastrar_cliente(request):
    if request.method == 'POST':
        service = ClienteService()
        cliente = service.cadastrar_cliente(request.POST)
        if cliente:
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('home')
    return render(request, 'cadastro.html', {'form': ClienteForm()})
```

#### Tipo de refatoração aplicada:

 Separação de responsabilidades:
- Movimentação da lógica de negócios para a camada de serviços (ClienteService).
- Criação de uma camada específica para validação (uso do forms.ClienteForm).

 Melhoria na validação:
- Validação mais robusta para o campo telefone e uso de tipos adequado(EmailField).

Modularização:
- Separação do código em diferentes arquivos para facilitar manutenção (models/cliente.py, forms/cliente_form.py, services/cliente_service.py, views/cliente_view.py).

Adição de feedback ao usuário:
- Utilização de mensagens informativas (messages.success).

### 2. Agendar Serviço

**ANTES:**

```python
# views.py
def agendar_servico(request):
    if request.method == 'POST':
        agendamento = Agendamento.objects.create(
            cliente=request.user.cliente,
            servico_id=request.POST['servico'],
            data=request.POST['data']
        )
        return redirect('home')
    return render(request, 'agendar.html')
```

**DEPOIS:**

```python
# services/agendamento_service.py
class AgendamentoService:
    def verificar_disponibilidade(self, data, servico):
        return not Agendamento.objects.filter(
            data=data,
            status='CONFIRMADO'
        ).exists()

    def criar_agendamento(self, cliente, servico, data):
        if self.verificar_disponibilidade(data, servico):
            agendamento = Agendamento.objects.create(
                cliente=cliente,
                servico=servico,
                data=data,
                status='PENDENTE'
            )
            self.notificar_novo_agendamento(agendamento)
            return agendamento
        return None

# views/agendamento_view.py
@login_required
def agendar_servico(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            service = AgendamentoService()
            agendamento = service.criar_agendamento(
                request.user.cliente,
                form.cleaned_data['servico'],
                form.cleaned_data['data']
            )
            if agendamento:
                messages.success(request, "Agendamento realizado!")
                return redirect('home')
            messages.error(request, "Horário indisponível")
    return render(request, 'agendar.html', {'form': AgendamentoForm()})
```

#### Tipo de refatoração aplicada:

Introdução de lógica de domínio em serviços:
- Transferência da lógica de agendamento para o serviço (AgendamentoService), incluindo validações como a verificação de disponibilidade.

Separação de responsabilidades:
- Isolamento da lógica de negócio (ex.: verificação de disponibilidade e notificação) da camada de apresentação (views.agendamento_view).

Melhoria na reutilização:
- Criação de métodos reutilizáveis no serviço, como verificar_disponibilidade e criar_agendamento.

Melhoria na experiência do usuário:
- Adição de mensagens claras em caso de sucesso ou falha no agendamento (messages.success, messages.error).

### 3. Enviar Orçamento


**ANTES:**

```python
# views.py
def enviar_orcamento(request, agendamento_id):
    if request.method == 'POST':
        orcamento = Orcamento.objects.create(
            agendamento_id=agendamento_id,
            valor=request.POST['valor'],
            descricao=request.POST['descricao']
        )
        # Envia email direto na view
        send_mail(
            'Novo Orçamento',
            f'Valor: R${orcamento.valor}',
            'from@example.com',
            [orcamento.agendamento.cliente.email]
        )
        return redirect('home')
```

**DEPOIS:**

```python
# services/orcamento_service.py
class OrcamentoService:
    def __init__(self):
        self.notificador = NotificacaoService()

    def criar_orcamento(self, agendamento, dados):
        form = OrcamentoForm(dados)
        if form.is_valid():
            orcamento = form.save(commit=False)
            orcamento.agendamento = agendamento
            orcamento.status = 'PENDENTE'
            orcamento.save()
            
            self.notificador.notificar_novo_orcamento(orcamento)
            return orcamento
        return None

# services/notificacao_service.py
class NotificacaoService:
    def notificar_novo_orcamento(self, orcamento):
        template = 'emails/novo_orcamento.html'
        context = {'orcamento': orcamento}
        
        send_mail(
            'Novo Orçamento Disponível',
            render_to_string(template, context),
            'from@example.com',
            [orcamento.agendamento.cliente.email],
            html_message=render_to_string(template, context)
        )

# views/orcamento_view.py
@staff_member_required
def enviar_orcamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    
    if request.method == 'POST':
        service = OrcamentoService()
        orcamento = service.criar_orcamento(agendamento, request.POST)
        
        if orcamento:
            messages.success(request, "Orçamento enviado com sucesso!")
            return redirect('lista_orcamentos')
            
    return render(request, 'criar_orcamento.html', {
        'form': OrcamentoForm(),
        'agendamento': agendamento
    })
```

#### Tipo de refatoração aplicada:

Extração de lógica para serviços:
- A lógica para criação de orçamentos e envio de notificações foi movida para a camada de serviços (OrcamentoService e NotificacaoService).

Separação de responsabilidades:
- Divisão entre lógica de negócio (criação de orçamento) e notificações, garantindo modularidade.

Melhoria na manutenibilidade:
- Uso do formulário (OrcamentoForm) para validação e simplificação da view.

Aumento da coesão:
- Cada classe agora é responsável por uma tarefa específica (ex.: NotificacaoService cuida apenas das notificações).

# Conclusão

Este projeto, quando otimizado com as melhorias propostas, pode proporcionar uma experiência de usuário mais fluida, além de garantir maior robustez e segurança. A refatoração do código, melhoria na organização do sistema, e a adoção de boas práticas de segurança e arquitetura permitirão que o projeto tenha maior escalabilidade e manutenção mais eficiente no longo prazo.
