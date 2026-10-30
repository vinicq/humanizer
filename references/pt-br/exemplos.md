# Exemplos com fatos controlados (português)

Estes exemplos complementam as regras R01-R12 e o catálogo em português ([padroes.md](padroes.md)). São fictícios e servem para calibrar quanto mudar, não como evidência sobre produtos ou pessoas. Os exemplos em inglês estão em [../en/examples.md](../en/examples.md).

#### Mensagem profissional

**Fatos do cenário hipotético:** a homologação encontrou dois erros no formulário de cadastro; a publicação precisa esperar a correção. Não há prazo nem responsável definidos.

**Antes:** "É importante ressaltar que a homologação identificou dois erros no cadastro, evidenciando a necessidade fundamental de aguardar a correção antes da publicação."

**Depois:** "A homologação encontrou dois erros no cadastro. A publicação deve aguardar a correção."

Não acrescente "a equipe corrigirá hoje" nem "vou avisar o cliente": seriam compromissos novos.

#### Precisão de uma etapa

**Antes:** "A revisão do contrato viabilizou a contratação da equipe."

**Depois possível:** "A revisão do contrato permitiu contratar a equipe."

Não troque por "Contratamos a equipe": a frase original descreve a condição que tornou a contratação possível e não confirma que ela aconteceu.

#### Comentário comum de PR

**Fatos do cenário hipotético:** o parser já aceita `--dry-run`; os testes de CLI não cobrem essa opção; o pedido é completar a cobertura sem mudar o comportamento.

**Texto:** "O parser já aceita `--dry-run`, mas os testes de CLI não cobrem a opção. Acrescente os casos correspondentes sem alterar o comportamento implementado."

Não afirme que a suíte falhou nem amplie o pedido para refatorar o parser.

#### Avaliação sem extrapolação

**Fatos do cenário hipotético:** na entrevista, a pessoa explicou como registra defeitos, mas não respondeu à pergunta sobre autenticação da API.

**Texto:** "A pessoa explicou como registra defeitos. Não respondeu à pergunta sobre autenticação da API."

Não transforme a falta de resposta em "não tem experiência com APIs". Essa conclusão exigiria outra evidência.
