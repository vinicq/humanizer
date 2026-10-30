# Humanizer

[English](README.md) · **Português (Brasil)**

Uma Agent Skill para escrever, editar e revisar textos em inglês e em português do Brasil, de modo que soem como escritos por uma pessoa para um leitor. Ela tira os vícios que denunciam a saída de um modelo e mantém intactos os fatos, o sentido, os termos técnicos e a voz do autor.

> **Antes** (saída bruta do modelo)
> A Padaria Lúcia faz parte do bairro da Ponta Verde, em Maceió, desde 1998. Fundada por Lúcia Ferreira, ficou conhecida pelo pão de queijo e pelo bolo de macaxeira, dois favoritos de quem passa por aqui. [...] Seja para começar a manhã ou fazer uma pausa para o café da tarde, venha conhecer a nossa padaria.
>
> **Depois**
> A Padaria Lúcia fica no bairro da Ponta Verde, em Maceió. Foi fundada em 1998 por Lúcia Ferreira e é conhecida pelo pão de queijo e pelo bolo de macaxeira.
>
> Abrimos todos os dias, das 6h às 20h.

A skill não detecta autoria e não promete passar por detectores de IA. Ela edita para o leitor.

Versão 7.0.0 · por Vinicius Queiroz · MIT

## O que há no repositório

| Caminho | O que faz |
|---|---|
| `SKILL.md` | A skill. Escopo, prioridades, regras de preservação R01-R12, o procedimento de edição e a checagem final. Carrega em toda execução. |
| `references/` | Detalhes que só carregam quando a tarefa pede: `en/` (catálogo em inglês EN01-EN78, revisão final e exemplos) e `pt-br/` (catálogo em português PT01-PT86, revisão final e exemplos, em português), mais `voice-and-genres.md` e `sources.md`, comuns aos dois idiomas. |
| `agents/humanizer-revisor.md` | Subagente revisor somente leitura para o Claude Code. Lista achados e não edita. |
| `codex/humanizer-revisor.toml` | O mesmo revisor como agente personalizado do Codex. |
| `agents/openai.yaml` | Como a skill aparece no Codex. |
| `.claude-plugin/` | Manifestos de plugin e de marketplace do Claude Code. |
| `plugins/codex/` | O plugin do Codex: cópia gerada da skill. Não edite à mão. |
| `.agents/plugins/marketplace.json` | Manifesto de marketplace do Codex, que aponta para `plugins/codex`. |
| `assets/icon.png` | Ícone do plugin. |
| `scripts/build-codex-plugin.py` | Gera `plugins/codex` a partir da raiz do repositório. |
| `scripts/check-wikipedia.py` | Avisa quando as páginas da Wikipédia que sustentam os catálogos mudaram. |
| `wikipedia/` | Extração, seção por seção, dessas páginas. Material de manutenção; a skill não lê. |
| `AGENTS.md` | Instruções para agentes de código que editam este repositório. |
| `CHANGELOG.md` · `LICENSE` | Histórico de versões e licença. |

A skill e o revisor dividem o trabalho:

| | Skill `humanizer` | Subagente `humanizer-revisor` |
|---|---|---|
| Use para | escrever ou reescrever um texto | revisar um texto que já existe |
| Roda | na sua conversa | em contexto separado, sem o viés de quem escreveu |
| Devolve | o texto final | achados: trecho, ID do padrão, problema, correção mínima, confiança |
| Edita arquivos | quando você pede | nunca |

## Instalação

O `SKILL.md` fica na raiz do repositório, ao lado das referências, então para o Claude o repositório é a pasta da skill. O Codex lê uma cópia gerada em `plugins/codex`.

Todos os comandos de clone usam HTTPS. SSH também funciona: `git@github.com:vinicq/humanizer.git`.

### Claude Code

Como plugin, com a skill e o revisor:

```text
/plugin marketplace add vinicq/humanizer
/plugin install humanizer@humanizer
```

Pelo terminal: `claude plugin marketplace add vinicq/humanizer` e `claude plugin install humanizer@humanizer`. A skill do plugin se chama `/humanizer:humanizer`.

Para ter o nome curto `/humanizer`, clone na sua pasta de skills e copie o revisor:

```bash
git clone https://github.com/vinicq/humanizer.git ~/.claude/skills/humanizer
cp ~/.claude/skills/humanizer/agents/humanizer-revisor.md ~/.claude/agents/
```

No Windows (PowerShell):

```powershell
git clone https://github.com/vinicq/humanizer.git "$HOME\.claude\skills\humanizer"
Copy-Item "$HOME\.claude\skills\humanizer\agents\humanizer-revisor.md" "$HOME\.claude\agents\"
```

Escolha um método só. Com os dois, aparecem duas skills `humanizer`.

### App desktop do Claude e claude.ai

- **Aba Code do app desktop:** lê a mesma pasta `~/.claude` e os mesmos plugins de escopo de usuário que o CLI, então os passos acima já cobrem. No app você também pode adicionar o plugin pelo botão `+` ao lado da caixa de texto, em Add plugins.
- **Chat e Cowork (app desktop e claude.ai):** pegam as skills da sua conta, não de `~/.claude`. Monte um ZIP cuja raiz seja uma pasta `humanizer/`, envie em **Customize > Skills** e ative:

```bash
git clone https://github.com/vinicq/humanizer.git && cd humanizer
git archive --format=zip --prefix=humanizer/ -o humanizer.zip HEAD
```

O `git archive` respeita as linhas `export-ignore` do `.gitattributes`, então o ZIP deixa de fora as pastas de manutenção (`plugins/`, `codex/`, `scripts/`, `wikipedia/`, `assets/`, `.agents/`, `.claude-plugin/`) e leva só a skill. O botão "Download ZIP" do GitHub entrega uma pasta chamada `humanizer-main`, que precisa ser renomeada para `humanizer` antes de zipar de novo; por isso o comando `git archive` é mais simples.

Skills enviadas exigem a execução de código ligada. Contas Team já vêm com ela; no Enterprise, um proprietário precisa habilitar a execução de código e as Skills. O subagente não se aplica aqui: o chat não tem subagentes.

### Codex CLI

