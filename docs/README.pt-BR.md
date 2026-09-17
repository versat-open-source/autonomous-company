# Autonomous Company

[English — fonte canônica](../README.md) · [Español](README.es.md)

Workspace de agentes para operações no Versat ERP por empresa, com instruções, skill importada, roteamento local privado e validação offline. Não instala um serviço nem executa transações por conta própria.

Responsável: **versat-open-source**; mantenedor: **@elviszoz**. Perfil: **agent / finance**, criticidade operacional alta. Governança fixada na revisão **9260d3a** do Versat AI Harness (VERSION **0.2.0**, mudanças ainda em Unreleased), com commit completo e hashes em `.versat/`. Consulte a [decisão de adoção](decisions/0002-consumer-agent-layout.md).

Use Python **3.12.14**. Execute na raiz:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
cp versat-companies.example.json versat-companies.local.json
bash scripts/validate/run.sh
```

Preencha o JSON local com suas empresas e nomes exatos das conexões MCP já configuradas no cliente. Tokens ficam na configuração segura do cliente. O arquivo local é ignorado pelo Git; nunca force sua inclusão.

Abra o workspace em um cliente que leia `AGENTS.md` e `.agents/skills/`. Siga o [fluxo operacional](../workflows/versat-operation/workflow.md): contexto ambíguo, configuração ausente, conexão indisponível ou escrita não autorizada impedem chamadas.

As skills ficam em `.agents/skills/`; o operador supervisionado é definido em `.codex/agents/operator.toml`. Os workflows usam `workflows/<nome>/workflow.md` e precisam ser carregados explicitamente. O carregamento nativo do operador exige um cliente Codex compatível e verificação separada; nenhum agendador é instalado. Consulte a [arquitetura dos agentes e os requisitos de execução](architecture/agent-project.md).

A validação cobre estilo, testes, 15 cenários fictícios, estrutura dos artefatos e vínculos de dependências, esquemas, integridade dos padrões e exclusão de dados privados. Não comprova descoberta nativa de agentes, comportamento do modelo nem conectividade real com o ERP.

Mudanças materiais seguem [SDD](../.versat/sdd/process.md), PR, revisão de CODEOWNERS e check `validate`. Consulte [contribuições](../CONTRIBUTING.md), [arquitetura](architecture/overview.md), [operações](operations.md), [segurança](../SECURITY.md) e [prontidão](readiness.md).

Nenhuma licença geral de distribuição foi escolhida. Publicação não concede licença de software; consulte a [proveniência](../THIRD_PARTY_NOTICES.md).