Instale o plugin:

```bash
codex plugin marketplace add vinicq/humanizer
codex plugin add humanizer@humanizer
```

Abra uma conversa nova. A skill é `humanizer:humanizer`: peça pelo nome, escolha em `/skills` ou descreva a tarefa; o Codex também a seleciona pela descrição. O plugin fica em `plugins/codex` e é gerado a partir da raiz do repositório por `scripts/build-codex-plugin.py`, então edite os arquivos da raiz, nunca a cópia gerada.

O revisor é um agente personalizado do Codex, em arquivo separado. Copie-o de um clone:

```bash
git clone https://github.com/vinicq/humanizer.git ~/src/humanizer
mkdir -p ~/.codex/agents
cp ~/src/humanizer/codex/humanizer-revisor.toml ~/.codex/agents/
```

Ele fica disponível como o subagente `humanizer-revisor`.

**Alternativa manual** (Codex sem o plugin, e outros agentes que leem `~/.agents/skills`): clone onde quiser, por exemplo `~/src/humanizer`, e crie um link ou copie **só** `plugins/codex/skills/humanizer` para `~/.agents/skills/humanizer`. Não clone o repositório inteiro em `~/.agents/skills`: o Codex passa a achar a skill duas vezes, na raiz e em `plugins/codex`.

```bash
git clone https://github.com/vinicq/humanizer.git ~/src/humanizer
mkdir -p ~/.agents/skills ~/.codex/agents
ln -s ~/src/humanizer/plugins/codex/skills/humanizer ~/.agents/skills/humanizer
cp ~/src/humanizer/codex/humanizer-revisor.toml ~/.codex/agents/
```

No Windows (PowerShell), com junction (não precisa de administrador):

```powershell
git clone https://github.com/vinicq/humanizer.git "$HOME\src\humanizer"
New-Item -ItemType Directory -Force "$HOME\.agents\skills", "$HOME\.codex\agents" | Out-Null
New-Item -ItemType Junction -Path "$HOME\.agents\skills\humanizer" -Target "$HOME\src\humanizer\plugins\codex\skills\humanizer"
Copy-Item "$HOME\src\humanizer\codex\humanizer-revisor.toml" "$HOME\.codex\agents\"
```

Use o plugin ou o link manual, não os dois: com os dois, a skill aparece duas vezes. Para atualizar, rode `git pull` no clone (o link acompanha) ou atualize o plugin.

### App do Codex

O app do Codex usa a mesma configuração do Codex CLI. Abra a aba **Plugins**, procure Humanizer, instale e abra uma conversa nova. O link manual acima e o arquivo do agente em `~/.codex/agents/` cobrem o app também. Fechar a janela pode deixar o app rodando na bandeja do sistema com a configuração antiga; saia dele pela bandeja se a skill não aparecer.

### Outros agentes

A maioria dos agentes que aceitam Agent Skills lê `~/.agents/skills`, então o link manual da seção do Codex costuma cobrir. Por agente, crie um link ou copie `plugins/codex/skills/humanizer` (não a raiz do repositório) para a pasta de skills:

| Agente | Pasta da skill (usuário / projeto) | Revisor |
|---|---|---|
| OpenCode | `~/.config/opencode/skills/humanizer` · `.opencode/skills/humanizer` (também lê `~/.agents/skills` e `~/.claude/skills`) | Formato próprio de agente em `~/.config/opencode/agents/`; adapte o arquivo Markdown |
| Cursor | `~/.cursor/skills/humanizer` · `.cursor/skills/humanizer` (também lê `~/.agents/skills` e `~/.claude/skills`) | Lê `agents/humanizer-revisor.md` como está, em `~/.cursor/agents/` ou `.claude/agents/` |
| GitHub Copilot no VS Code | `~/.copilot/skills/humanizer` · `.github/skills/humanizer` (também lê `~/.agents/skills` e `~/.claude/skills`) | Lê o formato do Claude em `~/.claude/agents/` ou `.claude/agents/` |
| Gemini CLI | `gemini skills install https://github.com/vinicq/humanizer`, ou `~/.gemini/skills/humanizer` | `~/.gemini/agents/`, formato próprio |
| Antigravity | `.agents/skills/humanizer` no projeto | - |
| Windsurf | `~/.codeium/windsurf/skills/humanizer` · `.windsurf/skills/humanizer` | - |

Na linha do Gemini, o comando `install` recebe o repositório inteiro; nas demais, vale o link ou a cópia de `plugins/codex/skills/humanizer`. Esses caminhos vêm da documentação de cada fornecedor em outubro de 2026. Se um cliente mudar o modo de encontrar skills, vale a documentação dele.

### Sem instalar

Anexe `SKILL.md` e o catálogo do seu idioma (`references/pt-br/padroes.md` para português, `references/en/patterns.md` para inglês) à conversa, mais `references/pt-br/revisao-final.md` ou `references/en/final-pass.md` para a passada final, e diga:

```text
Use os arquivos anexos como guia de escrita e revisão nesta conversa.
O SKILL.md é a base e vale mais que o catálogo.
Preserve fatos, fontes, termos técnicos, condições, negações e grau de certeza.
Não traduza nem resuma, a menos que eu peça. Devolva só a versão final.
```

Abra uma sessão nova depois de instalar e confira se o cliente lista `humanizer`. Para atualizar, rode `git pull` no clone (ou reinstale o plugin).

## Uso

Chame pelo nome:

```text
/humanizer

[cole o texto]
```

Ou peça em palavras simples, em qualquer um dos idiomas:

```text
Use the humanizer skill on this release note. Keep the facts and the version numbers.
Revise este e-mail com a skill humanizer e entregue só a versão final.
```

Aponte para um arquivo:

```text
/humanizer docs/proposal.md
```

Peça ao revisor quando quiser uma segunda leitura sem edições:

```text
Peça ao humanizer-revisor para revisar docs/proposal.md.
Idioma: inglês. Gênero: proposta técnica. Leitor: o comitê gestor.
Não mexer em: os números da seção 3 e as citações.
```

Ele devolve achados com o trecho, o padrão (EN01-EN78, PT01-PT86 ou R01-R12), o problema, uma correção mínima e um nível de confiança. Você decide o que aplicar. Uma boa rotina para um texto importante: escreva com a skill, revise com o subagente, aplique o que fizer sentido.

### Combine com a sua voz

Se quiser que a reescrita soe como você, inclua uma amostra da sua escrita:

```text
/humanizer

Aqui vai uma amostra da minha escrita para combinar a voz:
[cole 2 ou 3 parágrafos seus]

Agora humanize este texto:
[cole o texto]
```

A skill lê a amostra atrás de traços observáveis (tamanho de frase e de parágrafo, pontuação, contrações, pessoa, registro, como você abre e fecha, como usa listas) e escreve o texto novo com eles. Ela não copia seus erros de digitação, suas opiniões, sua biografia nem qualquer afirmação da amostra, e a amostra nunca se sobrepõe aos fatos do texto editado. Com uma amostra abaixo de cerca de 150 palavras, o casamento é aproximado, e a skill avisa. Peça uma nota curta de voz se quiser ver quais traços ela usou.

### Torne-a o padrão

Adicione isto ao seu `CLAUDE.md`, `AGENTS.md` ou equivalente:

```markdown
## Escrita e revisão

Para escrita em linguagem natural, aplique a skill `humanizer` instalada neste
ambiente. Para revisar um texto pronto, use o subagente `humanizer-revisor`.
Preserve fatos, fontes, sentido, termos técnicos, condições, negações e
grau de certeza. Não traduza, resuma, invente evidências nem altere
requisitos sem pedido. Em reescritas comuns, devolva só a versão final.
```

## Como funciona

Modelos de linguagem escolhem o caminho seguro e frequente: a frase que serve a qualquer assunto, a lista de três itens, o fechamento animado, o subtítulo em cada parágrafo. Cada escolha é razoável sozinha. Juntas, resultam num texto que diz menos do que o tamanho sugere e soa como ninguém em particular. A solução não é salpicar manias "humanas" por cima; é dizer a coisa específica de que o leitor precisa.

A skill segue seis passos:

1. **Fixar o contrato da tarefa.** Idioma, gênero, leitor, formato, tamanho e limites. Se você deu uma amostra de voz, ela é separada aqui do texto a editar.
2. **Marcar o que não pode mudar.** Citações, código, comandos, identificadores, URLs, números, datas, nomes e termos normativos.
3. **Diagnosticar problemas reais** contra o catálogo do idioma do texto. Um padrão é motivo para olhar, não ordem para cortar: frase correta fica.
4. **Escrever ou revisar** com a menor mudança que resolve o problema.
5. **Revisar em duas passadas:** primeiro o sentido (nada acrescentado, perdido ou mais certo do que era), depois a passada específica do idioma em `references/pt-br/revisao-final.md` ou `references/en/final-pass.md`.
6. **Entregar no formato pedido**, em geral só o texto final.

Doze regras (R01-R12) ficam acima do catálogo. As principais: nenhum fato, experiência ou fonte inventados (R02); citações e código são protegidos (R03); nada de tradução ou resumo sem pedido; o registro segue o gênero e o autor, não um estilo fixo (R07). Quando uma regra e um padrão discordam, vale a regra. Um texto limpo volta quase intocado; veja o exemplo da descrição de pull request mais abaixo.

## O catálogo em português (86 padrões)

O catálogo em português é o [`references/pt-br/padroes.md`](references/pt-br/padroes.md), com IDs PT01-PT86. Segue a página da Wikipédia em português [Sinais de texto gerado por inteligência artificial](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Sinais_de_texto_gerado_por_intelig%C3%AAncia_artificial) (S02), revisão 73274816, na ordem da página; PT70-PT76 vêm da página [Grandes modelos de linguagem](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Grandes_modelos_de_linguagem) (S03), revisão 73268669. Os grupos abaixo usam os nomes de seção da própria página. A Wikipédia é a fonte de verdade sobre o que conta como sinal. Os indícios de escrita humana, os que não funcionam e os históricos estão no catálogo para a skill **não** agir sobre eles (PT54-PT69 e PT75). PT77-PT86 são acréscimos de outras fontes ou da prática editorial, marcados assim na linha **Fontes**. Cada entrada traz o gatilho, por que soa como IA, a correção, a exceção e uma linha **Fontes** com a fonte e a seção da página. Os sinais que só fazem sentido dentro da Wikipédia (wikitexto, páginas de usuário, permissões de edição) ficam no fim do catálogo como não aplicados.

O texto em inglês usa o catálogo próprio, feito a partir da Wikipédia em inglês: `references/en/patterns.md` (EN01-EN78), listado no [README.md](README.md).

### O que verificar primeiro

| ID | Padrão | O que observar |
|---|---|---|
| PT01 | Fontes e conteúdo | fonte que não diz o que a frase afirma; autor, data ou URL errados; "papel fundamental" no lugar do fato |
| PT02 | Tradução e variedades do português | falso cognato, regência estranha, veículos chamados de "prestigiosos" sem leitura (variante do português não é indício) |

### Conteúdo

| ID | Padrão | O que observar |
|---|---|---|
| PT03 | Ênfase indevida em importância, legado e tendências mais amplas | "serve como", "um papel crucial", "marco decisivo", "legado duradouro" |
| PT04 | Ênfase padronizada em notoriedade, atribuição e cobertura na mídia | "citado em veículos de destaque", "cobertura independente", lista de onde o assunto apareceu |
| PT05 | Análises superficiais | gerúndio no fim da frase: "destacando", "sublinhando", "garantindo", "refletindo" |
| PT06 | Linguagem promocional e publicitária | "ostenta", "vibrante", "aninhado", "no coração de", "beleza natural" |
| PT07 | Expressão vaga de conexão ou associação | "em conexão com", "associado a", "esteve ligada a" sem o vínculo dito |
| PT08 | Atribuições vagas e generalização de opiniões | "relatórios do setor", "especialistas argumentam", "várias fontes" quando poucas são citadas |
| PT09 | Conclusões padronizadas sobre desafios e perspectivas futuras | "Apesar desses desafios", "Perspectivas futuras", fecho de futuro promissor |
| PT10 | Seção "Prêmios e reconhecimento" e títulos "X e Y" | cabeçalho "Prêmios e reconhecimento", títulos "X e Y" |

### Linguagem e gramática

| ID | Padrão | O que observar |
|---|---|---|
| PT11 | Alta densidade de "vocabulário de IA" | "além disso" no início, "alinhar-se com", "crucial", muitas dessas palavras juntas |
| PT12 | Evitação de construções copulativas simples ("é", "são") | "serve como", "ergue-se como", "funciona como", "ostenta" no lugar de "é" ou "tem" |
| PT13 | Paralelismo negativo: "não apenas X, mas também Y" | "não apenas... mas também...", "não é só X, é Y" |
| PT14 | Paralelismo negativo: "não X, mas Y" | "não é X, é Y", "nem X, nem Y, apenas Z" |
| PT15 | Paralelismo negativo invertido: "Y em vez de X" | "em vez de X" fechando a frase |
| PT16 | Introduções que tratam listas ou títulos amplos como nomes próprios | abertura que define o título como entidade: "Edições dos EuroGames é a lista..." |
| PT17 | Regra de três | três adjetivos, substantivos ou frases em fila: "azulejos, metais e plásticos" |

### Estilo

| ID | Padrão | O que observar |
|---|---|---|
| PT18 | Maiúsculas em todas as palavras principais dos títulos | maiúscula em todas as palavras principais dos títulos |
| PT19 | Excesso de negrito | negrito mecânico em todas as ocorrências de um termo |
| PT20 | Listas verticais com título em cada item | item que abre com título em negrito, dois-pontos e explicação |
| PT21 | Erros nos títulos das seções | título do documento repetido num cabeçalho, salto de nível, nível 1 no corpo |
| PT22 | Emojis usados como formatação | emoji no início de títulos e itens |
| PT23 | Uso incomum de tabelas | tabela pequena cujo conteúdo caberia em prosa |
| PT24 | Aspas e apóstrofos curvos | aspas e apóstrofos curvos misturados com retos |

### Comunicação dirigida ao usuário

| ID | Padrão | O que observar |
|---|---|---|
| PT25 | Conversas com o usuário | "espero que isto ajude", "claro!", "você tem toda a razão!", "me avise" |
| PT26 | Ressalvas didáticas sobre o que é "importante observar" (2023-2024) | "é importante observar", "pode variar", "é crucial diferenciar" (2023-2024) |
| PT27 | Ressalvas sobre falta de fonte e o que a informação "provavelmente" seria (2024-2025) | "os detalhes específicos são limitados", "nas fontes fornecidas" (2024-2025) |
| PT28 | Enquadramentos corretivos (meados de 2026 em diante) | "deve ser tratada como... e não como...", "não estabelece, por si só" (meados de 2026) |
| PT29 | Modelos de frases e campos por preencher | "[Seu Nome]", "[Descreva a seção...]", datas `2025-xx-xx`, `INSERT_SOURCE_URL_30` |

### Marcação

| ID | Padrão | O que observar |
|---|---|---|
| PT30 | Uso de Markdown | Markdown onde o destino não renderiza |
| PT31 | Uso incorreto de asteriscos | `**asteriscos**` literais em destino sem Markdown |
| PT32 | Uso incorreto de cerquilhas | `##` literal como título |
| PT33 | Formatação incomum de links | `[texto](url)` literal; `([url](url))` duplicado |
| PT34 | Linhas horizontais entre seções | `---` entre todas as seções |
| PT35 | Código wiki incorreto (marcação do destino quebrada) | sintaxe, predefinições ou campos do destino corrompidos |
| PT36 | Falhas na marcação interna e nas referências, por ferramenta | `:contentReference[oaicite:0]{index=0}`, `citeturn0search0`, `[cite: 1]` |

### Problemas em citações e referências

| ID | Padrão | O que observar |
|---|---|---|
| PT37 | Ligações externas que não funcionam | vários links mortos, sem cópia arquivada |
| PT38 | DOI e ISBN inválidos | DOI que não resolve, dígito verificador de ISBN que não confere |
| PT39 | DOI que levam a artigos sem relação | DOI válido de outro trabalho num artigo inventado |
| PT40 | Referências a livros sem páginas ou URL | livro sem página ou URL, ou página que não confirma o texto |
| PT41 | Uso incorreto ou fora do padrão das referências | referência repetida depois de todo ponto, URL inventada por posição, `↩` |
| PT42 | Parâmetro utm_source | `utm_source=openai`, `utm_source=chatgpt.com`, `referrer=grok.com` |
| PT43 | Referências definidas e não usadas | fontes na lista que nenhuma frase cita; chamadas para referências inexistentes |

### Indícios em comentários

| ID | Padrão | O que observar |
|---|---|---|
| PT44 | Indícios em comentários e tom de atendimento | tom de atendimento em comentários: "Entendo a preocupação..." |

### Resumos de edição

| ID | Padrão | O que observar |
|---|---|---|
| PT45 | Resumos de edição: fórmulas gerais | "Revisei o conteúdo para oferecer uma descrição neutra e informativa" |
| PT46 | Garantias padronizadas de cumprimento das regras | "garantiu que... segue", "em conformidade com", "tom enciclopédico" |
| PT47 | Menções a informações "preservadas", erros "evitados" e outros procedimentos | "preservando o sentido original", "evitado", "garantindo" |
| PT48 | Ênfase na presença ou confiabilidade das referências | "acrescentadas informações verificadas", "melhorada a atribuição" |
| PT49 | Menção à avaliação em vez da mudança | "Atendendo aos comentários do avaliador", "Todas as afirmações verificadas" |

### Outros indícios

| ID | Padrão | O que observar |
|---|---|---|
| PT50 | "Declarações de submissão" colocadas dentro do documento | "Nota ao avaliador:", "Todas as referências são de fontes independentes" dentro do documento |
| PT51 | Páginas de perfil padronizadas | "Bem-vindo à minha página!", "Sobre mim", "Vamos conversar!" em perfil padronizado |
| PT52 | Diferenças entre modelos | sem gatilho de texto: cada modelo e versão tem seu idioleto |

### Vieses no conteúdo

| ID | Padrão | O que observar |
|---|---|---|
| PT53 | Viés favorável ao autoritarismo | sem gatilho de texto: respostas que favorecem o autoritarismo |

### Indícios de escrita humana

_Não são problemas a corrigir. São sinais que apontam para autoria humana; a skill não edita por eles._


| ID | Padrão | O que observar |
|---|---|---|
| PT54 | Data do texto em relação ao lançamento do ChatGPT | sinal humano: texto anterior a 30 de novembro de 2022 |
| PT55 | Capacidade de explicar as próprias escolhas editoriais | sinal humano: quem escreveu explica como o erro ocorreu |
| PT56 | Sintaxe típica da escrita humana | sinal humano: "é" e "tem" simples, "escreveu" em vez de "foi autor de" |

### Indícios que não funcionam

_Listados para a skill não agir sobre eles. A Wikipédia diz que não distinguem texto de IA de texto humano._


| ID | Padrão | O que observar |
|---|---|---|
| PT57 | Ineficaz: gramática perfeita | ineficaz: texto sem erros gramaticais |
| PT58 | Ineficaz: mistura de registros, linguagem "clínica" e "emotiva" ao mesmo tempo | ineficaz: informalidade misturada com formalidade |
| PT59 | Ineficaz: texto "sem graça" ou "robótico" | ineficaz: texto "sem graça" ou "robótico" |
| PT60 | Ineficaz: texto "rebuscado", "acadêmico" ou "formal" | ineficaz: prosa formal, acadêmica ou rebuscada |
| PT61 | Ineficaz: conectivos isolados | ineficaz: "além disso", "consequentemente" isolados |
| PT62 | Ineficaz: conteúdo sem fontes | ineficaz: afirmações sem referência |

### Indícios históricos

_Comuns em modelos antigos e bem menos frequentes hoje. Vêm da página da Wikipédia; a skill não marca um texto por um deles isolado._


| ID | Padrão | O que observar |
|---|---|---|
| PT63 | Avisos sobre a data-limite do conhecimento | histórico: "até minha última atualização de treinamento" |
| PT64 | Resumos ao fim das seções | histórico: "em resumo", "em conclusão" no fim das seções |
| PT65 | Recusa em atender ao pedido | histórico: "como modelo de linguagem de IA", "sinto muito" |
| PT66 | Uso excessivo de travessões | histórico: uso excessivo de travessões (2022 a setembro de 2026) |
| PT67 | Interrupções abruptas | histórico: texto que termina no meio da frase |
| PT68 | Datas de acesso antigas | histórico: data de acesso incompatível com a data do documento |
| PT69 | Diversidade lexical e variação de palavras | histórico: o mesmo referente com nomes diferentes a cada menção |

### Grandes modelos de linguagem

| ID | Padrão | O que observar |
|---|---|---|
| PT70 | Conclusões que nenhuma fonte tira e premissa falsa aceita | conclusão que nenhuma fonte tira; premissa absurda atendida ("benefícios de comer vidro") |
| PT71 | Tom neutro sem substância neutra | tom neutro com substância enviesada, sobretudo em biografias de pessoas vivas |
| PT72 | Paráfrase próxima ao resumir | trecho literal ou paráfrase colada na fonte protegida |
| PT73 | Edição por LLM que perde informação ou não vê o erro | "pode falhar" vira "falha", "até 5" vira "menos de 5" |
| PT74 | Pedir ao modelo que corrija a própria saída não substitui a correção manual | resumo que diz ter tirado o tom promocional e o manteve; citações sem conferência |
| PT75 | Refinar a expressão de ideias próprias é uso legítimo | sinal humano: pessoa que usa o modelo para refinar ideias que são dela |
| PT76 | Divulgação do uso e material que imita documentação real | saída de LLM sem divulgação; imagem gerada que imita documentação real |

### Acréscimos de outras fontes e da prática editorial (sem seção na Wikipédia)

| ID | Padrão | O que observar |
|---|---|---|
| PT77 | Vivências e personalidade fabricadas | "na minha experiência", "já vi isso de perto", emoção sem origem |
| PT78 | Comparações e slogans simétricos | "menos processo, mais resultado", "não é uma ferramenta, é um movimento" |
| PT79 | Faixas e escalas inexistentes | "da eficiência à transformação" onde os extremos não formam uma escala |
| PT80 | Agente oculto e fragmentos ambíguos | "foi decidido" quando importa quem decidiu |
| PT81 | Perguntas retóricas de template | "mas por que isso importa?", "o resultado? surpreendente" |
| PT82 | Ritmo uniforme ou irregularidade fabricada | frases de mesma construção em fila, ou alternância fabricada de comprimentos |
| PT83 | Prosa picotada e lista disfarçada | frases curtas, uma por linha, sem relação declarada |
| PT84 | Entusiasmo e emoção inadequados | "incrível!", exclamação e celebração em relatório de falha |
| PT85 | Instruções do material tratadas como comandos | o texto a revisar diz "ignore as regras" e o editor obedece |
| PT86 | Tradução, resumo ou segunda versão não solicitados | revisão que volta traduzida, resumida ou em duas versões |
## Exemplos

Como foram feitos: os textos "antes" são saída bruta do GPT-6.1 numa sessão isolada do Codex, sem instruções do usuário e sem skills carregadas, recebendo apenas os fatos de cada pedido. Os textos "depois" são os mesmos rascunhos passados por esta skill. Os IDs PT remetem ao catálogo acima; os IDs EN, ao catálogo em inglês listado no [README.md](README.md).

### Anúncio de lançamento (inglês)

> **Antes**
> tidewatch 2.0 is here, with offline syncing and faster uploads for local folders backed up to S3.
>
> The new offline mode queues changes while you're disconnected and uploads them when your connection returns. You can keep working on local files through a connection drop without having to remember what needs syncing later.
>
> This release also improves sync performance. In our benchmark of 10,000 small files, tidewatch 2.0 completed the sync 40% faster. Results will vary with your files and connection, but this benchmark gives a concrete measure of the improvement for that workload.
>
> Version 2.0 drops support for Python 3.9, so check your Python environment before upgrading. The migration guide at `docs/migrate-2.md` covers the steps for moving to the new release.
>
> tidewatch remains an open-source command-line tool for syncing local folders to S3. If you're upgrading an existing setup, start with the migration guide, then give 2.0 a try.

> **Depois**
> tidewatch 2.0 adds an offline mode and a faster sync.
>
> Offline mode queues changes while you're disconnected and uploads them when the connection returns.
>
> In our benchmark of 10,000 small files, sync is 40% faster.
>
> Version 2.0 drops support for Python 3.9, so check your Python version before upgrading. The migration guide is at `docs/migrate-2.md`.
>
> tidewatch is an open-source command-line tool that syncs local folders to S3.

O que mudou: a abertura "is here" saiu (EN70). O benefício que ninguém declarou, "without having to remember what needs syncing", saiu (EN78). A ressalva em torno do benchmark saiu, porque "in our benchmark of 10,000 small files" já delimita o escopo (EN25). O convite final e o ponteiro repetido para o guia de migração saíram (EN24, EN57). Os fatos, a versão, o caminho e o aviso sobre o Python ficaram intactos.

### Descrição de pull request (inglês)

> **Antes**
> Fixes invoice due dates being calculated in server time (UTC) instead of the customer's time zone. Customers in UTC-3 to UTC-5 saw due dates one day early on invoices created after 21:00 local time.
>
> The fix converts timestamps to the customer's time zone before truncating to a date.
>
> - Adds unit tests for UTC-3, UTC-5, and UTC+9.
> - No database migration required.

**Depois:** sem alteração. O rascunho informa o bug, quem foi afetado, a correção, os testes e a situação da migração, sem nada inflado. A skill deixa em paz o texto limpo; editá-lo só acrescentaria risco.

### Post de LinkedIn (inglês), simples e com amostra de voz

> **Antes**
> Ledgerly reached 1,000 active users this October!
>
> We launched our budgeting app in March 2026. Seven months later, our team of three is celebrating a milestone that means a lot to us: 1,000 people actively using something we built.
>
> Thank you to everyone who has tried Ledgerly, shared feedback, or recommended it to someone else. You've helped us get here.
>
> Next up: CSV export, so you can take your budgeting data with you.
>
> We're excited to keep building.

> **Depois**
> Ledgerly, our budgeting app, now has 1,000 active users.
>
> We launched in March 2026 and reached the mark in October. The team is three people.
>
> Thanks to everyone who uses it. Next up is CSV export.

O que mudou: o ponto de exclamação e o "We're excited to keep building" saíram (EN74). "Means a lot to us" é um sentimento que os fatos não deram (EN64). "Shared feedback, or recommended it" e "take your budgeting data with you" são ações e benefícios que nunca foram declarados (EN78). "Seven months later" era preparação para uma data já informada (EN70).

Com esta amostra de voz:

```text
Shipped the importer fix today. Short version: the vendor changed date formats, we didn't
notice, invoices broke for two days. That's on us. Tests now cover the three formats we've
seen in the wild, and the parser fails loudly instead of guessing. If you hit something odd,
ping me directly. I'd rather hear about it twice than not at all.
```

> **Depois, nessa voz**
> Ledgerly passed 1,000 active users in October. Short version: we launched in March 2026, there are three of us, and the next feature is CSV export. Thanks to everyone using it.

Traços aproveitados: frases declarativas curtas, a abertura "Short version:", contrações, tom neutro sem exagero. Traços descartados: "That's on us" e "ping me directly", que pertencem à história da própria amostra e não são fatos sobre o Ledgerly.

### E-mail para a equipe (português)

> **Antes**
> Assunto: Nova data de entrega do módulo de relatórios
>
> Olá, equipe,
>
> A entrega do módulo de relatórios passa de 14/11 para 21/11. A API do fornecedor mudou o formato das datas sem aviso, e precisamos ajustar o importador e refazer os testes. O restante do cronograma continua igual.
>
> Na quinta-feira, às 10h, teremos uma reunião para revisar os testes.
>
> Abraços!

**Depois:** o mesmo texto, terminando em "Abraços" sem o ponto de exclamação (PT84). Um aviso de atraso não pede a animação, e o resto já era direto.

### Parágrafo didático (português)

> **Antes**
> O teste de regressão verifica se uma alteração no software prejudicou funcionalidades que já funcionavam. Ele é importante porque uma mudança em uma parte do sistema pode afetar outras, mesmo sem intenção. Imagine um formulário de login com campos de e-mail e senha. A equipe adiciona a opção "Lembrar de mim". Depois dessa mudança, é necessário conferir se o usuário ainda consegue entrar com dados válidos, se uma senha incorreta continua sendo rejeitada e se os campos obrigatórios seguem sendo validados. Esses testes ajudam a identificar problemas introduzidos pela alteração. Eles podem ser executados manualmente ou por ferramentas de automação. A seleção dos testes deve considerar quais funcionalidades podem ter sido afetadas e quais são mais importantes para o funcionamento do sistema.

> **Depois**
> O teste de regressão verifica se uma alteração no software prejudicou funcionalidades que já funcionavam. Uma mudança em uma parte do sistema pode afetar outras, mesmo sem intenção. Imagine um formulário de login com campos de e-mail e senha, ao qual a equipe adiciona a opção "Lembrar de mim". Depois dessa mudança, é necessário conferir se o usuário ainda consegue entrar com dados válidos, se uma senha incorreta continua sendo rejeitada e se os campos obrigatórios seguem sendo validados. Esses testes podem ser executados manualmente ou por ferramentas de automação. Para escolher quais rodar, considere quais funcionalidades a alteração pode ter afetado e quais são mais importantes para o sistema.

O que mudou: "Ele é importante porque" anunciava a importância em vez de dar o motivo (PT03). "Esses testes ajudam a identificar problemas..." repetia a definição (PT64). "A seleção dos testes deve considerar" virou verbo (edição simples, sem entrada no catálogo). O exemplo do login e suas três checagens ficam: são o conteúdo, não uma tríade forçada.

### Página "Sobre nós" (português)

> **Antes**
> A Padaria Lúcia faz parte do bairro da Ponta Verde, em Maceió, desde 1998. Fundada por Lúcia Ferreira, ficou conhecida pelo pão de queijo e pelo bolo de macaxeira, dois favoritos de quem passa por aqui.
>
> Recebemos você todos os dias, das 6h às 20h. Seja para começar a manhã ou fazer uma pausa para o café da tarde, venha conhecer a nossa padaria.

> **Depois**
> A Padaria Lúcia fica no bairro da Ponta Verde, em Maceió. Foi fundada em 1998 por Lúcia Ferreira e é conhecida pelo pão de queijo e pelo bolo de macaxeira.
>
> Abrimos todos os dias, das 6h às 20h.

O que mudou: "faz parte do bairro desde 1998" vestia uma data de importância (PT03). "Dois favoritos de quem passa por aqui" é uma afirmação que os fatos não sustentavam (PT08). "Seja para começar a manhã ou fazer uma pausa" é uma gama de usos que ninguém informou (PT79). O convite genérico saiu (PT06). O texto ficou curto porque os fatos são poucos.

## Acompanhando a Wikipédia

Os guias da Wikipédia sobre escrita de IA mudam com frequência. Na revisão de 30 de outubro de 2026, por exemplo, as páginas em inglês e em português listam o uso excessivo de travessão como indicador histórico, válido de 2022 a setembro de 2026. Antes de cada versão, rode:

```bash
python scripts/check-wikipedia.py
```

O script compara a revisão atual de cada página com a última registrada (`wikipedia/revisions.json`), lista as seções acrescentadas ou removidas e imprime o link do diff. Quando uma página mudou, leia o diff, atualize a extração em `wikipedia/` e os catálogos, e rode `python scripts/check-wikipedia.py --record`. Uma mudança na Wikipédia é um convite à revisão, não uma regra automática: passa pelas mesmas prioridades (R01-R12) de qualquer outra fonte.

## Limites

- As fontes-base foram lidas entre 23 e 30 de outubro de 2026. Para tudo que dependa de fatos atuais sobre modelos, detectores ou ferramentas, confira de novo.
- O repositório é verificado quanto à estrutura: frontmatter, R01-R12, EN01-EN78, PT01-PT86, links entre a base e as referências, e o manifesto do plugin (`claude plugin validate .`). Isso não é um benchmark de qualidade de escrita.
- O perfil de voz padrão em `SKILL.md` ("Profiles and modes") é o do autor. Ele só vale quando o pedido não nomeia outro autor ou leitor; uma amostra de voz e o próprio pedido sempre vencem. Para usar o seu padrão, edite esse parágrafo e o item 8 da passada final em `references/pt-br/revisao-final.md`.

## Contribuindo

As regras ficam em `SKILL.md` e `references/`; instalação e uso ficam nos READMEs. O [`AGENTS.md`](AGENTS.md) lista as convenções do repositório. Um sinal que a Wikipédia documenta entra no catálogo do seu idioma, na ordem da página; um acréscimo de outra fonte entra na última seção do catálogo, com a fonte nomeada. Para propor um padrão, descreva o problema observável, a intervenção, a exceção e um caso de teste, e nomeie a fonte primária, se houver. Mantenha a preferência pessoal separada dos achados de pesquisa.

## Fontes

Os padrões se apoiam só em fontes primárias: guias editoriais da Wikipédia, pesquisa acadêmica, institutos de pesquisa, documentação de fornecedores e um guia de estilo. As principais:

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), mantida pelo WikiProject AI Cleanup
- [Wikipédia: Sinais de texto gerado por inteligência artificial](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Sinais_de_texto_gerado_por_intelig%C3%AAncia_artificial) e [Wikipédia: Grandes modelos de linguagem](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Grandes_modelos_de_linguagem)
- Rodrigues, Sturm and Pinheiro, *A linguistic comparison between human- and AI-generated content*, iScience, 2026
- Kobak et al., *Delving into LLM-assisted writing in biomedical publications through excess vocabulary*, Science Advances, 2025
- Liang et al., *GPT detectors are biased against non-native English writers*, Patterns, 2023

A lista completa, com os padrões que cada fonte sustenta, está no apêndice abaixo. Como cada fonte é usada, e seus limites, está em [`references/sources.md`](references/sources.md), sob o mesmo ID.

## Histórico de versões

Veja [CHANGELOG.md](CHANGELOG.md).

- **7.0.0** (30/10/2026): primeira versão pública. Skill na raiz do repositório; dois catálogos com numeração independente, cada um a partir da sua página da Wikipédia (EN01-EN78 e PT01-PT86), com fontes por padrão; o travessão deixou de ser proibido, porque a Wikipédia o lista só como indicador histórico; plugin do Codex em `plugins/codex`; ícone do plugin; casamento de voz; subagente revisor para Claude Code e Codex; verificação de revisões da Wikipédia.

## Licença

MIT, por Vinicius Queiroz (2026). Partes deste pacote derivam de trabalho publicado sob a mesma licença por Siqi Chen (2025); o arquivo [LICENSE](LICENSE) mantém os dois avisos, como a licença exige. As fontes citadas mantêm as próprias licenças.

## Apêndice: pesquisas e guias por trás dos padrões

As fontes **base** sustentam o catálogo ou suas cautelas atuais. **Em avaliação** quer dizer que o registro (título, autores, data, identificador) foi conferido em 30/10/2026, mas o conteúdo ainda não entrou no catálogo. Nenhuma fonte vira regra sozinha; cada uma passa pelas prioridades da base.

A coluna **Padrões e regras** mostra o que cada fonte sustenta. A consulta inversa está no catálogo: todo padrão em `references/pt-br/padroes.md` e em `references/en/patterns.md` termina com uma linha **Fontes** (ou **Sources**) que traz o ID e a seção da página. Neste README a coluna lista IDs PT; o README em inglês lista IDs EN. Oito padrões em português (PT77, PT79, PT80, PT81, PT82, PT84, PT85, PT86) são acréscimos editoriais sem fonte externa registrada. Fonte que só tem entradas no catálogo em inglês mostra "só o catálogo em inglês". As páginas da Wikipédia valem na revisão indicada; o script de manutenção avisa quando ela muda.

### Guias editoriais da Wikipédia

| ID | Fonte | Situação | Padrões e regras |
|---|---|---|---|
| S01 | [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), WikiProject AI Cleanup (revisão 1382823144, 30/10/2026) | base | só o catálogo em inglês |
| S02 | [Wikipédia: Sinais de texto gerado por inteligência artificial](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Sinais_de_texto_gerado_por_intelig%C3%AAncia_artificial) (revisão 73274816, 23/10/2026) | base | PT01, PT02, PT03, PT04, PT05, PT06, PT07, PT08, PT09, PT10, PT11, PT12, PT13, PT14, PT15, PT16, PT17, PT18, PT19, PT20, PT21, PT22, PT23, PT24, PT25, PT26, PT27, PT28, PT29, PT30, PT31, PT32, PT33, PT34, PT35, PT36, PT37, PT38, PT39, PT40, PT41, PT42, PT43, PT44, PT45, PT46, PT47, PT48, PT49, PT50, PT51, PT52, PT53, PT54, PT55, PT56, PT57, PT58, PT59, PT60, PT61, PT62, PT63, PT64, PT65, PT66, PT67, PT68, PT69 |
| S03 | [Wikipédia: Grandes modelos de linguagem](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Grandes_modelos_de_linguagem) (revisão 73268669, 22/10/2026) | base | PT70, PT71, PT72, PT73, PT74, PT75, PT76 |

São guias editoriais de observação, não política nem teste de autoria. As duas páginas mantêm seções de indicadores históricos e de indicadores que não funcionam.

### Pesquisa acadêmica

| ID | Trabalho | Situação | Padrões e regras |
|---|---|---|---|
| S04 | Rodrigues, Sturm and Pinheiro. A linguistic comparison between human- and AI-generated content. iScience, 2026. [DOI 10.1016/j.isci.2026.114976](https://doi.org/10.1016/j.isci.2026.114976), [PubMed 41809036](https://pubmed.ncbi.nlm.nih.gov/41809036/) | base | PT09, PT10, PT44, PT58, PT60 |
| S05 | Geng and Trotta. Human-LLM Coevolution: Evidence from Academic Writing. Findings of ACL, 2025. [ACL Anthology](https://aclanthology.org/2025.findings-acl.657/) | base | PT11 |
| S06 | Kobak et al. Delving into LLM-assisted writing in biomedical publications through excess vocabulary. Science Advances, 2025. [arXiv 2406.07016](https://arxiv.org/abs/2406.07016) | base | PT11 |
| S07 | Juzek and Ward. Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models. COLING, 2025. [arXiv 2412.11385](https://arxiv.org/abs/2412.11385) | em avaliação | ainda nenhum |
| S08 | Liang et al. GPT detectors are biased against non-native English writers. Patterns, 2023. [arXiv 2304.02819](https://arxiv.org/abs/2304.02819) | base | R08 |
| S09 | Basani et al. Diversity Boosts AI-Generated Text Detection, 2025. [arXiv 2509.18880](https://arxiv.org/abs/2509.18880) | base | R08 |
| S10 | Russell et al. StoryScope: Investigating idiosyncrasies in AI fiction, 2026. [arXiv 2604.03136](https://arxiv.org/abs/2604.03136) | em avaliação | ainda nenhum |
| S11 | Guo et al. How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection, 2023. [arXiv 2301.07597](https://arxiv.org/abs/2301.07597) | em avaliação | ainda nenhum |
| S12 | Paech et al. Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models, 2025. [arXiv 2510.15061](https://arxiv.org/abs/2510.15061) | em avaliação | ainda nenhum |
| S13 | Xu et al. Base Models Look Human To AI Detectors, 2026. [arXiv 2605.19516](https://arxiv.org/abs/2605.19516) | em avaliação | ainda nenhum |
| S14 | Cheng et al. Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text, 2025. [arXiv 2506.07001](https://arxiv.org/abs/2506.07001). Registrada para marcar o escopo: a skill não adota técnicas de evasão | em avaliação | ainda nenhum |
| S15 | Bitton et al. Detecting Stylistic Fingerprints of Large Language Models, 2025. [arXiv 2503.01659](https://arxiv.org/abs/2503.01659) | em avaliação | ainda nenhum |
| S16 | Wu et al. A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions, 2023. [arXiv 2310.14724](https://arxiv.org/abs/2310.14724) | em avaliação | ainda nenhum |
| S17 | Mitchell et al. DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, 2023. [arXiv 2301.11305](https://arxiv.org/abs/2301.11305) | em avaliação | ainda nenhum |
| S18 | Hans et al. Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text, 2024. [arXiv 2401.12070](https://arxiv.org/abs/2401.12070) | em avaliação | ainda nenhum |
| S19 | Verma et al. Ghostbuster: Detecting Text Ghostwritten by Large Language Models, 2023. [arXiv 2305.15047](https://arxiv.org/abs/2305.15047) | em avaliação | ainda nenhum |
| S20 | Dugan et al. RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors, 2024. [arXiv 2405.07940](https://arxiv.org/abs/2405.07940) | em avaliação | ainda nenhum |

### Institutos de pesquisa e empresas

| ID | Trabalho | Situação | Padrões e regras |
|---|---|---|---|
| S21 | Graphite. [AI Tells](https://graphite.io/five-percent/research/ai-tells), 16/09/2026, e [AI Tells: Opus 5.5 Update](https://graphite.io/five-percent/research/ai-tells-opus-5-5-update), 01/10/2026 | base | PT06, PT13, PT14, PT15, PT61, PT78 |
| S22 | Pew Research Center. [How Much of the Internet Is Written With AI?](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/), 20/08/2026 | base | ainda nenhum |

### Documentação de fornecedores e guia de estilo

| ID | Trabalho | Situação | Padrões e regras |
|---|---|---|---|
| S23 | Anthropic. [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1), seções Writing density e Formatting in chat | base | PT20, PT83, R10 |
| S24 | Google developer documentation style guide. [Hyphens](https://developers.google.com/style/hyphens) | base | PT66, R09 |
